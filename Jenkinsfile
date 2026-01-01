pipeline {
    agent any

    environment {
        IMAGE_NAME = "lms-app"
        CONTAINER_NAME = "lms-container"
    }

    stages {
        stage('Cleanup & Checkout') {
            steps {
                deleteDir()
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    def managePyPath = sh(script: 'find . -name manage.py | head -n 1', returnStdout: true).trim()
                    if (managePyPath == "") {
                        error "FATAL: manage.py not found in Git."
                    }
                    def projectDir = sh(script: "dirname ${managePyPath}", returnStdout: true).trim()
                    
                    dir(projectDir) {
                        sh "docker build --no-cache -t ${IMAGE_NAME}:latest ."
                    }
                }
            }
        }

        stage('Deploy & Database Update') {
            steps {
                script {
                    // 1. Stop and remove the old container
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    // 2. Start the new container
                    sh "docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"

                    // 3. WAIT for the container process to initialize
                    echo "Waiting for container to initialize..."
                    sleep 5

                    // 4. Run Migrations inside the running container
                    echo "Running Database Migrations..."
                    sh "docker exec ${CONTAINER_NAME} python manage.py makemigrations"
                    sh "docker exec ${CONTAINER_NAME} python manage.py migrate"
                    
                    echo "Deployment and Database Migration Complete!"
                }
            }
        }
    }

    post {
        success {
            echo "Successfully deployed to http://98.92.195.182:8000"
        }
    }
}
