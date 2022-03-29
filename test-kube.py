import os
import sys
import platform
from config import OTEL_EXPORTER_OTLP_ENDPOINT

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = OTEL_EXPORTER_OTLP_ENDPOINT

os.system("export OTEL_RESOURCE_ATTRIBUTES=\"team='Platform',manual_effort=120\"; export OTEL_SERVICE_NAME='Petclinic Test Environment'; ansible-playbook kube/test-kube-orchestration.yaml ; unset OTEL_SERVICE_NAME")