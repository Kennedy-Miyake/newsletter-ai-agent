from src.scraping_strategies.scraping_strategy import ScrapingStrategy

class TechCrunchScrapingStrategy(ScrapingStrategy):
    def scrape_all_news(self, parser):
        news = []

        raw_news = parser.find_all('li', class_='wp-block-post', limit=30)
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

    def scrape_news_content(self):
        pass