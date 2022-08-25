from selenium import webdriver
from module import Mail
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
driver = webdriver.Firefox()
driver.get("https://10.5.19.55/")

# 调用 Mail 类并接收 driver 驱动
mail = Mail(driver)    # mail就是实例化对象
# 登录
mail.login()
# 登录之后的动作
sleep(3)
WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id('loginout'))
# 退出
mail.logout()

driver.quit()