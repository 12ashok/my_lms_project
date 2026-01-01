pipeline {
    agent any

    stages {
        stage('Checkout & Clean') {
            steps {
                // Clear old data and pull fresh code from Git
                deleteDir()
                checkout scm
            }
        }

        stage('Locate and Build') {
            steps {
                script {
                    // 1. Find the path to manage.py
                    def managePyPath = sh(script: 'find . -name manage.py | head -n 1', returnStdout: true).trim()
                    
                    if (managePyPath == "") {
                        error "FATAL: manage.py not found in the repository! Check your Git files."
                    }

                    // 2. Get the directory containing manage.py
                    def projectDir = sh(script: "dirname ${managePyPath}", returnStdout: true).trim()
                    echo "Found manage.py at: ${managePyPath}"
                    echo "Switching build context to: ${projectDir}"

                    // 3. Build the image FROM that directory
                    dir(projectDir) {
                        sh "docker build --no-cache -t lms-app:latest ."
                    }
                }
            }
        }

        stage('Test') {
            steps {
                // Run tests using the image we just built
                sh "docker run --rm lms-app:latest python manage.py test"
            }
        }
    }
}
