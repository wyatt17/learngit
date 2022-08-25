from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.url = "https://www.baidu.com"

    def baidu_input(self, values):
        
        # 这里变量values的self不需要加，只有当前函数内部才需要访问这个变量
        # self.values = values    # 加self表示全局变量
        self.driver.get(self.url)
        element = self.driver.find_element_by_name('wd')
        element.clear()
        element.send_keys(values)
        self.driver.find_element_by_xpath("//input[@id='su']").click()
        WebDriverWait(self.driver, 5, 0.5).until_not(EC.title_is('百度一下，你就知道'))

    def test_baidu_search_postman(self):
        value = "postman"
        self.baidu_input(value)
        self.assertEqual(self.driver.title, value+"_百度搜索")
 
    def test_baidu_search_apifox(self):     
        value = "apifox"
        self.baidu_input(value)
        self.assertEqual(self.driver.title, value+"_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestBaidu('test_baidu_search_postman'))
    suite.addTest(TestBaidu('test_baidu_search_apifox'))

    runner = unittest.TextTestRunner()
    runner.run(suite)