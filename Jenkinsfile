pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-django-app .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -p 8000:8000 my-django-app'
            }
        }
    }
}