# Details of the custom credential required in tower

## Credential Type configuration service details
```yaml
fields:
  - id: apmurl
    type: string
    label: APM Url
```
 
Credential: Injector configuration for the Playbook/Template
```yaml
env:
  OTEL_EXPORTER_OTLP_ENDPOINT: '{{apmurl}}'
```

## Team details
```yaml
fields:
  - id: apmservice
    type: string
    label: APM Service
  - id: team
    type: string
    label: Team Name
  - id: effort
    type: string
    label: Effort in minutes
```

Credential: Injector configuration for the Playbook/Template
```yaml
env:
  OTEL_SERVICE_NAME: '{{apmservice}}'
  OTEL_RESOURCE_ATTRIBUTES: 'team={{team}},manual_effort={{effort}}'
```