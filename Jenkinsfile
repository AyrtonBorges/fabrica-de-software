pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ayrtonborges/html .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker container run -p 8080:80 ayrtonborges/html'
            }
        }
    }
}