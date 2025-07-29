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
    
    def select_news(self, all_news):
        selected_news = dict({})

        i = 0
        for news in all_news:
            (category, title, author, time) = news.values()
            print(f'{i} | {category} | {title}')
            print(f'{author} | {time}\n')
            i += 1

        while True:
            select_news = int(input(f'Qual notícia você deseja selecionar (0-{(len(all_news))-1})? R: '))
            if (select_news >= 0) and (select_news <= len(all_news)):
                selected_news = all_news[select_news]
                return selected_news

            print(f'Notícia não encontrada!')

    def scrape_news_content(self, parser):
        news = parser.find('div', class_='wp-block-post-content')
        remove_elements = news.find_all('div')
        for element in remove_elements:
            element.extract()

        all_content = news.find_all(True)

        full_content = ""
        for content in all_content:
            if content.name == 'h2':
                full_content += (f'Title: ' + content.get_text(strip=True) + '\n')
                continue
            elif content.name == 'h3':
                full_content += (f'Subtitle:' + content.get_text(strip=True) + '\n')
                continue

            full_content += (content.get_text(strip=True) + '\n')
        
        return full_content