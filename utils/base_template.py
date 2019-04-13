import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chromedriver = webdriver.Chrome(ChromeDriverManager().install())


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = chromedriver

    def tearDown(self):
        self.driver.quit()
