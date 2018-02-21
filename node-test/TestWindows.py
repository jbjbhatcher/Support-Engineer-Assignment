import unittest
from selenium import webdriver
import requests
import sys

class SeleniumTestWindows(unittest.TestCase):
    def setUp(self):

        self.username = "jbhtcher@memphis.edu"
        self.authkey  = "u63c4853726aabbb"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None

        caps = {}
        caps['name'] = 'Selenium Test Example'
        caps['build'] = '1.0'
        caps['browserName'] = 'Chrome'
        caps['deviceName'] = 'Nexus 6P'
        caps['platformVersion'] = '7.0'
        caps['platformName'] = 'Android'
        caps['deviceOrientation'] = 'portrait'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey) # include username and authkey in url
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):
        try:
            self.driver.get('local:8000')
            self.assertEqual("local", self.driver.title)
            self.test_result = 'pass'
            self.driver.quit()
        except:
             print("Unexpected error:", sys.exc_info()[0])
             raise


if __name__ == '__main__':
    unittest.main()
