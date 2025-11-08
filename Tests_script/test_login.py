from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.Selenium_actions import SeleniumActions
from POM.Login_page import LoginPage

def test_login_website(driver,actions):
    login=LoginPage(driver,actions)
    login.enter_url("https://www.saucedemo.com/")
    login.login_website("standard_user","secret_sauce")
    
    assert login.is_logged_in(),"Login failed"
    