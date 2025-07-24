from bs4 import BeautifulSoup

class Scraping:
    def __init__(self, content):
        self.raw_content = content
        self.parser_content = self.get_html_parser()

    def get_html_parser(self):
        return BeautifulSoup(self.raw_content, 'html.parser')

    def techcrunch(self):
        raw_notices = self.parser_content.find_all('ul', class_='wp-block-post-template')
        print(raw_notices)