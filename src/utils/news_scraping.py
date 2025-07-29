import time
from src.scraping_strategies.scraping_strategy import ScrapingStrategy
from src.scraping_strategies import techcrunch_strategy
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

class NewsScraping:

    __default_websites = dict({
        'auto': 'Auto',
        'techcrunch': 'https://techcrunch.com/category/artificial-intelligence/'
    })
    __default_strategies = dict({
        'auto': None,
        'techcrunch': techcrunch_strategy.TechCrunchScrapingStrategy()
    })

    __strategy = dict({})
    __website = dict({})
    __news = []

    def __init__(self, website_name: str = 'Auto'):
        self.__website = self.set_website(website_name)
        self.__register_strategy()
    
    def set_website(self, website_name: str = 'None'):
        website_name = website_name.lower()

        if website_name in self.__default_websites.keys():
            return dict({
                website_name: self.__default_websites[website_name]
            })

        while True:
            for name in self.__default_websites:
                print(f'{name} - URL: {self.__default_websites[name]}')
            
            website_name = str(input(f'Selecione qual site você deseja obter as notícias:'))

            if website_name in self.__default_websites:
                self.__website = dict({
                    website_name: self.__default_websites[website_name]
                })
                return

    def get_website_url(self) -> str:
        domain = next(iter(self.__website))
        return self.__website[domain]

    def __register_strategy(self):
        domain = next(iter(self.__website))
        if domain in self.__default_strategies:
            self.__strategy = dict({
                domain: self.__default_strategies[domain]
            })
            return

    async def __parser_html(self, page):
        content = await page.content()
        return BeautifulSoup(content, 'html.parser')

    async def fetch_news(self, page):
        strategy = next(iter(self.__strategy.values()))
        parser = await self.__parser_html(page)

        self.__news = strategy.scrape_all_news(parser)
    
    async def goto_news(self, page):
        strategy = next(iter(self.__strategy.values()))
        selected_news = strategy.select_news(self.__news)

        await page.get_by_role('link', name=selected_news['Title']).click()
        time.sleep(0.5)
    
    async def get_news_article(self, page):
        strategy = next(iter(self.__strategy.values()))
        parser = await self.__parser_html(page)
        
        article = strategy.scrape_news_content(parser)
        return article