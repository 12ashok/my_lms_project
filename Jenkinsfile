pipeline {
    agent any

    environment {
        IMAGE_NAME = "lms-app"
        CONTAINER_NAME = "lms-container"
    }

    stages {
        stage('Cleanup & Checkout') {
            steps {
                // This clears the folder to prevent permission/lock issues
                deleteDir()
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    // Look for manage.py
                    def managePyPath = sh(script: 'find . -name manage.py | head -n 1', returnStdout: true).trim()
                    
                    if (managePyPath == "") {
                        error "FATAL: manage.py not found in Git. Did you push your changes?"
                    }

                    def projectDir = sh(script: "dirname ${managePyPath}", returnStdout: true).trim()
                    
                    dir(projectDir) {
                        sh "docker build --no-cache -t ${IMAGE_NAME}:latest ."
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    sh "docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
                }
            }
        }
    }
}
