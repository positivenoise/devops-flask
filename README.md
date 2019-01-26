#Devops-Flask

Deployment templates for Flask site

Run from within app folder with "python app.py"

##Docker instructions

Build from within app directory with "docker build -t 'name' ."

Run docker once built with "docker run -p 5000:5000 -P -d name"

Run docker compose from base directory with "docker-compose up"

##Minkube instructions

Start minikube with "minikube start --vm-driver=hyperv"
If errors try resetting with "minikube delete"

Bring docker env into minikube with "minikube docker-env | Invoke-Expression"
Build your docker image with docker build - ensure version is not latest

##Kubectl

Create deployment with:

kubectl run flask-test --image=flask-docker:v0 --port=5000
kubectl expose deployment flask-test --type="LoadBalancer"
minikube service flask-test --url