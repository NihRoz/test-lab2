pipeline {
    agent {
        dockerContainer {
            image 'gcc:latest' // Используем образ gcc для сборки C++ проекта
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'g++ -o hello hello.cpp' // Сборка проекта
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts 'hello' // Архивация бинарного файла
            }
        }
    }
}
