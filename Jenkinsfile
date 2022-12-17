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
                sh 'docker run -p 8082:80 ayrtonborges/html'
            }
        }
    }
}