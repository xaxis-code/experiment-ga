pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 .'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
                sh '/home/devops/.local/bin/pytest --junitxml=output.xml'
                archiveArtifacts artifacts: 'output.xml', fingerprint: true
            }
        }
        stage('Build') {
            when {
                branch 'master|dev|test|demo|release|prod|main'
            }
            environment {
                IMAGE_NAME = "experiment-ga"
                AWS_ACCOUNT_ID = "952256534162"
                AWS_REGION = "us-east-1"
                REPO_NAME = "952256534162.dkr.ecr.us-east-1.amazonaws.com"
            }
            steps {
                withCredentials([string(credentialsId: 'aws-access-key', variable: 'ACCESS_KEY'), string(credentialsId: 'aws-secret-key', variable: 'SECRET_KEY')]) {
                    sh '''
                        aws configure set aws_access_key_id $ACCESS_KEY
                        aws configure set aws_secret_access_key $SECRET_KEY
                        aws configure set region $AWS_REGION
                    '''
                    sh '''
                        ECR_PASSWORD=$(aws ecr get-login-password)
                        echo $ECR_PASSWORD | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                    '''
                    sh 'echo "Image name is ${IMAGE_NAME}"'
                    sh 'docker build --tag $REPO_NAME/$IMAGE_NAME:cci .'
                    sh 'docker push $REPO_NAME/$IMAGE_NAME:cci'
                }
            }
        }
    }
}
