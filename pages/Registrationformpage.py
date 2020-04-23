from selenium.webdriver.common.by import By


class RegistrationPage():
    def __init__(self, driver):
        self.driver = driver;
        self.email = (By.ID, 'email')
        self.password = (By.CLASS_NAME, 'password')
        self.cfnpassword = (By.NAME, 'cnfpassword')
        self.first_name = (By.NAME, 'first_name')
        self.last_name = (By.NAME, 'last_name')
        self.username = (By.CLASS_NAME, 'form-control.username')
        self.textarea =(By.ID, 'textarea')
        self.submit = (By.ID, 'submitForm')

    def register(self, email):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(('payal@123'))
        self.driver.find_element(*self.cfnpassword).send_keys(('payal@123'))
        self.driver.find_element(*self.first_name).send_keys('Payal')
        self.driver.find_element(*self.last_name).send_keys('Priya')
        self.driver.find_element(*self.username).send_keys('payalpriya02@gmail.com')
        self.driver.find_element(*self.textarea).send_keys('payalpriya@123')
        self.driver.find_element(*self.submit).click()

