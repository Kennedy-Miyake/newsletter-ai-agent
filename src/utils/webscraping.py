from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

class ScrapingNews:

    __website_url = None
    __news = []

    def __init__(self, website_name):
        self.__website_url = self.__get_website_url(website_name)
    
    def __get_website_url(self, website_name):
        websites = dict({
            'TechCrunch': 'https://techcrunch.com/category/artificial-intelligence/'
        })

        if website_name in websites.keys():
            return websites[website_name]
        
        print("Não existe site com esse nome!")

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

    def get_website_url(self):
        return self.__website_url

    def get_news(self):
        return self.__news