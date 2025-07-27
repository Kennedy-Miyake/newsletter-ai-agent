from abc import (ABC, abstractmethod)

class ScrapingStrategy(ABC):
    async def _get_raw_content(self, page):
        return await page.content()

    @abstractmethod
    def scrape_all_news(self):
        pass

    def scrape_news_content(self):
        pass