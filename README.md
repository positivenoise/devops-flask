# Devops-Flask

Deployment templates for Flask site

Includes flask front end, mysql database with phpmyadmin administration in seperate containers.

## Docker instructions

From base directory:

Build images with:
```
docker build -t devops-flask:v0 app
docker build -t mysql-db:v0 mysql-db
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

Build the custom images with:
```
docker build -t devops-flask:v0 app
docker build -t mysql-db:v0 mysql-db
```

Deploy to Kubernetes with:
```
kubectl run db --image=mysql-db:v0 --port=3306
kubectl expose deployment db --type="LoadBalancer"
kubectl run phpmyadmin --image=phpmyadmin/phpmyadmin --port=80
kubectl expose deployment phpmyadmin --type="LoadBalancer"
kubectl run app --image=devops-flask:v0 --port=5000
kubectl expose deployment app --type="LoadBalancer"
```

View endpoint urls:
```
minikube service app --url
minikube service phpmyadmin --url
```
See everything with `minikube dashboard`
