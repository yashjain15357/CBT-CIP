# modules/parser.py
from bs4 import BeautifulSoup
from modules.utils import logger

class Parser:
    def parse(self, html, selectors):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            data = {}
            for key, selector in selectors.items():
                element = soup.select_one(selector)
                data[key] = element.text.strip() if element else None
            logger.info('Successfully parsed HTML')
            return data
        except Exception as e:
            logger.error(f'Error parsing HTML: {e}')
            return None
