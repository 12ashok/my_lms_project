pipeline {
    agent any

    stages {
        stage('Checkout & Sync') {
            steps {
                // REMOVED deleteDir() to protect your manually created manage.py
                checkout scm
                
                script {
                    // Ensure Jenkins user owns the files you created as 'ubuntu'
                    sh 'sudo chown -R jenkins:jenkins .'
                    sh 'ls -la' // Diagnostic: Check if manage.py is visible in logs
                }
            }
        }

        stage('Locate and Build') {
            steps {
                script {
                    def managePyPath = sh(script: 'find . -name manage.py | head -n 1', returnStdout: true).trim()
                    
                    if (managePyPath == "") {
                        error "FATAL: manage.py still missing. Run 'django-admin startproject core .' on the VM terminal!"
                    }

                    def projectDir = sh(script: "dirname ${managePyPath}", returnStdout: true).trim()
                    echo "Found project at: ${projectDir}"

                    dir(projectDir) {
                        sh "docker build --no-cache -t lms-app:latest ."
                    }
                }
            }
        }

        stage('Test') {
            steps {
                sh "docker run --rm lms-app:latest python manage.py test"
            }
        }
    }
}
