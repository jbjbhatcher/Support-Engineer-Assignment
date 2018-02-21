# MARK: - imports
import json
from json import JSONEncoder
import urllib2

# selenium imports
from selenium import webdriver

username = 'jbhtcher@memphis.edu' # username to log in with
authkey = 'u63c4853726aabbb' # auth token
endpoint = "https://crossbrowsertesting.com/api/v3/selenium/browsers?format=json"
all_browsers_available = json.loads(urllib2.urlopen(endpoint).read())

# keep track of machine state w/ class
class Machine():
    def __init__(self, type):

        self.type = type # name of the machine to be tested
        # self.version =
        # self.platform =
        # self.screenResolution =

        self.didPass = None

        # convert the json data to python data

    def test_local_title(self): # should set Machine.didPass to True on success
        pass


# create machine instances
print all_browsers_available[0]['name']
print all_browsers_available[1]['name']
print all_browsers_available[2]['name']
