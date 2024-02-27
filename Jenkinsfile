pipeline {
  agent {
    docker {
      image 'ubuntu:20.04'
      args '-v /workspace:/app'
    }
  }
  stages {
    stage('Checkout') {
      steps {
        git credentialsId: 'jenkins-git-credentials', url: 'https://gitlab.com/user/project.git'
      }
    }
    stage('Build') {
      steps {
        sh 'mkdir build && cd build && cmake .. && make'
      }
    }
    stage('Artifact') {
      steps {
        archiveArtifacts artifacts: 'build/main', fingerprint: true
      }
    }
  }
}
