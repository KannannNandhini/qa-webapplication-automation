from test_evironments.environmenys_setup import EnvironmentSetup
from page_objects.pages.login_page import LoginPage
from page_objects.pages.adding_cart import AddCart


class TestLoginPage(EnvironmentSetup):

    def setUp(self):
        self.login_page_obj = LoginPage(self.driver)
        self.add_cart_obj = AddCart(self.driver)
        self.result = None

    def tearDown(self):
        test_name = self._testMethodName
        print(test_name)

    def test_001_login(self):
        self.result = self.login_page_obj.login_page()
        self.result = True
        self.assertTrue(self.result)

    def test_002_adding_product_to_the_product(self):
        self.result = self.add_cart_obj.adding_products_to_the_cart()
        self.assertTrue(self.result)
