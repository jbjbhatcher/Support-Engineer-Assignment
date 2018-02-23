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
        # these parameters are on a test by test basis. You can change the name and it will reflect in your CBT history
        caps['name'] = 'Selenium Test Example Mobile (Android)'
        caps['build'] = '1.0'

        # these parameters specify which machine you want to run the test on
        caps['browserName'] = 'Chrome'
        caps['deviceName'] = 'Nexus 6P'
        caps['platformVersion'] = '7.0'
        caps['platformName'] = 'Android'
        caps['deviceOrientation'] = 'portrait'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" %(self.username,self.authkey) # include username and authkey in url
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


            # get the  most recent test
            most_recent_test = self.api_session.get(test_history_endpoint + '?start_date=2018-02-22&num=1').text
                # start_date - the date the test was started
                # num - the number of API results to get

            # take the most recent test, and access its id to refer to it
            most_recent_test = json.loads(most_recent_test)

            most_recent_test_id = most_recent_test['selenium'][0]['selenium_test_id']


            # construct the endpoint with the id
            cbt_set_endpoint = cbt_set_endpoint + str(most_recent_test_id)

            # make the payload
            payload = {'selenum_test_id': most_recent_test_id,'action': 'set_score', 'score': 'pass'} # NOTE: from https://stackoverflow.com/questions/111945/is-there-any-way-to-do-http-put-in-python

            # profit
            response_from_post = self.api_session.put(cbt_set_endpoint, data=payload)
            print response_from_post
            print 'HERE IS THE ID OF THE SESSION BEING SET: ' + str(most_recent_test_id)

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
