# TLDR: Testing APM with Ansible

Dependencies:
* installed ElasticSearch, Kibana and APM, Mac instructions: https://github.com/elastic/homebrew-tap
* installed minikube
* installed kubectl
* installed ansible in a virtual env
```bash
python3 -m venv venv
source venv/bin/active 
```

This project:
* Starts Elastic infrastructure
* Configure ansible and python
* run apm ansible test playbooks
* sets up minikube and a java app with apm enabled

```bash
python setup.py
python test-kube.py
python test.py
python tear-down.py
```


Generate Traffic for Java App
```bash
python python3 java_app/generate_traffic.py http://[cluster ip]:30001
```

## Elastic Config
Apply this on your apm_transaction index and index template
```json

PUT apm-7.16.3-transaction-000001/_mapping
{
    "runtime": {
      "labels.manual_effort": {
        "type":"long"
      }
    }
}


PUT _template/apm-7.16.3-transaction?include_type_name
{
  "order": 2,
  "index_patterns": [
    "apm-7.16.3-transaction*"
  ],
  "settings": {
    "index": {
      "lifecycle": {
        "name": "apm-rollover-30-days",
        "rollover_alias": "apm-7.16.3-transaction"
      }
    }
  },
  "aliases": {},
  "mappings": {
    "_doc": {
      "_meta": {
        "beat": "apm",
        "version": "7.16.3"
      },
      "runtime": {
        "labels.manual_effort": {
          "type": "long"
        }
      },
      "dynamic_templates": [],
      "date_detection": false
    }
  }
}
```

## Import the dasboad
dashboard.ndjson

## TODO
* capture metrics e.g. business unit - manual effort ect.
* develop insightful dashbboards
