import pytest
from selenium import webdriver
from Utils.Selenium_actions import SeleniumActions

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def actions(driver):
    return SeleniumActions(driver)
