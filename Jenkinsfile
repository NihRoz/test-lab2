pipeline {
    agent {
        docker {
            image 'ubuntu:latest' // Используем образ Ubuntu
        }
    }
    stages {
        stage('Setup') {
            steps {
                sh 'apt-get update && apt-get install -y g++' // Установка g++
            }
        }
        stage('Build') {
            steps {
                sh 'g++ -o main main.cpp' // Сборка проекта
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts 'main' // Архивация бинарного файла
            }
        }
    }
}
