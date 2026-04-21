pipeline{
  agent any

  environment {
    DOCKER_IMAGE = "sobine/mydjangoapp"
    DOCKER_TAG = "ci"
  }
  stages {
    
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        sh 'docker compose build'
      }
    }
    stage('Test') {
      steps {
        sh 'docker compose run --rm web python manage.py test'
      }
    }
    stage('Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]){
          sh '''
              echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
              docker tag $DOCKER_IMAGE:$DOCKER_TAG $DOCKER_IMAGE:latest
              docker push $DOCKER_IMAGE:$DOCKER_TAG
              docker push $DOCKER_IMAGE:latest

          '''
        }
        
      }
    }
    stage('Deploy') {
      steps {
        sh '''
            docker compose down
            docker compose pull
            docker compose up -d
        '''
      }
    }
    stage('Smoke test') {
      steps {
        sh 'sleep 10'
        sh 'curl -f http://localhost:8000/health/|| exit 1'
      }
    }
  }


  post {
    success {
      echo 'CI pipeline completed successfully'
    }
    failure {
      echo 'CI pipeline failed'
    }
  }
}
  
      
