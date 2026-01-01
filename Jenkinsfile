pipeline {
    agent any // Runs directly on the Jenkins VM shell

    stages {
        stage('Install Dependencies') {
            steps {
                // Use pip3 instead of pip
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Use python3 instead of python
                sh 'python3 manage.py test'
            }
        }
        stage('Docker Build') {
            steps {
                // This still works because Docker is installed on the VM
                sh 'docker build -t lms-site:latest .'
            }
        }
    }
}