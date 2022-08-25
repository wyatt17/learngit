from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.baidu.com")

element = driver.find_element_by_xpath("//ul[@id='hotsearch-content-wrapper']/li[1]/a/span[2]")
print(element.text)