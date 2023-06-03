from test_utility.utility_methods import UtilMethods
from page_objects.locators.login_locators import LoginPageLocator



class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.uti_obj = UtilMethods(self.driver)
        self.user_textbox_xpath = LoginPageLocator.user_textbox_xpath
        self.Password_textbox_xpath = LoginPageLocator.Password_textbox_xpath
        self.submit_button_xpath = LoginPageLocator.submit_button_xpath


    def enter_user_name(self, user_name):
        self.uti_obj.send_keys(self.user_textbox_xpath, user_name)

    def enter_password(self, password):
        self.uti_obj.send_keys(self.Password_textbox_xpath, password)


    def login(self, user_name, password):
        self.uti_obj.clear_text_box(self.user_textbox_xpath)
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.uti_obj.click(self.submit_button_xpath)


    def login_page(self):
        user = "standard_user"
        password = "secret_sauce"
        print("successfully login")
        self.login(user, password)
        # self.uti_obj.alert()
        login_url = "https://www.saucedemo.com/"
        if self.driver.current_url == login_url:
            result = True
        else:
            result = False
            print("Failed ot Login....")

        return result







