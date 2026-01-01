pipeline {
    agent any

    environment {
        IMAGE_NAME = "lms-app"
        CONTAINER_NAME = "lms-container"
    }

    stages {
        stage('Checkout & Permissions') {
            steps {
                // Pulls code from Git
                checkout scm
                
                script {
                    // Fix permissions in case manual files were created as 'ubuntu'
                    // Requires "jenkins ALL=(ALL) NOPASSWD: ALL" in /etc/sudoers
                    sh 'sudo chown -R jenkins:jenkins .'
                }
            }
        }

        stage('Build Image') {
            steps {
                script {
                    // Find manage.py location dynamically
                    def managePyPath = sh(script: 'find . -name manage.py | head -n 1', returnStdout: true).trim()
                    
                    if (managePyPath == "") {
                        error "FATAL: manage.py not found. Ensure it is in your Git repo or VM workspace."
                    }

                    def projectDir = sh(script: "dirname ${managePyPath}", returnStdout: true).trim()
                    
                    dir(projectDir) {
                        // Build the Docker image
                        sh "docker build --no-cache -t ${IMAGE_NAME}:latest ."
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                // This runs the container, executes tests, then DELETES the container (--rm)
                sh "docker run --rm ${IMAGE_NAME}:latest python manage.py test"
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // 1. Stop and remove the old container if it is already running
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    // 2. Start the new container in Detached mode (-d) to keep it running
                    // Maps port 8000 of the VM to port 8000 of the container
                    sh "docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
                    
                    echo "Application is running at http://your-ip:8000"
                }
            }
        }
    }

    post {
        success {
            echo "Deployment Successful!"
        }
        failure {
            echo "Pipeline failed. Check logs for manage.py location or Permission issues."
        }
    }
}
