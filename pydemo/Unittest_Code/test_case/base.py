from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url1 = None):
        if url1 is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url1)

    def get_title(self):
        return self.driver.get_title

    def search_wait(self, title = None):
        if title is None:
            WebDriverWait(self.driver, 5, 0.5).until_not(EC.title_is('百度一下，你就知道'))
        else:
            WebDriverWait(self.driver, 5, 0.5).until_not(EC.title_is(title))
