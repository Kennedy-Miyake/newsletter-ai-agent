import time
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

class NewsScraping:

    __website_url = None
    __news = []

    def __init__(self, website_name: str = 'Auto'):
        self.__website_url = self.set_website(website_name)
    
    def set_website(self, website_name: str = 'None'):
        website_name = website_name.lower()

        websites = dict({
            'auto': 'Auto',
            'techcrunch': 'https://techcrunch.com/category/artificial-intelligence/'
        })

        if website_name in websites.keys():
            return websites[website_name]

        while True:
            for name in websites:
                print(f'{name} - URL: {websites[name]}')
            
            website_name = str(input(f'Selecione qual site você deseja obter as notícias:'))

            if website_name in websites:
                self.__website_url = websites[website_name]
                return

    def get_website_url(self) -> str:
        return self.__website_url
    
    async def __get_content(self, url):
        async with async_playwright() as p:
            browser = await p.firefox.launch()
            page = await browser.new_page()
            await page.goto(url)
            content = await page.content()

            await browser.close()
            
            return content
    
    async def select_news(self):
        selected_news = dict()

        self.__news = await self.__fetch_techcrunch_news()

        i = 0
        for news in self.__news:
            (category, title, author, time) = news.values()
            print(f'{i} | {category} | {title}')
            print(f'{author} | {time}\n')
            i += 1

        select_news = int(input(f'Qual notícia você deseja selecionar (0-{(len(self.__news))-1})? R: '))
        if (select_news >= 0) and (select_news <= len(self.__news)):
            selected_news = self.__news[select_news]
            return selected_news

        print(f'Notícia não encontrada!')
        
    async def __fetch_techcrunch_news(self):
        news = []
        
        news_content = await self.__get_content(self.__website_url)
        news_parser = BeautifulSoup(news_content, 'html.parser')
        raw_news = news_parser.find_all('li', class_='wp-block-post', limit=30)
        for raw_news in raw_news:
            category = raw_news.find('div', class_='loop-card__cat-group').get_text(strip=True)
            title = raw_news.find('h3', class_='loop-card__title').get_text(strip=True)
            author = raw_news.find('ul', class_='loop-card__author-list').get_text(strip=True)
            time = raw_news.find('time', class_='loop-card__time').get_text(strip=True)
            news.append(dict({
                'Category': category,
                'Title': title,
                'Author': author,
                'Time': time
            })) 

        return news

    async def __get_techcrunch_news(self):
        async with async_playwright() as p:
            browser = await p.firefox.launch()
            page = await browser.new_page()
            await page.goto(self.__website_url)
            
            selected_news = await self.select_news() 

            await page.get_by_role('link', name=selected_news['Title']).click()

            time.sleep(0.5)
            raw_content = await page.content()
            parser = BeautifulSoup(raw_content, 'html.parser')

            news = parser.find('div', class_='wp-block-post-content')
            remove_elements = news.find_all('div')
            for r_element in remove_elements:
                r_element.extract()

            all_content = news.find_all(True)

            for content in all_content:
                if content.name == 'h2':
                    print(f'Title: ' + content.get_text(strip=True))
                    continue
                elif content.name == 'h3':
                    print(f'Subtitle:' + content.get_text(strip=True))
                    continue
                
                print(content.get_text(strip=True))
                
            await browser.close()

    def get_website_url(self):
        return self.__website_url

    def get_news(self):
        return self.__news