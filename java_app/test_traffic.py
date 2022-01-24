import sys
import urllib.request
import time
import os


url = os.getenv('TEST_URL','http://192.168.64.31:30001')

class TestClass:
    def test_base_url(self):
        assert 200 == urllib.request.urlopen(url).getcode()

    def test_find_url(self):
        assert 200 == urllib.request.urlopen(url+"/owners/find").getcode()
    
    def test_vets_url(self):
        assert 200 == urllib.request.urlopen(url+"/vets.html").getcode()

    def test_error_url(self):
        try:
            urllib.request.urlopen(url+"/oups").getcode()
        except urllib.error.HTTPError as exception:
            assert 500 == exception.code
    
    def test_load_test(self):
        base_urls = 0
        secondary_urls = 0
        error_urls = 0
        for x in range(1000):
            #contents = urllib.request.urlopen("http://example.com/foo/bar").read()
            urllib.request.urlopen(url)
            if x // 5 == 0:
                urllib.request.urlopen(url+"/owners/find")
                urllib.request.urlopen(url+"/vets.html")
                secondary_urls = secondary_urls + 1
            try:
                if x // 10 == 0:
                    urllib.request.urlopen(url+"/oups")
            except urllib.error.HTTPError as exception:
                error_urls = error_urls + 1
            # time.sleep(1)
            base_urls = base_urls + 1
        print(base_urls + secondary_urls + error_urls)
        assert (base_urls + secondary_urls + error_urls) == 1015


