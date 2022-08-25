from selenium import webdriver
import time
driver = webdriver.Edge()
driver.get(r'E:\tool\demo\upload\upload.html')

driver.find_element_by_name('file').send_keys(r'E:/1.txt')
time.sleep(2)
driver