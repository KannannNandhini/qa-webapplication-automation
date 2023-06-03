from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class UtilMethods(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def send_keys(self, locator, value):
        try:
            self.driver.find_element_by_xpath(locator).send_keys(value)
        except Exception as e:
            print(e)

    def click_element(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def click(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def clear_text_box(self, locator):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,locator)))
        self.driver.find_element_by_xpath(locator).clear()

    def drop_down_visible_text(self, locator, text):

        select = Select(self.driver.find_element_by_xpath(locator))
        select.select_by_visible_text(text)

    def drop_down_value(self, locator, value):

        select = Select(self.driver.find_element_by_xpath(locator))
        select.select_by_value(value)

    def drop_down_index(self, locator, index):

        select = Select(self.driver.find_element_by_xpath(locator))
        select.select_by_index(index)

    def alert(self):

        alert=Alert (self.driver)
        alert.accept()





