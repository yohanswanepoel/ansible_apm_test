# TLDR: Testing APM with Ansible

Dependencies:
* installed ElasticSearch, Kibana and APM
* installed minikube
* installed kubectl
* installed ansible in a virtual env

This project:
* Starts Elastic infrastructure
* Configure ansible and python
* run apm ansible test playbooks
* sets up minikube and a java app with apm enabled

```bash
python setup.py
python test-kube.py
python tear-down.py
```