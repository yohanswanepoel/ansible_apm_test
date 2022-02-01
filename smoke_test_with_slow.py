import os
import sys
import platform

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = 'http://localhost:8200'

def run_test(team, x):
    os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='{}',manual_effort=25\"; export OTEL_SERVICE_NAME='Demo Test'; ansible-playbook smoke_tests/test-apm-with-slow.yaml ; unset OTEL_SERVICE_NAME".format(team))

for x in range(1):
    run_test("Test A", x)
    run_test("Test B", x)