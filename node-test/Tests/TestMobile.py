import unittest
from selenium import webdriver
import requests
import sys
import json
from json import JSONEncoder
import urllib2

username = "jbhtcher@memphis.edu"
authkey  = "u63c4853726aabbb"

class SeleniumTestMobile(unittest.TestCase):
    def setUp(self):

        self.api_session = requests.Session()
        self.api_session.auth = (username, authkey)
        self.test_result = None

        caps = {}
        # these parameters are on a test by test basis. You can change the name and it will reflect in your CBT history
        caps['name'] = 'Selenium Test Example Mobile (Android)'
        caps['build'] = '1.0'

        # NOTE: these are different than Windows, so they test different machines.
        caps['browserName'] = 'Chrome'
        caps['deviceName'] = 'Nexus 6P'
        caps['platformVersion'] = '7.0'
        caps['platformName'] = 'Android'
        caps['deviceOrientation'] = 'portrait'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" %(username, authkey) # include username and authkey in url
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):
        def set_remote_test_result(): # this function should be called after having a successful test result
            # endpoints
            cbt_set_endpoint = 'https://crossbrowsertesting.com/api/v3/selenium/'
            test_history_endpoint = "https://crossbrowsertesting.com/api/v3/selenium?format=json"

            # start an API session to get information that is private to your account
            self.api_session = requests.Session()
            self.api_session.auth = (username, authkey)
            response = self.api_session.get(test_history_endpoint)

            # get today's date for finding API calls that happened today
            import datetime
            now = datetime.datetime.now()

            # get the  most recent test
            most_recent_test = self.api_session.get(test_history_endpoint + '?start_date=%s-%s-%s&num=1' % (now.year, now.month, now.day)).text

            # take the most recent test, and access its id to refer to it
            most_recent_test = json.loads(most_recent_test)

            most_recent_test_id = most_recent_test['selenium'][0]['selenium_test_id']

            # construct the endpoint with the id
            cbt_set_endpoint = cbt_set_endpoint + str(most_recent_test_id)

            # make the payload
            payload = {'selenum_test_id': most_recent_test_id,'action': 'set_score', 'score': 'pass'} # NOTE: from https://stackoverflow.com/questions/111945/is-there-any-way-to-do-http-put-in-python

            # profit
            response_from_post = self.api_session.put(cbt_set_endpoint, data=payload)

        try:
            self.driver.get('http://local:8000') # this is where we setup our local test server. NOTE: 'local' is used instead of localhost. This is a technical detail that can get kind of confusing, so just remember to use local when you are testing your website behind your firewall.
            self.assertEqual("Hello world!", self.driver.title)
            self.test_result = 'pass'
            self.driver.quit()
        except:
             print("Unexpected error:", sys.exc_info()[0])
             raise


if __name__ == '__main__':
    unittest.main()
