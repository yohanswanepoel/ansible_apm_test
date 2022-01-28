import os
import sys
import platform

os.system("ansible-playbook elastic_stack/stop-stack.yaml")

os.system("minikube delete --profile=apmtest")

os.system("ps -ef | grep -i elastic | grep -i java")
os.system("ps -ef | grep -i kibana | grep -i java")
os.system("ps -ef | grep -i apm-server | grep -i java")