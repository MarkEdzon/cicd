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
                checkout([$class: 'GitSCM', 
                    branches: [[name: "*/${env.GIT_BRANCH}"]], 
                    userRemoteConfigs: [[url: "${env.GIT_REPO_URL}", credentialsId: "${env.GIT_CREDENTIALS_ID}"]]
                ])
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                sudo rsync -av --delete --exclude='venv/' --exclude='.git/' --exclude='staging/' ./ /var/www/html/
                sudo chown -R www-data:www-data /var/www/html/
                '''
            }
        }
        stage('Check PHP') {
            steps {
                sh 'php -v'
            }
        }
        stage('Run All PHP Files') {
            steps {
                sh '''
                echo "Executing all PHP files in workspace..."
                find . -name "*.php" -type f | while read file; do
                    echo "----------------------"
                    echo "Running $file"
                    php "$file"
                    echo "----------------------"
                done
                '''
            }
        }
    }
    post {
        always {
            echo "Pipeline finished."
        }
    }
}
