pipeline{
  agent any

  environment {
    DOCKER_IMAGE = "sobin/mydjangoapp"
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
    stage('Cleanup') {
      steps {
        sh 'docker compose down'
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
  
      
