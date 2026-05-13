pipeline {
    agent any
    stages {
        stage('Source Control') {
            steps {
                git 'https://github.com/frasolis-design/actividad-api-lol.git'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t api-lol-solis:latest .'
            }
        }
        stage('Quality Test') {
            steps {
                sh 'docker run --rm api-lol-solis:latest'
            }
        }
    }
}