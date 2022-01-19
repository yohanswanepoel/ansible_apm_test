import os
import sys
import platform

os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Plaform',manual_effort=60\"; export OTEL_SERVICE_NAME='My Service App'; ansible-playbook test-kube-orchestration.yaml ; unset OTEL_SERVICE_NAME")