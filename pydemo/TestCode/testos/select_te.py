from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get(r'E:\tool\select.html')


# select_element = Select(driver.find_element(By XPATH, "//select[@id='s1Id']"))
select_element = Select(driver.find_element_by_xpath("//select[@id='s1Id']"))
select_element.select_by_index(1)
select_element.select_by_value('o2')
select_element.select_by_visible_text('o3')

for option in select_element.options:
    print(option.text)