from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.base import BasePage


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class HomePage(BasePage):
    logo = (By.CLASS_NAME, 'hero')
    name_input = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div/input')

    def __init__(self, driver):
        super().__init__(driver)  # Python3 version

    def set_name(self, name):
        self.hover(*self.name_input)
        self.find_element(*self.name_input).send_keys(name)

    def check_page_loaded(self):
        return True if self.find_element(*self.logo) else False
