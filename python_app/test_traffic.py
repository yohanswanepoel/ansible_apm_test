import sys
import urllib.request
import time
import os


url = os.getenv('TEST_URL','http://192.168.64.31:30002')

class TestClass:
    def test_base_url(self):
        assert 200 == urllib.request.urlopen(url).getcode()

    def test_about_url(self):
        assert 200 == urllib.request.urlopen(url+"/about/").getcode()
    
    def test_signup_url(self):
        assert 200 == urllib.request.urlopen(url+"/accounts/signup/").getcode()

    def test_error_url(self):
        try:
            urllib.request.urlopen(url+"/error).getcode()
        except urllib.error.HTTPError as exception:
            assert 404 == exception.code
    
    def load_test(self):

        for x in range(1000):
        #contents = urllib.request.urlopen("http://example.com/foo/bar").read()
        urllib.request.urlopen(url)
        if x // random.randrange(3,7) == 0:
            urllib.request.urlopen(url+"/about/")
            urllib.request.urlopen(url+"/accounts/signup/")
        try:
            if x // random.randrange(5,10) == 0:
                urllib.request.urlopen(url+"/error")
        except urllib.error.HTTPError as exception:
            pass
        # time.sleep(1)
        assert True
