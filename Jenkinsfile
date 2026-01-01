pipeline {
    agent any

    environment {
        IMAGE_NAME = "lms-app"
        // Force the build to ignore old, empty cached layers
        BUILD_ARGS = "--no-cache"
    }

    stages {
        stage('Cleanup & Diagnostic') {
            steps {
                // Remove old files to ensure a clean start
                deleteDir()
                checkout scm
                
                script {
                    echo "--- Current Directory Structure ---"
                    sh 'ls -R'
                    
                    // Verify if manage.py exists anywhere in the pulled code
                    def check = sh(script: 'find . -name manage.py', returnStdout: true).trim()
                    if (check == "") {
                        error "FATAL ERROR: manage.py not found in Git repository. Please ensure you have pushed your Django project code."
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    // Find the directory containing manage.py (handles subfolders)
                    def managePyPath = sh(script: 'find . -name manage.py | head -n 1', returnStdout: true).trim()
                    def projectDir = sh(script: "dirname ${managePyPath}", returnStdout: true).trim()
                    
                    echo "Project located in: ${projectDir}. Starting Docker build..."

                    dir(projectDir) {
                        // Build the image from the folder where manage.py lives
                        sh "docker build ${env.BUILD_ARGS} -t ${env.IMAGE_NAME}:latest ."
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Use the image we just built to run Django tests
                // We use -w /code to ensure we are in the right spot inside the container
                sh "docker run --rm ${env.IMAGE_NAME}:latest python manage.py test"
            }
        }
        
        stage('Deploy (Optional)') {
            steps {
                echo "Tests passed! You can now deploy your container."
                // Example: sh "docker run -d -p 8000:8000 --name lms-container ${env.IMAGE_NAME}:latest"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        failure {
            echo "Pipeline failed. Check the logs above for file path errors."
        }
    }
}
