
all: build deploy expose ui

build:
	@echo "building mage"
	minikube --profile apmtest image build -t skaffold-demo .

deploy:
	@echo "deploy service"
	kubectl apply -f ../app-local/k8s-app.yaml -n development

expose:
	@echo "expose service"
	kubectl apply -f ../app-local/k8s-service.yaml -n development

ui:
	@echo "open browser"
	minikube --profile=apmtest service skaffold-demo -n development