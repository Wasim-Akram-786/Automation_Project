class LoginPage:
    # locator
    username_id = 'Email'
    password_id= "Password"
    button = "//button[@type='submit']"
    logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    # Defined Action method

    def setUserName(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_linktext).click()
