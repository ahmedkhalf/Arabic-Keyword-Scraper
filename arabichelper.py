import eel
import requests
from bs4 import BeautifulSoup
from threading import Thread


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


class Word():
    def __init__(self, word):
        self.word = word
        self.meanings = []
        self.lookup_done = False

    def get_url(self):
        return "https://www.almaany.com/ar/dict/ar-ar/" + self.word


    def get_page_html(self, url):
        page = requests.get(url)
        if page:
            if page.status_code < 300:
                return page


    def get_soup(self, page):
        soup = BeautifulSoup(page.content, "html.parser")
        return soup


    def get_meanings(self, soup):
        wordlist = soup.find("ol", {"class": "meaning-results"}).findAll("li", recursive=False)
        console_log.debug("Adding meanings for word: " + self.word)
        for word in wordlist:
            self.meanings.append(word.text)


    def select_meaning(self):
        console_log.debug("Selecting meanings for word: " + self.word)
        for word in self.meanings:
            eel.add_meaning(word.text)
        eel.print_meaning()


    def lookup(self):
        url = self.get_url()
        page = self.get_page_html(url)
        if page == None:
            console_log.error("Could not get page for word: " + self.word + ", please check your internet connection")
        soup = self.get_soup(page)
        self.get_meanings(soup)
        self.lookup_done = True


def get_words():
    global WordList
    for word in WordList:
        word.lookup()


@eel.expose
def lookup_words(text):
    console_log.debug("lookup_words called")
    global WordList
    WordList = []
    words = text.splitlines()
    for word in words:
        word = word.strip()
        if word != "":
            WordList.append(Word(word))  # Word("كشافة").lookup()
    thread = Thread(target = get_words)
    thread.start()


@eel.expose
def request_words():
    console_log.debug("Requested Words")
    global WordList
    words = []
    for word in WordList:
        words.append(word.word)
    return words

@eel.expose
def get_meaning(id):
    global WordList
    if id < len(WordList):
        while True:
            if WordList[id].lookup_done:
                eel.add_meaning(WordList[id].meanings)
                break


def on_close(page, sockets):
	console_log.debug(page +  " closed")


web_options = {
	"mode": "chrome-app",
	"host": "localhost",
	"port": 8000,
    "cmdline_args": ["--disable-extensions"]
}


def main():
    print("[ Arabic Keyword Scraper Console ]\n")
    console_log.debug("Starting Program!")
    eel.init("web_view")
    eel.start("index.html", size=(507, 595), options=web_options, callback=on_close)


if __name__ == "__main__":
    main()
