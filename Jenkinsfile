pipeline {
    agent any

    environment {
        // Replace with your Docker Hub username and image name
        DOCKER_IMAGE = "sanjusci/test_docker_jenkins"
        DOCKER_CRED_ID = "docker-hub-credentials" // The ID from Jenkins Credentials
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/sanjusci/test_docker_jenkins.git'
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker ps'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the repo
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    // Push the image to Docker Hub using stored credentials
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CRED_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                        sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                // Stop and remove old container, then run new one
                sh "docker stop flask-app-container || true"
                sh "docker rm flask-app-container || true"
                sh "docker run -d --name flask-app-container -p 8080:5001 ${DOCKER_IMAGE}:latest"
            }
        }
    }
}
