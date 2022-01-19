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
## TODO
* capture metrics e.g. business unit - manual effort ect.
* develop insightful dashbboards
