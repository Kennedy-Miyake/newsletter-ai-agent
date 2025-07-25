from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

class ScrapingNews:

    __website_url = None
    __notices = []

    def __init__(self, website_name):
        self.__website_url = self.__get_website_url(website_name)
    
    def __get_website_url(self, website_name):
        websites = dict({
            'TechCrunch': 'https://techcrunch.com/category/artificial-intelligence/'
        })

        if website_name in websites.keys():
            return websites[website_name]
        
        print("Não existe site com esse nome!")


        notices = []
        
        for raw_notice in raw_notices:
            category = raw_notice.find('div', class_='loop-card__cat-group').get_text(strip=True)
            title = raw_notice.find('h3', class_='loop-card__title').get_text(strip=True)
            author = raw_notice.find('ul', class_='loop-card__author-list').get_text(strip=True)
            time = raw_notice.find('time', class_='loop-card__time').get_text(strip=True)
            notices.append(dict({'Category': category, 'Title': title, 'Author': author, 'Time': time})) 

        return notices