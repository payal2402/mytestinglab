from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver;
        self.emailInput = (By.XPATH, '//input[@placeholder="Enter email"]')
        self.loginBtn = (By.CSS_SELECTOR, 'button')

    def login(self, email):
        self.driver.find_element(*self.emailInput).send_keys(email)
        self.driver.find_element(*self.loginBtn).click()