pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // This pulls your code from Git into the Jenkins workspace
                checkout scm
            }
        }
        stage('Docker Build') {
            steps {
                // Now that files are present, build the image
                sh 'docker build --no-cache -t lms-app:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                // This will now work because manage.py was copied into the image
                sh '''
                    LOCATION=$(docker run --rm lms-app:latest find /code -name "manage.py" | head -n 1)
                    DIR_PATH=$(dirname $LOCATION)
                    docker run --rm -w $DIR_PATH lms-app:latest python manage.py test
                '''
            }
        }
    }
}
