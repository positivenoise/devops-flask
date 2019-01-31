# Devops-Flask

Deployment templates for Flask site

Includes flask front end, mysql database with phpmyadmin administration in seperate containers.

Instructions for k8s deployment are incomplete

## Docker instructions

From base directory:

Build images with:
```
docker build -t devops-flask:latest app
docker build -t mysql-db:latest mysql-db
docker build -t phpmyadmin:latest phpmyadmin
```
Run with
```
docker-compose up
```
## Minkube instructions

Start minikube with `minikube start --vm-driver=hyperv`
Enable add-ons with `minikube addons enable heapster; minikube addons enable ingress`
Setup cluster registry with `kubectl apply -f manifests/registry.yaml`
Wait for deployment to finish with `kubectl rollout status deployments/registry`
If errors try resetting with `minikube delete`

Build the custom images with:
```
docker build -t 127.0.0.1:30400/devops-flask:latest app
docker build -t 127.0.0.1:30400/mysql-db:latest mysql-db
docker build -t 127.0.0.1:30400/phpmyadmin:latest phpmyadmin
```
Find minikube IP with `minikube ip` and put in REG_IP address

Run socat proxy with:
```
docker build -t socat-registry utilities/socat
docker stop socat-registry; docker rm socat-registry; 
docker run -d -e "REG_IP=10.0.1.62" -e "REG_PORT=30400" --name socat-registry -p 30400:5000 socat-registry
```
Push image to repositry with:
```
docker push 127.0.0.1:30400/devops-flask:latest
docker push 127.0.0.1:30400/mysql-db:latest
docker push 127.0.0.1:30400/phpmyadmin:latest
```

Check the registry: `minikube service registry-ui​​`

Deploy to Kubernetes with ​​`kubectl apply -f manifests/manual-deployment.yaml​​`

Check the deployment with `minikube service devops-flask​​`

## OLD


Bring docker env into minikube with `minikube docker-env | Invoke-Expression`

Reset env back with `docker-machine env --unset | Invoke-Expression`

OLD Deploy to Kubernetes with:
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
