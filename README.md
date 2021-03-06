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

Start minikube with `minikube start --memory 8000 --cpus 2 --vm-driver=hyperv`
Enable add-ons with `minikube addons enable heapster; minikube addons enable ingress`
Setup cluster registry with `kubectl apply -f manifests/registry.yaml`
Wait for deployment to finish with `kubectl rollout status deployments/registry`

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

Deploy to Kubernetes with: 
```
kubectl apply -f manifests/devops-flask-manual-deployment.yaml
kubectl apply -f manifests/mysql-db-manual-deployment.yaml
kubectl apply -f manifests/phpmyadmin-manual-deployment.yaml
```
Check the deployment with `minikube service devops-flask​​`
Check phpmyadmin with `minikube service phpmyadmin​​` and root:my-secret-password

See everything with `minikube dashboard`
If errors try resetting with `minikube delete`

## Jenkins

```
docker build -t 127.0.0.1:30400/jenkins:latest jenkins
docker build -t socat-registry utilities/socat
docker stop socat-registry; docker rm socat-registry; 
docker run -d -e "REG_IP=10.0.1.63" -e "REG_PORT=30400" --name socat-registry -p 30400:5000 socat-registry
docker push 127.0.0.1:30400/jenkins:latest
kubectl apply -f manifests/jenkins.yaml
kubectl rollout status jenkins
minikube service jenkins
```

RESULT = kubectl get pods --selector=app=jenkins --output=jsonpath={.items..metadata.name}
Display Jenkins admin password kubectl exec -it RESULT cat /var/jenkins_home/secrets/initialAdminPassword
### Setup Credentials

Credentials -> Global credentials (unrestricted) -> Add Credentials

ID is devops-flask_kubeconfig - Kubeconfig enter directly and copy the contents of /var/jenkins_home/.kube/config but ensure the server address is correct.

### Setup Pipeline

* Select Install suggested plugins
* Create an admin user
* Create a new item and select Pipeline
* Definition is Pipeline script from SCM
* https://github.com/positivenoise/devops-flask
* Save and run