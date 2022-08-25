from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

action = ActionChains(driver)

element = driver.find_element_by_id("123")
action.double_click(element).perform()

action.move_to_element(element).perform()

sour = driver.find_element_by_id("1233")
target = driver.find_element_by_class_name("1234")
action.drag_and_drop(sour, target).perform()

action.click_and_hold(sour).move_to_element(target).release().perform()

action.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()