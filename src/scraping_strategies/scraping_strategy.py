from abc import (ABC, abstractmethod)

class ScrapingStrategy(ABC):
    @abstractmethod
    def scrape_all_news(self, parser):
        pass

    def select_news(self, all_news):
        pass

    def scrape_news_content(self):
        pass