from selenium_service.browser import Browser
from scraping.scraper import Scraper
from data_processor.data_processor import DataProcessor
from config import BASE_URL

browser = Browser()
scraper = Scraper(browser)
processor = DataProcessor()

for year in range(1990, 2024):
    page_number = f'{str(year)}-{str(year + 1)}/'
    url = f'{BASE_URL}{page_number}'
    
    scraped_data = scraper.scrape_page(url)
    processor.add_data(scraped_data, year)

browser.close()
processor.clean_data()
processor.save_to_csv('data.csv')
