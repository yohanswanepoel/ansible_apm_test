import os
import sys
import platform

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = ''

os.system("ansible-playbook elastic_stack/stop-stack.yaml")

print("Stopping Kubernetes and Removing Profile")
os.system("minikube delete --profile=apmtest")

print("Verify Stack is down")
os.system("ps -ef | grep -i elastic | grep -i java")
os.system("ps -ef | grep -i kibana | grep -i java")
os.system("ps -ef | grep -i apm-server | grep -i java")