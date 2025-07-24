from bs4 import BeautifulSoup

class Scraping:
    def __init__(self, content):
        self.raw_content = content
        self.parser_content = self.get_html_parser()

    def get_html_parser(self):
        return BeautifulSoup(self.raw_content, 'html.parser')

    def techcrunch(self):
        notices = []
        
        raw_notices = self.parser_content.find_all('li', class_='wp-block-post', limit=30)
        for raw_notice in raw_notices:
            category = raw_notice.find('div', class_='loop-card__cat-group').get_text(strip=True)
            title = raw_notice.find('h3', class_='loop-card__title').get_text(strip=True)
            author = raw_notice.find('ul', class_='loop-card__author-list').get_text(strip=True)
            time = raw_notice.find('time', class_='loop-card__time').get_text(strip=True)
            notices.append(dict({'Category': category, 'Title': title, 'Author': author, 'Time': time})) 

        return notices