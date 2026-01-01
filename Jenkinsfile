pipeline {
    agent any 

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Ensure your code isn't broken before building
                sh 'python manage.py test'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Creates a versioned image of your site
                sh 'docker build -t my-lms-site:latest .'
            }
        }
        stage('Deploy') {
            steps {
                // Stop the old version and start the new one
                sh 'docker-compose up -d'
            }
        }
    }
}