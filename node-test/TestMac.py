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
        caps['name'] = 'Selenium Test Example Mac'
        caps['build'] = '1.0'
        caps['browserName'] = 'Safari'
        caps['platform'] = 'Mac OSX 10.9'
        caps['screenResolution'] = '2560x1440'


        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey) # include username and authkey in url
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):
        try:
            self.driver.get('http://local:8000')
            self.assertEqual("Hello world!", self.driver.title)
            self.test_result = 'pass'
            self.driver.quit()
        except:
             print("Unexpected error:", sys.exc_info()[0])
             raise


if __name__ == '__main__':
    unittest.main()
