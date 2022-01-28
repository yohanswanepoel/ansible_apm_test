import os
import sys
import platform

os.system("ansible-galaxy collection install community.kubernetes")

os.system("ansible-playbook elastic_stack/stop-stack.yaml")

os.system("ansible-playbook elastic_stack/setup-apm.yaml")

os.system("ansible-playbook elastic_stack/start-stack.yaml")

# export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:8200"
os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = 'http://localhost:8200'

os.environ['OTEL_SERVICE_NAME'] = 'Ansible Test Service'


os.system("python smoke_test.py")

