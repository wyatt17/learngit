from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(r'http://www.w3school.com.cn/cssref/css_selectors.asp')
# //table[@class="dataintable"]//tr[1]//th 获取表头元素
table_header = driver.find_elements_by_xpath('//table[@class="dataintable"]//tr[1]//th')
for header in table_header:  # 循环获取元素
    print(header.text)  # 打印文本内容
driver.quit()