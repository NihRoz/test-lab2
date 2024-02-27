pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo Hello Jenkins!'
                sh 'g++ -o my_program main.cpp' // Компилируем исходный файл
                sh './my_program'
            }
            post {
                success {
                    archiveArtifacts 'my_program' // Загружаем бинарный файл как артефакт сборки
                }
            }
        }
    }
}
