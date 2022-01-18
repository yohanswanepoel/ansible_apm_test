import sys
import urllib.request
import time


print(len(sys.argv))
print("Argument List: ", str(sys.argv), str(sys.argv[1]))
url = str(sys.argv[1])
if len(sys.argv) == 2:
    for x in range(1000):
        #contents = urllib.request.urlopen("http://example.com/foo/bar").read()
        urllib.request.urlopen(url)
        if x // 5 == 0:
            urllib.request.urlopen(url+"/owners/find")
            urllib.request.urlopen(url+"/vets.html")
        try:
            if x // 10 == 0:
                urllib.request.urlopen(url+"/oups")
        except urllib.error.HTTPError as exception:
            pass
        time.sleep(1)
        print(x)
else:
    print("You need to specify the service URL")