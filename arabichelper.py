import requests
from bs4 import BeautifulSoup


def get_page_html(url):
    page = requests.get(url)
    if page.status_code < 300:
        return page


def get_soup(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup



