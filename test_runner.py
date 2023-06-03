import unittest
from test_script import tc_001_login_page
from HtmlTestRunner import HTMLTestRunner


class MyTestSuite(unittest.TestCase):

    def test_suite(self):

        login_page_script = unittest.TestLoader().loadTestsFromTestCase(tc_001_login_page.TestLoginPage)
        suite = unittest.TestSuite(login_page_script)
        runner = HTMLTestRunner(output='reports', report_title="TestCase Execution", report_name="TestExecutionReport",
                                verbosity=1, add_timestamp=True, combine_reports=False)

        runner.run(unittest.TestSuite(suite))


if __name__ == '__main__':
    obj = MyTestSuite()
    obj.test_suite()
