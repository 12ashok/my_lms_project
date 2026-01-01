pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }
    
    stages {
        stage('Install Dependencies') {
            steps {
                // Now 'pip' will be found because it exists inside the python image
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }
        // ... rest of your build stages
    }
}