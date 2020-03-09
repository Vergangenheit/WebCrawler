from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request


class AmazonScraper(object):

    def __init__(self, website, search):
        self.website = website
        self.search = search

        self.driver = webdriver.Chrome(r"C:/Users/User/chromedriver/chromedriver.exe")
        self.delay = 3

    def test(self):
        self.driver

    def search_amazon(self):
        self.driver.get(self.website)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
            print("Page is ready")
            element = self.driver.find_element_by_id("twotabsearchtextbox")
            element.send_keys(self.search)
            self.driver.find_element_by_xpath("""//*[@id="nav-search"]/form/div[2]/div/input""").click()
        except TimeoutException:
            print("Loading took too much time")

    def extract_results(self):

        products = []
        prices = []
        i = 0
        while i < len(
                self.driver.find_elements_by_css_selector(".a-size-medium.s-inline.s-access-title.a-text-normal")):
            link = self.driver.find_elements_by_css_selector(".a-size-medium.s-inline.s-access-title.a-text-normal")[i]
            link.click()
            product = self.driver.find_element_by_id("productTitle")
            try:
                price = self.driver.find_element_by_id("priceblock_ourprice")
                print(str(product.text) + ":" + str(price.text))
                products.append(product.text)
                prices.append(price.text)
                self.driver.back()
                i += 1
            except:
                try:
                    price = self.driver.find_element_by_css_selector(
                        ".a-size-base.a-color-price.offer-price.a-text-normal")
                    print(str(product.text) + ":" + str(price.text))
                    products.append(product.text)
                    prices.append(price.text)
                    self.driver.back()
                    i += 1
                except:
                    self.driver.back()
                    i += 1
                    pass

        return products, prices

    def extract_urls(self):

        url_list = []
        i = 0
        while i < len(
                self.driver.find_elements_by_css_selector(".a-size-medium.s-inline.s-access-title.a-text-normal")):
            link = self.driver.find_elements_by_css_selector(".a-size-medium.s-inline.s-access-title.a-text-normal")[i]
            link.click()
            try:
                url_list.append(self.driver.current_url)
                self.driver.back()
                i += 1
            except:
                self.driver.back()
                i += 1
                pass

    def quit(self):
        self.driver.close()


if __name__ == "__main__":
    scraper = AmazonScraper("https://www.amazon.com/", "Apple iPhone 7")
    scraper.search_amazon()
    scraper.extract_results()
    scraper.quit()