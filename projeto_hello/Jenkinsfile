pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ayrtonborges/my-django-app:latest .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker container run -d -p 8000:8000 ayrtonborges/my-django-app:latest'
            }
        }
    }
}