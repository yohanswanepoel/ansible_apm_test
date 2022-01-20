import sys
import urllib.request
import time
import random


print(len(sys.argv))
print("Argument List: ", str(sys.argv), str(sys.argv[1]))
url = str(sys.argv[1])
if len(sys.argv) == 2:
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
        print(x)
else:
    print("You need to specify the service URL")