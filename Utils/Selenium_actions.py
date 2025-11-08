from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class SeleniumActions:
    def __init__(self,driver):
        self.driver=driver

    def enter_text(self, locator_type,locator_value,text):
        element=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((locator_type,locator_value))
        )
        element.clear()
        element.send_keys(text)

    def click(self,locator_type,locator_value):
        element=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((locator_type,locator_value))
        )
        element.click()

    def mouse_hover(self,locator_type,locator_value):
        element=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((locator_type,locator_value))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def select_element(self,locator_type,locator_value,text):
        element=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((locator_type,locator_value))
        )
        select=Select(element)
        select.select_by_visible_text(text)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
