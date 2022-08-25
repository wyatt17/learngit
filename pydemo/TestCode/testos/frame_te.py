from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get(r'E:\tool\demo\frame\frame.html')

element = driver.find_elements_by_xpath("//input[@type='text']")
element.send_keys("123wai")
driver.switch_to.frame('f1')
print(driver.find_elements_by_id('innerlable').text)
driver.find_elements_by_id("innerlable").click()
driver.switch_to.frame('f2')
driver.switch_to.parent_frame()
driver.switch_to.default_content()

