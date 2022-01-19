import os
import sys
import platform

def run_test(team, x):
    os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='{}',manual_effort=30\"; export OTEL_SERVICE_NAME='Demo Test'; ansible-playbook test-apm.yaml ; unset OTEL_SERVICE_NAME".format(team))
    if x // 5 == 0:
        os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='{}',manual_effort=25\"; export OTEL_SERVICE_NAME='Demo Test'; ansible-playbook test-apm-with-error.yaml ; unset OTEL_SERVICE_NAME".format(team))

for x in range(60):
    run_test("Team A", x)
    run_test("Team B", x)
    run_test("Team C", x)
    run_test("Team D", x)