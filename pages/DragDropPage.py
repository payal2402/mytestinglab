
from selenium.webdriver import ActionChains

class DragDrop:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def hover(self):
          self.driver.find_element_by_xpath("//span[text()='Mouse Actions']").click()
          self.driver.find_element_by_link_text('Hover Menus').click()
          self.driver.find_element_by_partial_link_text('Simple').click()
          btn = self.driver.find_element_by_css_selector('.dropbtn')
          self.action.move_to_element(btn).perform()
          self.driver.find_element_by_css_selector('[href="#textOne"]').click()


    def drag_n_drop(self):
          self.driver.find_element_by_xpath("//span[text()='Mouse Actions']").click()
          self.driver.find_element_by_link_text('Drag and Drop').click()
          event = self.driver.find_element_by_xpath("//div[text()='My Event 1']")
          today = self.driver.find_element_by_css_selector('td.fc-today')
          # self.action.drag_and_drop(event, today).perform()
          self.action.click_and_hold(event).move_to_element(today).release(today).perform()