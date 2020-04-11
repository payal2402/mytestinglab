
from pages.locators import CommonLocators


class CommonActions:
    def __init__(self, driver):
        self.driver = driver


    def get_logo_name(self):
        logo = self.driver.find_element(*CommonLocators.logoName)
        return logo.text