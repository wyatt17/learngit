from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(r'E:\tool\checkbox.html') # 打开checkbox.html文件，使用绝对地址
checkboxs = driver.find_elements_by_xpath('//input[@type="checkbox"]')  # 获取批量的对象
for checkbox in checkboxs:  # 循环控制
   if not checkbox.is_selected():  # 判断多选框是否被选中
       checkbox.click()  # 单击
time.sleep(3)
driver.quit()