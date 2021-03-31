import requests
import bs4
from bs4 import BeautifulSoup


class JokeScraper:
    '''
    Scraps web pages through the BeautifulSoup library. 
    It extracts data from HTML pages, and returns a list 
    of jokes.
    '''

    def __init__(self):
        page = requests.get(
            "https://www.boredpanda.com/funny-pun-jokes/?utm_source=google&utm_medium=organic&utm_campaign=organic")
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def get_jokes(self):
        '''
        Retuns a list of jokes from the web pages' span tag
        '''
        jokes = self.soup.find_all('span', class_="bordered-description")
        joke_list = []  # list of jokes
        for joke in jokes:
            joke_list.append(joke.text)
        return joke_list
