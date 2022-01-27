import os
import sys
import platform

os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Automation Team',manual_effort=120\"; export OTEL_SERVICE_NAME='Automation Service'; ansible-playbook setup-awx.yaml ; unset OTEL_SERVICE_NAME")

# Need to check that operator is running first
os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Automation Team',manual_effort=120\"; export OTEL_SERVICE_NAME='Automation Service'; ansible-playbook setup-awx-access.yaml ; unset OTEL_SERVICE_NAME")

# Build the Image
os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Automation Team',manual_effort=120\"; export OTEL_SERVICE_NAME='Automation Service'; ansible-playbook setup-awx-build-custom-ee.yaml ; unset OTEL_SERVICE_NAME")