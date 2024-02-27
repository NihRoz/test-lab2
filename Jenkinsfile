pipeline {
    agent {
        docker {
            image 'ubuntu:latest' // Используем образ gcc для сборки C++ проекта   
        }
    }
    stages {
        stage('Prepare') {
            steps {
                sh 'echo preparing'
            }
        }
        stage('Build') {
            steps {
                sh 'apt update -y && apt upgrade -y && apt install gcc -y'
                sh 'g++ -o artifact main.cpp' // Сборка проекта
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts 'artifact' // Архивация бинарного файла
            }
        }
    }
}
