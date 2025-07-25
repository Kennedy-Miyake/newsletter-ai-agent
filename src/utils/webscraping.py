from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

class ScrapingNews:

    __website_url = None
    __notices = []

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
    
    async def __fetch_techcrunch_notices(self):
        notices = []
        
        notices_content = await self.__get_content(self.__website_url)
        notices_parser = BeautifulSoup(notices_content, 'html.parser')
        raw_notices = notices_parser.find_all('li', class_='wp-block-post', limit=30)
        for raw_notice in raw_notices:
            category = raw_notice.find('div', class_='loop-card__cat-group').get_text(strip=True)
            title = raw_notice.find('h3', class_='loop-card__title').get_text(strip=True)
            author = raw_notice.find('ul', class_='loop-card__author-list').get_text(strip=True)
            time = raw_notice.find('time', class_='loop-card__time').get_text(strip=True)
            notices.append(dict({
                'Category': category,
                'Title': title,
                'Author': author,
                'Time': time
            })) 

        return notices

    def get_website_url(self):
        return self.__website_url

    def get_notices(self):
        return self.__notices