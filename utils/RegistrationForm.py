from pages.locators import Registrationformlocator

class RegistrationForm:
    def __init__(self, driver):
        self.driver = driver


    def get_content_header_title(self):
        content_header_title = self.driver.find_element(*Registrationformlocator.get_content_header_title)
        return content_header_title.text