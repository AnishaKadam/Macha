from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    user_input=(By.ID,"user-name")
    pass_input=(By.ID,"password")
    login=(By.CSS_SELECTOR,".submit-button.btn_action")
    inventory=(By.ID,"inventory_container")


    def __init__(self,driver,actions):
        self.driver=driver
        self.actions=actions

    def enter_url(self,url):
        print(f"entering {url}")
        self.driver.get(url)

    def login_website(self,username,password):
        print("entering login credentials")
        self.actions.enter_text(*self.user_input,username)
        self.actions.enter_text(*self.pass_input,password)
        self.actions.click(*self.login)

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver,10).until(
             EC.visibility_of_element_located(self.inventory)
            )
            print("Login successful")
            return True
        except:
            print("login unsuccessful")
            return False

