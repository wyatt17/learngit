
import unittest
from selenium import webdriver
from time import sleep
import codecs
from itertools import islice
import csv
from selenium.webdriver.common.by import By
from baidu_page1 import BaiduPage1
from base import BasePage

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.list1 = []
        cls.list2 = []
        with codecs.open("baidu_data.csv", 'r', 'gbk') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                cls.list1.append(line[1])
                cls.list2.append(line[2])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search_selenium(self):
        bd = BaiduPage1(self.driver)
        bd.get("https://www.baidu.com")

        bd.search_input =self.list1[0]
        bd.search_button.click()
        sleep(3)
        self.assertEqual(self.driver.title, self.list2[0])

    # def test_baidu_search_unittest(self):
    #     bd = BaiduPage(self.driver)
    #     bd.open()
    #     bd.search_input(self.list1[1])
    #     bd.search_button()
    #     bd.search_wait()
    #     self.assertEqual(self.driver.title, self.list2[1])

    # def test_baidu_search_pytest(self):
    #     bd = BaiduPage(self.driver)
    #     bd.open()
    #     bd.search_input(self.list1[2])
    #     bd.search_button()
    #     bd.search_wait()
    #     self.assertEqual(self.driver.title, self.list2[2])

if __name__ == '__main__':
    unittest.main()