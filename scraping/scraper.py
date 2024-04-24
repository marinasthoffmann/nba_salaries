from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, browser):
        self.browser = browser

    def scrape_page(self, url):

        self.browser.get(url)
        soup = BeautifulSoup(self.browser.get_page_source(), 'html.parser')

        players = self.get_elements_list_by_class_name(soup, "name")
        salaries = self.get_elements_list_by_class_name(soup, "hh-salaries-sorted")

        data_tuples = list(zip(players[1:], salaries[1:]))

        return data_tuples  
   
    def get_elements_list_by_class_name(self, soup, class_name):  
        elements = soup.find_all("td", attrs={"class": f"{class_name}"})
        return [element.text.strip() for element in elements]
    