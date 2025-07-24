from bs4 import BeautifulSoup

class Scraping:

    __raw_content = None
    __parser_content = None
    
    def __init__(self, content):
        self.__raw_content = content
        self.__parser_content = self.__get_html_parser()

    def __get_html_parser(self):
        return BeautifulSoup(self.__raw_content, 'html.parser')

    def get_techcrunch_notices(self):
        notices = []
        
        raw_notices = self.__parser_content.find_all('li', class_='wp-block-post', limit=30)
        for raw_notice in raw_notices:
            category = raw_notice.find('div', class_='loop-card__cat-group').get_text(strip=True)
            title = raw_notice.find('h3', class_='loop-card__title').get_text(strip=True)
            author = raw_notice.find('ul', class_='loop-card__author-list').get_text(strip=True)
            time = raw_notice.find('time', class_='loop-card__time').get_text(strip=True)
            notices.append(dict({'Category': category, 'Title': title, 'Author': author, 'Time': time})) 

        return notices