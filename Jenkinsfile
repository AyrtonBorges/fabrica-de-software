pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                copy
                sh 'docker container run -p 8000:8000 django:latest python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker container run -p 8000:8000 django:latest'
            }
        }
    }
}
