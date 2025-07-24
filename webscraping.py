from bs4 import BeautifulSoup

class scraping:
    def __init__(self, content):
        self.raw_content = content
        self.parser_content = self.get_html_parser()

    def get_html_parser(self):
        return BeautifulSoup(self.raw_content, 'html.parser')
