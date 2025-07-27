from abc import (ABC, abstractmethod)

class ScrapingStrategy(ABC):
    @abstractmethod
    def scrape_all_news(self):
        pass

    def scrape_news_content(self):
        pass