# MARK: - imports
import json
from json import JSONEncoder
import urllib2

# selenium imports
from selenium import webdriver

username = # username to log in wiht
authkey = # auth token

# keep track of machine state w/ class
class Machine():

    endpoint = "https://crossbrowsertesting.com/api/v3/selenium/browsers?format=json"

    def __init__(self, type):

        self.type = type # name of the machine to be tested
        self.version =
        self.platform =
        self.screenResolution =

        self.didPass = None

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )

        self.driver.implicitly_wait(20)


    def test_local_title(self): # should set Machine.didPass to True on success
        self.driver.get('local:8000') # specify the URL to test on
        self.assertEqual('Hello world!', self.driver.title)


    def get_all_available_browsers(self): # this method is called on an instance, and returns a JSON string containing all of the browsers available.
        all_browsers = urllib2.urlopen(self.endpoint).read()
        return all_browsers

# create machine instances
windows = Machine('Windows')
mac = Machine('Mac')
mobile = Machine('iPad')

# testing
print windows.type
print windows.get_all_available_browsers()
