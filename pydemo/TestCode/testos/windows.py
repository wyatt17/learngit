from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get('https://www.sogou.com/')

driver.find_element_by_link_text("搜狗输入法").click()
nowhandle = driver.current_window_handle
print(nowhandle)
print(driver.title)

allheadles = driver.window_handles
for allhead in allheadles:
    if allhead != nowhandle:
        driver.switch_to.window(allhead)
        time.sleep(2)