from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.w3school.com.cn/cssref/pr_align-items.asp')

headers = driver.find_elements_by_xpath("//table[@class='definition-usage']/tbody/tr/th")
for head in headers:
    print(head.text)

# driver.quit()