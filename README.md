# Devops-Flask

Deployment templates for Flask site

Includes flask front end, mysql database with phpmyadmin administration in seperate containers.

## Docker instructions

From base directory:

Build images with:
```
docker build -t devops-flask app
docker build -t mysql-db mysql-db
```
Run with
```
docker-compose up
```
## Minkube instructions

Start minikube with `minikube start --vm-driver=hyperv`
If errors try resetting with `minikube delete`

Bring docker env into minikube with `minikube docker-env | Invoke-Expression`
Reset env back with `docker-machine env --unset | Invoke-Expression`

Build your docker image with docker build - ensure version is not latest

## Kubectl
- These deployment instructions are out of date

Create deployment with:

```
kubectl run flask-test --image=flask-docker:v0 --port=5000
kubectl expose deployment flask-test --type="LoadBalancer"
minikube service flask-test --url
```