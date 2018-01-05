from bs4 import BeautifulSoup
import requests


class Scraper:
    def make_request(self, url):
        r = requests.get(url)
        return r.text

    def scrape_url(self, url):
        soup = BeautifulSoup(self.make_request(url), 'html.parser')
        return soup.title.string
