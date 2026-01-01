pipeline {
    agent any 

    stages {
        stage('Build Image') {
            steps {
                // Build the image first
                sh 'docker build -t lms-app:${BUILD_NUMBER} .'
                sh 'docker tag lms-app:${BUILD_NUMBER} lms-app:latest'
            }
        }
        stage('Run Tests inside Container') {
            steps {
                // Run tests inside the container we just built
                // --rm removes the container after the test finishes
                sh 'docker run --rm lms-app:latest python /code/manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                // Use Docker Compose to restart the site with the new image
                sh 'docker-compose up -d'
            }
        }
    }
}
