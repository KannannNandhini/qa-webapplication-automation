from time import sleep

from test_utility.utility_methods import UtilMethods
from page_objects.locators.addindcartlocator import AddingCartLocator
from page_objects.pages.login_page import LoginPage

class AddCart(object):

    def __init__(self, driver):
        self.driver = driver
        self.uti_obj = UtilMethods(self.driver)
        self.login_obj = LoginPage(self.driver)
        self.filter_cilck_xpath = AddingCartLocator.filter_cilck_xpath
        self.product_sauce_bike_light_xpath = AddingCartLocator.product_sauce_bike_light_xpath
        self.cart_list_logo_xpath = AddingCartLocator.cart_list_logo_xpath
        self.checkout_button_xpath = AddingCartLocator.checkout_button_xpath
        self.continue_shopping_button_xpath = AddingCartLocator.continue_shopping_button_xpath
        self.name_checkout_page_xpath = AddingCartLocator.name_checkout_page_xpath
        self.last_name_checkout_page_xpath = AddingCartLocator.last_name_checkout_page_xpath
        self.zip_pincode_checkout_page_xpath = AddingCartLocator.zip_pincode_checkout_page_xpath
        self.continue_button_xpath = AddingCartLocator.continue_button_xpath
        self.finish_button_xpath = AddingCartLocator.finish_button_xpath
        self.back_home_button_xpath = AddingCartLocator.back_home_button_xpath

    def enter_name(self, name):
        self.uti_obj.send_keys(self.name_checkout_page_xpath, name)

    def enter_lastname(self, lastname):
        self.uti_obj.send_keys(self.last_name_checkout_page_xpath, lastname)

    def enter_zipcode(self, zipcode):
        self.uti_obj.send_keys(self.zip_pincode_checkout_page_xpath, zipcode)

    def adding_products_to_the_cart(self):
        self.uti_obj.drop_down_visible_text(self.filter_cilck_xpath, "Name (Z to A)")
        self.uti_obj.click(self.product_sauce_bike_light_xpath)
        self.uti_obj.click(self.cart_list_logo_xpath)
        self.uti_obj.click(self.checkout_button_xpath)
        name = "nandhu"
        lastname = "kanna"
        zipcode = "12345"
        self.enter_name(name)
        self.enter_lastname(lastname)
        self.enter_zipcode(zipcode)
        self.uti_obj.click(self.continue_button_xpath)
        self.uti_obj.click(self.finish_button_xpath)
        self.uti_obj.click(self.back_home_button_xpath)
        sleep(10)
        print("Successfully Ordered")
        return True 
