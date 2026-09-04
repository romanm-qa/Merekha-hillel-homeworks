# Lesson 31. Jenkins basics and pipeline

## 1. Что такое CI/CD

### Continuous Integration (CI)

**Continuous Integration** — практика, при которой изменения разработчиков регулярно добавляются в общий репозиторий и автоматически проверяются.

После `push` или создания Pull Request CI-система может:

- получить актуальный код;
- установить зависимости;
- выполнить статические проверки;
- собрать приложение;
- запустить автотесты;
- опубликовать результаты;
- сообщить команде, прошло ли изменение проверки.

Главная цель CI — как можно раньше обнаружить проблему после изменения кода.

Падение pipeline не всегда означает баг приложения. Причиной может быть:

- дефект в приложении;
- дефект или устаревшее ожидание в автотесте;
- нестабильный тест;
- проблема тестовых данных;
- проблема окружения или инфраструктуры.

После падения автоматизатор анализирует логи и отчёты и определяет источник проблемы.

### Continuous Delivery и Continuous Deployment

Эти понятия часто объединяют сокращением **CD**, но между ними есть разница.

- **Continuous Delivery** — приложение автоматически собирается и проверяется, но выпуск в production подтверждает человек.
- **Continuous Deployment** — успешно проверенная версия автоматически разворачивается в production без ручного подтверждения.

Упрощённая цепочка CI/CD:

```text
Commit → Build → Tests → Deploy to staging → Staging tests → Deploy to production
```

## 2. Что такое Jenkins

**Jenkins** — сервер автоматизации с открытым исходным кодом. Он выполняет заранее описанный процесс сборки, тестирования и развёртывания проекта.

Jenkins может:

- получать код из Git-репозитория;
- устанавливать зависимости;
- запускать команды и скрипты;
- собирать приложение или Docker-образ;
- запускать автотесты;
- публиковать JUnit, HTML и Allure-отчёты;
- сохранять артефакты, логи, скриншоты и видео;
- запускать следующие этапы только после успешных проверок;
- выполнять деплой;
- отправлять уведомления.

Jenkins не тестирует приложение самостоятельно. Он управляет инструментами, которые выполняют работу:

```text
Jenkins → Docker Compose → pytest → результаты → Allure/JUnit
```

В этой схеме:

- Jenkins определяет, **что и когда запускать**;
- Docker создаёт одинаковое окружение;
- pytest выполняет тесты;
- JUnit и Allure представляют результаты.

## 3. Jenkins controller и agent

### Controller

**Jenkins controller** управляет Jenkins:

- хранит конфигурацию;
- предоставляет веб-интерфейс;
- планирует сборки;
- распределяет задачи;
- хранит информацию о запусках.

### Agent

**Agent** — машина или окружение, где фактически выполняются шаги pipeline.

Для учебного локального Jenkins controller и agent могут находиться на одном Mac. В большом проекте controller управляет несколькими отдельными агентами, например Linux-, Windows- и macOS-машинами.

Важно: команда `sh` выполняется на выбранном агенте, поэтому нужные программы должны быть доступны именно там.

## 4. Локальный Jenkins и `localhost`

Если Jenkins запущен на Mac и открыт по адресу:

```text
http://localhost:8080
```

то:

- `localhost` означает текущий компьютер — Mac;
- `8080` — порт Jenkins.

При этом `localhost` всегда относится к тому окружению, внутри которого выполняется команда:

- в браузере на Mac — к Mac;
- внутри Jenkins-контейнера — к Jenkins-контейнеру;
- внутри контейнера с тестами — к контейнеру с тестами.

Поэтому контейнер с тестами обращается к PostgreSQL не через `localhost`, а через имя Compose-сервиса, например:

```text
postgres:5432
```

## 5. Способы установки Jenkins

Jenkins можно установить:

- непосредственно в операционную систему;
- в Docker-контейнер;
- на удалённый сервер;
- в облачную инфраструктуру.

Jenkins работает на Java, поэтому при обычной установке требуется совместимая JDK.

### Jenkins непосредственно на Mac

Jenkins работает как локальный сервис и может обращаться к установленным на Mac программам, включая Docker Desktop.

Для нашей учебной схемы это самый простой вариант:

```text
Mac
├── Jenkins
└── Docker Desktop
    ├── PostgreSQL
    └── Python + pytest
```

### Jenkins в Docker

Docker также можно использовать только для установки самого Jenkins:

```text
Mac → Docker → Jenkins container
```

Это не означает, что Python-тесты автоматически будут запускаться в отдельных контейнерах. Официальному Jenkins-контейнеру могут дополнительно понадобиться:

- Python и pip;
- Docker CLI;
- доступ к Docker daemon хоста;
- корректные права на Docker socket.

Поэтому Jenkins в Docker, который должен запускать другие Docker-контейнеры, требует дополнительной настройки.

## 6. Что такое Jenkins job, build и workspace

### Job

**Job** — настроенная задача Jenkins. Например, job может описывать pipeline для проверки Python-проекта.

### Build

**Build** — один конкретный запуск job. Запуски получают номера:

```text
#1, #2, #3 ...
```

Каждый build имеет статус, логи, продолжительность и результаты тестов.

### Workspace

**Workspace** — рабочая директория Jenkins, куда он получает код и где выполняет команды pipeline.

Jenkins проверяет код из репозитория в своей рабочей директории, а не незакоммиченные изменения из проекта, открытого в IDE.

## 7. Что такое Jenkins Pipeline

**Pipeline** — описанная последовательность этапов CI/CD.

Pipeline as Code означает, что процесс хранится в репозитории в виде файла `Jenkinsfile`.

Преимущества такого подхода:

- pipeline версионируется вместе с проектом;
- изменения видны в Git history;
- pipeline можно проверить через Pull Request;
- конфигурацию легче переносить и восстанавливать;
- команда видит, как именно собирается и тестируется проект.

`Jenkinsfile` использует синтаксис на основе Groovy DSL. Для обычного Declarative Pipeline глубокое знание Groovy не требуется.

## 8. Declarative и Scripted Pipeline

Jenkins поддерживает два основных формата.

### Declarative Pipeline

Declarative Pipeline имеет строгую и понятную структуру:

```groovy
pipeline {
    agent any

    stages {
        stage('Run tests') {
            steps {
                sh 'python -m pytest'
            }
        }
    }
}
```

Преимущества:

- легче читать;
- проще поддерживать;
- Jenkins может заранее проверить часть структуры;
- есть стандартные блоки `environment`, `options`, `parameters`, `when` и `post`;
- подходит для большинства проектов.

### Scripted Pipeline

Scripted Pipeline является более свободным Groovy-скриптом:

```groovy
node {
    stage('Run tests') {
        sh 'python -m pytest'
    }
}
```

Он предоставляет больше контроля, условий, циклов и динамической логики, но сложнее читается и поддерживается.

Для нашей домашней работы используем **Declarative Pipeline**.

## 9. Основные элементы Declarative Pipeline

### `pipeline`

Корневой блок Declarative Pipeline:

```groovy
pipeline {
    // конфигурация pipeline
}
```

### `agent`

Определяет, где будет выполняться pipeline:

```groovy
agent any
```

`any` означает любой доступный Jenkins-agent.

### `stages`

Содержит все основные стадии:

```groovy
stages {
    stage('Build') { /* ... */ }
    stage('Test') { /* ... */ }
}
```

### `stage`

Логический этап pipeline. Например:

- Checkout;
- Build;
- Test;
- Publish results;
- Deploy.

Стадии делают pipeline понятным и отображаются отдельно в интерфейсе Jenkins.

### `steps`

Содержит конкретные действия стадии:

```groovy
stage('Test') {
    steps {
        sh 'python -m pytest'
    }
}
```

### `sh`

Запускает shell-команду на Unix-подобном агенте:

```groovy
sh 'python -m pytest'
```

На Windows вместо него часто используется `bat` или `powershell`.

### `environment`

Определяет переменные окружения:

```groovy
environment {
    APP_ENV = 'test'
}
```

Секреты нельзя записывать в `Jenkinsfile` открытым текстом. Для них используются Jenkins Credentials.

### `post`

Содержит действия, которые выполняются после основных стадий:

```groovy
post {
    always {
        echo 'Pipeline finished'
    }
    success {
        echo 'Pipeline passed'
    }
    failure {
        echo 'Pipeline failed'
    }
}
```

Полезные условия:

- `always` — всегда;
- `success` — только после успеха;
- `failure` — только после ошибки;
- `unstable` — если build помечен как нестабильный;
- `changed` — если результат отличается от предыдущего запуска;
- `cleanup` — для финальной очистки.

Публикацию результатов обычно помещают в `post { always { ... } }`, чтобы отчёт сохранялся даже при падении тестов.

## 10. Получение кода из репозитория

### `git`

Простой способ получить конкретный репозиторий:

```groovy
git url: 'https://github.com/user/repository.git', branch: 'main'
```

### `checkout scm`

Если job настроена как **Pipeline script from SCM**, Jenkins уже знает репозиторий и ветку:

```groovy
checkout scm
```

Declarative Pipeline с `agent` обычно автоматически выполняет checkout. Чтобы управлять этим явно, можно отключить автоматический checkout:

```groovy
options {
    skipDefaultCheckout(true)
}
```

и затем добавить отдельную стадию:

```groovy
stage('Checkout') {
    steps {
        checkout scm
    }
}
```

Это делает процесс наглядным и не допускает двойного получения кода.

## 11. Pipeline script и Pipeline script from SCM

### Pipeline script

Код вводится вручную в интерфейсе Jenkins.

Подходит для быстрого эксперимента, но конфигурация не хранится вместе с проектом.

### Pipeline script from SCM

Jenkins получает `Jenkinsfile` из Git-репозитория.

Для домашней работы выбираем этот вариант, потому что `Jenkinsfile` должен быть сохранён в репозитории.

Основные настройки job:

```text
Definition: Pipeline script from SCM
SCM: Git
Repository URL: URL репозитория
Branch Specifier: ветка домашней работы
Script Path: Jenkinsfile
```

## 12. Credentials

**Jenkins Credentials** — защищённое хранилище секретных данных.

Там могут храниться:

- username и password;
- GitHub token;
- SSH private key;
- API token;
- secret text;
- certificate.

Секретам назначаются идентификаторы, например:

```text
github-token
```

В pipeline указывается идентификатор, а не само значение секрета.

Если репозиторий публичный, для чтения кода credentials обычно не требуются. Для приватного репозитория понадобится токен или SSH-ключ.

Нельзя хранить пароли и токены:

- в `Jenkinsfile`;
- в `.env`, который попадает в Git;
- непосредственно в исходном коде;
- в открытом виде в командах, если они попадут в лог.

## 13. Запуск Python-тестов без Docker

Jenkins может создать виртуальное окружение и запустить тесты непосредственно на агенте:

```groovy
stage('Set up Python') {
    steps {
        sh 'python3 -m venv .venv'
        sh '.venv/bin/python -m pip install -r requirements.txt'
    }
}

stage('Run tests') {
    steps {
        sh '.venv/bin/python -m pytest'
    }
}
```

Не следует рассчитывать на такую последовательность отдельных шагов:

```groovy
sh 'source .venv/bin/activate'
sh 'pytest'
```

Каждый `sh` может запускаться в отдельной оболочке, поэтому активация окружения не обязана сохраниться. Надёжнее напрямую использовать:

```text
.venv/bin/python
.venv/bin/pip
```

## 14. Запуск тестов через Docker Compose

Для проекта с PostgreSQL удобно описать окружение в Docker Compose:

```text
Jenkins
  ↓
Docker Compose
├── postgres
└── tests
```

Пример команды:

```bash
docker compose up --build --abort-on-container-exit --exit-code-from tests
```

Флаги означают:

- `--build` — пересобрать образ при необходимости;
- `--abort-on-container-exit` — остановить запуск после завершения одного из контейнеров;
- `--exit-code-from tests` — вернуть Jenkins код завершения контейнера `tests`.

Последний флаг особенно важен: если pytest завершится с ошибкой, Docker Compose должен вернуть ненулевой exit code, а Jenkins — пометить pipeline как failed.

После запуска окружение нужно очищать:

```bash
docker compose down --volumes --remove-orphans
```

Если данные должны сохраняться между запусками, удаление volumes нужно применять осознанно. Для изолированных тестов чистая база обычно предпочтительнее.

## 15. Результаты pytest в формате JUnit XML

**JUnit XML** — стандартный формат результатов тестирования, который понимает Jenkins. Он подходит не только для Java: pytest тоже умеет создавать такой файл.

Запуск pytest:

```bash
pytest --junitxml=test-reports/results.xml
```

Публикация в Jenkins:

```groovy
junit testResults: 'test-reports/*.xml'
```

После этого Jenkins сможет показать:

- количество пройденных тестов;
- количество упавших тестов;
- skipped-тесты;
- длительность;
- историю результатов.

Важный момент: шаг `junit` не создаёт результаты. Он только читает XML, который до этого должен создать pytest.

## 16. Allure в Python и Jenkins

Для интеграции нужны две разные части.

### `allure-pytest` в Python-проекте

Адаптер запускается вместе с pytest и создаёт сырые результаты:

```bash
pytest --alluredir=allure-results
```

Каталог содержит JSON-файлы и attachments, но ещё не является готовой HTML-страницей.

### Allure Plugin в Jenkins

Плагин Jenkins получает `allure-results`, генерирует отчёт и добавляет ссылку **Allure Report** к build.

Пример шага:

```groovy
allure([
    includeProperties: false,
    jdk: '',
    properties: [],
    reportBuildPolicy: 'ALWAYS',
    results: [[path: 'allure-results']]
])
```

Кроме плагина, в `Manage Jenkins → Tools` обычно настраивается Allure Commandline.

### JUnit и Allure одновременно

Можно сформировать оба результата одним запуском:

```bash
pytest \
    --junitxml=test-reports/results.xml \
    --alluredir=allure-results
```

JUnit даёт встроенную статистику Jenkins, а Allure — подробный интерактивный отчёт.

## 17. Артефакты Jenkins

**Artifact** — файл, который Jenkins сохраняет после build.

Примеры:

- логи;
- скриншоты;
- видео UI-тестов;
- HTML-отчёты;
- собранные пакеты;
- архивы;
- Docker image metadata.

Пример архивирования:

```groovy
archiveArtifacts artifacts: 'logs/**', allowEmptyArchive: true
```

Результаты тестов и build artifacts связаны, но это не одно и то же: `junit` анализирует тестовый XML, а `archiveArtifacts` просто сохраняет файлы.

## 18. Статусы Jenkins build

Основные статусы:

- **Success** — все обязательные шаги выполнены успешно;
- **Failure** — команда или стадия завершилась ошибкой;
- **Unstable** — build завершён, но есть проблемы, например упавшие тесты;
- **Aborted** — запуск остановлен вручную или по timeout;
- **Not Built** — этап не выполнялся.

Обычно shell-команда с exit code `0` считается успешной, а с ненулевым кодом — ошибкой.

## 19. Варианты запуска pipeline

Pipeline можно запускать:

- вручную кнопкой **Build Now**;
- после webhook от GitHub;
- с помощью периодической проверки репозитория (`Poll SCM`);
- по расписанию;
- после другого job;
- через API.

### Webhook

GitHub отправляет Jenkins HTTP-запрос сразу после события. Это быстрый и нормальный вариант для доступного из интернета Jenkins.

Но GitHub не может напрямую обратиться к адресу:

```text
http://localhost:8080
```

потому что `localhost` доступен только на самом Mac. Для локального Jenkins потребовался бы внешний адрес или туннель.

### Poll SCM

Jenkins периодически проверяет, появились ли новые коммиты. Это можно использовать для учебного локального Jenkins без публичного адреса.

Минусы:

- запуск происходит не мгновенно;
- Jenkins регулярно опрашивает GitHub;
- это менее эффективно, чем webhook.

## 20. Staging и production

- **Staging** — тестовое окружение, максимально похожее на production. Там выполняются проверки перед релизом.
- **Production** — рабочее окружение, которым пользуются реальные пользователи.

Пример доставки:

```text
Build image → Tests → Deploy to staging → Staging tests → Approval → Production
```

Docker позволяет продвигать один и тот же проверенный образ:

```text
my-app:1.4.0 → staging → production
```

Для staging и production используются разные:

- базы данных;
- секреты;
- URL;
- переменные окружения;
- права доступа;
- иногда вычислительные ресурсы.

Нельзя использовать production-базу для обычных тестов и нельзя хранить production-секреты в репозитории.

## 21. Полезные Jenkins plugins

Для нашей задачи важны:

- **Pipeline** — выполнение pipeline;
- **Git** — работа с Git-репозиториями;
- **GitHub** — дополнительная интеграция с GitHub;
- **Credentials** — безопасное хранение секретов;
- **JUnit** — публикация JUnit XML;
- **Allure** — публикация Allure-отчётов;
- **HTML Publisher** — публикация готовых HTML-отчётов;
- **AnsiColor** — цветной console output;
- **Build Timeout** — ограничение времени build.

Устанавливать все существующие плагины не нужно. Лишние плагины увеличивают сложность обновлений и поверхность атаки Jenkins.

## 22. Пример учебного Declarative Pipeline без Docker

```groovy
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest \
                        --junitxml=test-reports/results.xml \
                        --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'test-reports/*.xml', allowEmptyResults: true
            allure results: [[path: 'allure-results']]
        }
    }
}
```

Это учебный пример. Точные пути, плагины и команды зависят от структуры проекта и конфигурации Jenkins-agent.

## 23. План pipeline для нашей домашней работы

Для нашего проекта используем следующую схему:

```text
GitHub
  ↓
Jenkins на Mac
  ↓
Docker Compose
├── PostgreSQL
└── Python + pytest
  ↓
JUnit XML + allure-results
  ↓
JUnit и Allure в Jenkins
```

Предварительные стадии:

1. **Checkout** — получение кода ветки домашней работы.
2. **Build** — сборка Docker-образа тестов.
3. **Run tests** — запуск PostgreSQL и pytest через Docker Compose.
4. **Publish results** — публикация JUnit и Allure.
5. **Cleanup** — остановка и удаление тестовых контейнеров.

Email-уведомления для домашней работы не настраиваем по уточнению преподавателя.

## 24. Важные практические правила

1. Хранить `Jenkinsfile` в Git-репозитории.
2. Не записывать секреты в исходный код.
3. Проверять exit code тестовой команды.
4. Публиковать результаты даже после падения тестов.
5. Очищать временные контейнеры и окружение.
6. Не использовать одну базу одновременно для независимых тестовых запусков без изоляции.
7. Не устанавливать зависимости глобально без необходимости.
8. Использовать понятные названия стадий.
9. Добавлять timeout, чтобы зависшая сборка не занимала agent бесконечно.
10. Проверять не только зелёный, но и намеренно падающий сценарий pipeline.

## 25. Короткий итог

- Jenkins — сервер автоматизации CI/CD.
- Pipeline описывает последовательность автоматических действий.
- `Jenkinsfile` хранит pipeline как код.
- Declarative Pipeline проще и подходит для нашей задачи.
- Stage — логический этап, step — конкретное действие.
- Jenkins запускает инструменты, но не заменяет pytest, Docker или Allure.
- Docker обеспечивает воспроизводимое окружение.
- JUnit XML предоставляет Jenkins стандартную статистику тестов.
- Allure показывает подробный отчёт.
- Credentials позволяют не хранить секреты в коде.
- Staging используется для проверки, production — для реальных пользователей.
- Для домашней работы Jenkins будет работать на Mac, а PostgreSQL и тесты — в Docker Compose.
