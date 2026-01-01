pipeline {
    agent any

    environment {
        IMAGE_NAME = "lms-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls code from your Git repository
                checkout scm
            }
        }

        stage('Auto-Locate and Build') {
            steps {
                script {
                    // 1. Find the path to the directory containing manage.py
                    // This handles cases where your code is in a subfolder
                    def managePyPath = sh(script: 'find . -name manage.py | head -n 1', returnStdout: true).trim()
                    
                    if (managePyPath == "") {
                        error "Could not find manage.py in the workspace. Check your Git repository."
                    }

                    def projectDir = sh(script: "dirname ${managePyPath}", returnStdout: true).trim()
                    
                    echo "Found project in directory: ${projectDir}"

                    // 2. Build the Docker image from that specific directory
                    dir(projectDir) {
                        sh "docker build --no-cache -t ${IMAGE_NAME}:latest ."
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run the Django tests inside the container
                sh "docker run --rm ${IMAGE_NAME}:latest python manage.py test"
            }
        }

        stage('Cleanup') {
            steps {
                // Optional: Remove dangling images to save disk space on your single VM
                sh 'docker image prune -f'
            }
        }
    }
}
