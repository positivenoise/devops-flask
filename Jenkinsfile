node {

    checkout scm

    env.DOCKER_API_VERSION="1.23"
    
    sh "git rev-parse --short HEAD > commit-id"

    stage "Build"
    
        sh "docker build -t 127.0.0.1:30400/devops-flask:latest app"
        sh "docker build -t 127.0.0.1:30400/mysql-db:latest mysql-db"
        sh "docker build -t 127.0.0.1:30400/phpmyadmin:latest phpmyadmin"

    stage "Push"

        sh "docker push 127.0.0.1:30400/devops-flask:latest"
        sh "docker push 127.0.0.1:30400/mysql-db:latest"
        sh "docker push 127.0.0.1:30400/phpmyadmin:latest"


    stage "Deploy"

        sh "kubectl apply -f manifests/devops-flask-manual-deployment.yaml"
        sh "kubectl apply -f manifests/mysql-db-manual-deployment.yaml"
        sh "kubectl apply -f manifests/phpmyadmin-manual-deployment.yaml"
}