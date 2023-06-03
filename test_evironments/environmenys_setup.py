import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class EnvironmentSetup(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        base_url = "https://www.saucedemo.com/"
        self.driver.get(base_url)

    # @classmethod
    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()
