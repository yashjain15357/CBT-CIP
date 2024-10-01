# main.py
from modules.scraper import Scraper
from modules.parser import Parser
from modules.storage import Storage
from modules.utils import logger

def main():
    url = 'https://www.linkedin.com/analytics/creator/content/?metricType=IMPRESSIONS&timeRange=past_7_days'
    selectors = {
        'title': 'h1.title',
        'date': 'time.date',
        'author': '.author-name'
    }

    scraper = Scraper()
    parser = Parser()
    storage = Storage()

    html = scraper.fetch(url)
    if html:
        data = parser.parse(html, selectors)
        if data:
            storage.save_to_csv(data, 'data/output.csv')
            storage.save_to_db(data, 'scraped_data')

if __name__ == '__main__':
    main()
