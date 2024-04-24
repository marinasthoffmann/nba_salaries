from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config import SELENIUM_DRIVER_PATH   

class Browser:
    
    def __init__(self) -> None:
        self.service = Service(SELENIUM_DRIVER_PATH)
        self.options = Options()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--incognito')
        # self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get(self, url):
        self.driver.get(url)

    def get_page_source(self):
        return self.driver.page_source

    def close(self):
        self.driver.quit()
