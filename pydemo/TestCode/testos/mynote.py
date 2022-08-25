from selenium import webdriver


driver = webdriver.Edge()

driver.get(r'E:\tool\demo\alert\promptTest.html')
element = driver.find_element_by_xpath("//input[@name='t1']")
element.send_keys('12')
print(element.get_attribute("value"))