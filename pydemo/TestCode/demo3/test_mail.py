from time import sleep
from selenium import webdriver
from module import Mail
from read_csv import users1

driver = webdriver.Firefox()
driver.get("https://10.5.8.239")
mail = Mail(driver)
# 登录
sleep(2)
# mail.login('sec', 'abc.12345')
mail.login(users1[0][0], users1[0][1])

# 登录之后的动作
sleep(5)
# 退出
mail.logout()
driver.quit()