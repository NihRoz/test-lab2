pipeline {
    agent {
        docker {
            image 'gcc:latest' // Используем образ с установленным компилятором GCC
        }
    }
    stages {
        stage('Сборка') {
            steps {
                sh 'g++ -o my_program main.cpp' // Компилируем исходный файл
            }
            post {
                success {
                    archiveArtifacts 'my_program' // Загружаем бинарный файл как артефакт сборки
                }
            }
        }
    }
}
