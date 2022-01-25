# TLDR: Testing APM with Ansible

Dependencies:
* installed ElasticSearch, Kibana and APM, Mac instructions: https://github.com/elastic/homebrew-tap
* installed minikube
* installed kubectl
* installed ansible in a virtual env
```bash
python3 -m venv venv
source venv/bin/active 

pip install -r requirements.txt

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
Apply this on your apm_transaction index and index template - **your indexes may have different name**
```json

PUT apm*/_mapping
{
    "runtime": {
      "labels.manual_effort": {
        "type":"long"
      }
    }
}


PUT _template/apm_label_override
{
  "index_patterns": ["apm*"],
  "order": 99, 
  "mappings": {
    "runtime": {
      "labels.manual_effort": {
        "type":"long"
      }
    }
  }
}

```

## Import the dashboad
dashboard.ndjson

## TODO
* capture metrics e.g. business unit - manual effort ect.
* develop insightful dashbboards
* kubernetes feature gates: --feature-gates=EphemeralContainers=true
