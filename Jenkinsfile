pipeline {
    agent any
    stages {
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
