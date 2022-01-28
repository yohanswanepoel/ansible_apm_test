import os
import sys
import platform

def run_test(team, x):
    os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='{}',manual_effort=30\"; export OTEL_SERVICE_NAME='Demo Test'; ansible-playbook elastic_stack/test-apm.yaml ; unset OTEL_SERVICE_NAME".format(team))
    os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='{}',manual_effort=25\"; export OTEL_SERVICE_NAME='Demo Test'; ansible-playbook elastic_stack/test-apm-with-error.yaml ; unset OTEL_SERVICE_NAME".format(team))

for x in range(1):
    run_test("Test A", x)
    run_test("Test B", x)