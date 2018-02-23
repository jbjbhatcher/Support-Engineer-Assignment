# MARK: - imports
import json
from json import JSONEncoder
import urllib2
import requests

# selenium imports
from selenium import webdriver

username = 'jbhtcher@memphis.edu' # username to log in with
authkey = 'u63c4853726aabbb' # auth token

# MARK: - endpoints used with the CBT API
all_browsers_endpoint = "https://crossbrowsertesting.com/api/v3/selenium/browsers?format=json"
all_browsers_available = json.loads(urllib2.urlopen(all_browsers_endpoint).read())

test_history_endpoint = "https://crossbrowsertesting.com/api/v3/selenium?format=json"

class Machine():
    def __init__(self, name):
        self.asJson = None
        for i in range(len(all_browsers_available)): # purpose of this loop is to iterate over list of all possible browsers and to find the first matching occurence of a desired machine
            if all_browsers_available[i]['name'] == name and self.asJson is None:
                self.asJson = all_browsers_available[i]
                break # found the value so break
        self.api_name = self.asJson['api_name']
        self.caps = {
            'name': 'Selenium Test',
            'build': '1.0',
            'deviceName': self.asJson['name']
        }

        # construct the caps

    def __str__( self ):
        return 'The machine name is: ' + self.asJson['name']
        # convert the json data to python data

    def test_local_title(self): # should set Machine.didPass to True on success
        pass

# This class is for API calls that require authorization
class CBTSession():
    # http://docs.python-requests.org/en/master/user/advanced/#session-objects
    def __init__(self):
        # Accessing your testing history requires authorization, so the following allows us to authrorize on the server:
        self.api_session = requests.Session()
        self.api_session.auth = (username, authkey)
        response = self.api_session.get(test_history_endpoint)
        # assign responses
        # self.test_history = json.loads(response.text) # ALL test history, then load into python

        # NOTE: the purpose of this is to get the 3 most recent tests that happened today
        most_recent_tests = self.api_session.get(test_history_endpoint + '?start_date=2018-02-22&num=1').text # ?= passing parameters
        self.most_recent_tests = json.loads(most_recent_tests) # for pretty printing, use: json.dumps(cbt.most_recent_tests, indent=4, sort_keys=True)
        self.most_recent_test_id = cbt.most_recent_tests['selenium'][0]['selenium_test_id'] # this gets the test id
def get_all(): # gets all browsers available
    out_array = []
    for i in range(len(all_browsers_available)):
        out_array.append (all_browsers_available[i]['name'])
    return out_array


# MARK: - Machine testing
create machine instances
windows_machine = Machine('Windows 10')
mac_machine = Machine('Mac OSX 10.9')
mobile_machine = Machine('Android Galaxy Note 3 / 4.4')
-------------------------------------------------------------
print get_all()

# print machines json value (if these print, it means the machines have been successfully retrieved & you can interact with them in python)
print windows_machine.caps
print json.dumps(mac_machine.asJson, indent=4, sort_keys=True)
print mobile_machine
#

# # MARK: - CBT test
# cbt = CBTSession()
# # pretty print the most recent tests
# # most_recent = json.dumps(cbt.most_recent_tests, indent=4, sort_keys=True)
# most_recent_test_id = cbt.most_recent_tests['selenium'][0]['selenium_test_id']
# print most_recent
