import unittest
from selenium import webdriver
import requests

class SeleniumTestWindows(unittest.TestCase):
    def setUp(self):

        self.username = "jbhtcher@memphis.edu"
        self.authkey  = "u63c4853726aabbb"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None

        caps = {}
        caps['browserName'] = 'Chrome'
        caps['version'] = '60x64'
        caps['platform'] = 'Windows 10'
        caps['screenResolution'] = '1366x768'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey) # include username and authkey in url
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):
            self.driver.get('local:8000')
            self.assertEqual("local", self.driver.title)
            self.test_result = 'pass'
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()