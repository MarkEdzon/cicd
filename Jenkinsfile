pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/MarkEdzon/cicd.git'
        GIT_CREDENTIALS_ID = 'github-pat2'
        GIT_BRANCH = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${env.GIT_BRANCH}",
                    credentialsId: "${env.GIT_CREDENTIALS_ID}",
                    url: "${env.GIT_REPO_URL}"
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start Apache') {
    steps {
        sh 'echo "Apache already running"'
    }
}

        stage('Test') {
            steps {
                sh '''
                php -l index.php
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                sudo rsync -av --delete \
                --exclude='venv/' \
                --exclude='.git/' \
                ./ /var/www/html/

                sudo chown -R www-data:www-data /var/www/html/
                '''
            }
        }
    }
}
