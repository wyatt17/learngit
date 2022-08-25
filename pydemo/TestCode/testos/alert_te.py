from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get(r'E:\tool\demo\alert\promptTest.html')
# driver.get(r'E:/tool/demo/alert/alert2.html')
driver.find_element(By.XPATH, "//input[@name='button1']").click()
# driver.find_element_by_id('prompt').click()
alert = driver.switch_to.alert
print(alert.text)
WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.send_keys('zidonghuaceshi')
alert.accept()
WebDriverWait(driver, 5).until_not(EC.alert_is_present())
element = driver.find_element_by_xpath("//input[@name='t1']")
print(element.get_attribute("value"))