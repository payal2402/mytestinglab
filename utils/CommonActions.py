
from pages.locators import Loginlocator


class CommonActions:
    def __init__(self, driver):
        self.driver = driver


    def get_logo_name(self):
        logo = self.driver.find_element(*Loginlocator.logoName)
        return logo.text