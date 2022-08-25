from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
action = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.bing.com")

element = driver.find_element(By.XPATH, "//input[@id='sb_form_q']")
element.send_keys("selenium")
action.click(element).perform()

action.double_click().key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys('V').send_keys('V').key_up(Keys.CONTROL).perform()