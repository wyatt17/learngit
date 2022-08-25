class Mail:

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element_by_name("name").send_keys("sec")
        self.driver.find_element_by_name("password").send_keys("abc.12345")
        self.driver.find_element_by_id("login").click()

    def logout(self):
        self.driver.find_element_by_id("loginout").click()