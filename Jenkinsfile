pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t wahlul/myapp .'
                    // Push the image to Docker Hub
                    sh 'docker push wahlul/myapp'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy using Helm
                    sh 'helm upgrade --install myapp ./myapp --namespace myapp-namespace --create-namespace'
                }
            }
        }
    }
}

