pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker image build -t ayrtonborges/django:v1 .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker container run -p 8000:8000 ayrtonborges/django:v1 python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker container run -p 8000:8000 ayrtonborges/django:v1'
            }
        }
    }
}
