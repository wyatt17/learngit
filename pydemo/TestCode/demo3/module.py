class Mail:
    def __init__(self, driver):
        self.driver = driver
 
    def login(self, username, password):

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login").click()

    def logout(self):

        self.driver.find_element_by_id("loginout").click()