pipeline {
    agent {
        docker {
            image 'gcc:latest' // Используем образ gcc для сборки C++ проекта
            args '-u nihroz: ' // Jenkins требует прав root для работы внутри контейнера
        }
    }
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
