from bs4 import BeautifulSoup
import requests


class Scraper:
    def scrape_url(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title_arr = soup.title.string.split()
        scraped_title = ' '.join(title_arr[:-2])  # slicing off '- Youtube' at the end of the title
        return scraped_title
