from bs4 import BeautifulSoup

class scraping:
    def __init__(self, content):
        self.raw_content = content

    def get_html_parser(self):
        return BeautifulSoup(self.raw_content, 'html.parser')