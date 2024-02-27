pipeline {
    agent {
        docker {
            image 'gcc:latest' // Используем образ gcc для сборки C++ проекта
            args '-u root:root' // Jenkins требует прав root для работы внутри контейнера
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sudo g++ -o artifact main.cpp' // Сборка проекта
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts 'artifact' // Архивация бинарного файла
            }
        }
    }
}
