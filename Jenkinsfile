pipeline {
    // Pipeline выполняется на доступном Jenkins-узле
    agent any

    options {
        // Checkout выполняется вручную в отдельной стадии
        skipDefaultCheckout(true)

        // Добавляем время к строкам логов
        timestamps()

        // Включаем корректное отображение цветов в консоли
        ansiColor('xterm')

        // Запрещаем одновременный запуск сборок,
        // чтобы они не конфликтовали за порт PostgreSQL
        disableConcurrentBuilds()

        // Останавливаем pipeline, если он выполняется слишком долго
        timeout(time: 15, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code'

                // Получаем код из репозитория и ветки,
                // настроенных в Pipeline script from SCM
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker images'

                // Собираем тестовый образ из Dockerfile
                sh 'docker compose -f lesson_31_jenkins/docker-compose.yml build'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Starting PostgreSQL and running tests'

                // При падении тестов отмечаем сборку как неуспешную,
                // но продолжаем pipeline для публикации отчётов
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        docker compose -f lesson_31_jenkins/docker-compose.yml up \
                            --abort-on-container-exit \
                            --exit-code-from tests
                    '''
                }
            }
        }

        stage('Publish results') {
            steps {
                echo 'Publishing JUnit and Allure reports'

                // Публикуем стандартную статистику тестов в Jenkins
                junit(
                    testResults: 'lesson_31_jenkins/test-reports/*.xml',
                    allowEmptyResults: true
                )

                // Создаём подробный Allure-отчёт
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'lesson_31_jenkins/allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker resources'

            // Очистка выполняется при любом результате pipeline
            sh(
                returnStatus: true,
                script: '''
                    docker compose -f lesson_31_jenkins/docker-compose.yml down \
                        --volumes \
                        --remove-orphans
                '''
            )
        }

        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}