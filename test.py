import os
import sys
import platform


for x in range(10):
    os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Team A'\"; export OTEL_SERVICE_NAME='Good Test'; ansible-playbook test-apm.yaml ; unset OTEL_SERVICE_NAME")

os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Team A'\"; export OTEL_SERVICE_NAME='Good Test'; ansible-playbook test-apm-with-error.yaml ; unset OTEL_SERVICE_NAME")