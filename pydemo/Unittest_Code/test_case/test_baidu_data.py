import csv
import unittest
from selenium import webdriver
from time import sleep
import codecs
from itertools import islice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from baidu_page import BaiduPage

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.url = "https://www.baidu.com"
        cls.list1 = []
        cls.list2 = []
        with codecs.open('baidu_data.csv', 'r', 'gbk') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                cls.list1.append(line[1])
                cls.list2.append(line[2])
                
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 这里的content不会被其他方法访问，不需要加self
    def baidu_search(self, content):
        self.driver.get(self.url)
        # self.driver.find_element_by_id("kw").send_keys(content)
        # self.driver.find_element_by_id("su").click()

        self.driver.find_element(By.ID, 'kw').send_keys(content)
        self.driver.find_element(By.ID, 'su').click()
        # sleep(3)
        self.driver.find_element_by_xpath("//input[@id='su']").click()
        WebDriverWait(self.driver, 5, 0.5).until_not(EC.title_is('百度一下，你就知道'))

    def test_baidu_search_selenium(self):
        self.baidu_search(self.list1[0])
        self.assertEqual(self.driver.title, self.list2[0])
    
    def test_baidu_search_unittest(self):
        self.baidu_search(self.list1[1])
        self.assertEqual(self.driver.title, self.list2[1])

    def test_baidu_search_pytest(self):
        self.baidu_search(self.list1[2])
        self.assertEqual(self.driver.title, self.list2[2])

if __name__ == '__main__':
    unittest.main()