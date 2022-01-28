# TLDR: Testing APM with Ansible
AWX (Ansible Tower) requires a custom execution environment to use the Otel Plugin

To build that use the following steps as defined here: https://docs.ansible.com/automation-controller/latest/html/userguide/execution_environments.html and https://ansible-builder.readthedocs.io/en/latest/definition/

## requirements
* Podman or docker whichever you prefer
* ansible-builder (already in the requirements.txt file)
* pushing this to AWX...

This command generates a container file that you can build and then use as an execution environment
```bash
ansible-builder build
```

To build the container file and push it to the local registry
```bash
podman build -f context/Containerfile -t ansible-execution-env:latest context

podman tag localhost/ansible-execution-env:latest $(minikube -p apmtest ip):5000/ansible-execution-env:latest

podman push $(minikube -p apmtest ip):5000/ansible-execution-env:latest --tls-verify=false

podman image list $(minikube -p apmtest ip):5000
```

Altarnatively - use the minikube build command
```bash
minikube -p apmtest image build -t ansible-execution-env:latest . 
```

## Add image in AWX UI and test
* administration/execution environments
* add the result of echo $(minikube -p apmtest ip):5000/ansible-execution-env or localhost/ansible-execution-env:latest (if used minikube build)
* Launch job template with the new custom execution environment
* Add a project with ansible.cfg
* Add credentials for environment variables
* Custom credential
* Add credential to Job Template or use custom control environment
* https://github.com/yohanswanepoel/simple_ansible_test