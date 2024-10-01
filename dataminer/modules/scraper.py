# modules/scraper.py
import requests
from modules.utils import logger
from config.settings import USER_AGENT

class Scraper:
    def __init__(self):
        self.headers = {'User-Agent': USER_AGENT}

    def fetch(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            logger.info(f'Successfully fetched {url}')
            return response.text
        except requests.RequestException as e:
            logger.error(f'Error fetching {url}: {e}')
            return None
