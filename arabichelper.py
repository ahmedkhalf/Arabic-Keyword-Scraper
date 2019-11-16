import requests
from bs4 import BeautifulSoup


class console_log:
    logLevel = 3 # 3: debug, 2: warn, 1: error

    @staticmethod
    def debug(msg):
        if console_log.logLevel >= 3:
            print("[DEBUG]   " + msg)
    
    @staticmethod
    def warn(msg):
        if console_log.logLevel >= 2:
            print("[WARNING] " + msg)

    @staticmethod
    def error(msg):
        if console_log.logLevel >= 1:
            print("[ERROR]   " + msg)


def get_page_html(url):
    page = requests.get(url)
    if page.status_code < 300:
        return page


def get_soup(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


console_log.debug("Starting Program!")
