import os
import sys
import platform
from config import OTEL_EXPORTER_OTLP_ENDPOINT

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = OTEL_EXPORTER_OTLP_ENDPOINT

os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Account Team',manual_effort=120\"; export OTEL_SERVICE_NAME='Account Test Environment'; ansible-playbook kube/test-kube-python-orchestration.yaml ; unset OTEL_SERVICE_NAME")