import os
import sys
import platform
import time

for x in range(10):
    os.system("python test-kube.py")
    time.sleep(120)
    os.system("python test-kube-python.py")
    time.sleep(120)
