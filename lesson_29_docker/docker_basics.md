# Lesson 29: Docker

## Зачем нужен Docker

Docker решает проблему «у меня работает, а у тебя нет», когда приложение ведёт себя по-разному из-за разных версий языка, библиотек или настроек окружения.

Docker позволяет упаковать приложение, его код и зависимости в **образ**, на основе которого запускаются **контейнеры**.

Конфигурация, настройки окружения и секретные данные обычно не записываются внутрь образа, а передаются контейнеру при запуске через:

* environment variables;
* `.env`-файлы;
* Docker secrets;
* настройки CI/CD.

Благодаря Docker приложение можно запускать в предсказуемом окружении:

* на компьютере разработчика;
* на компьютере QA-инженера;
* на CI-сервере;
* в staging- или production-окружении.

---

## Образ и контейнер

### Образ — Image

**Образ** — неизменяемый шаблон, содержащий файловую систему, код приложения, зависимости и инструкции для запуска.

Сам по себе образ не выполняется. Он используется для создания контейнеров.

### Контейнер — Container

**Контейнер** — запущенный экземпляр образа.

Из одного образа можно запустить несколько независимых контейнеров.

Аналогия из Python:

```python
class Application:
    pass


container = Application()
```

Условно:

* класс `Application` — образ;
* объект `container` — контейнер.

Это упрощённая аналогия, но она помогает понять связь между образом и контейнером.

### Контейнер и виртуальная машина

Виртуальная машина обычно содержит полноценную гостевую операционную систему со своим ядром.

Контейнер использует ядро операционной системы хоста, поэтому контейнеры обычно:

* занимают меньше места;
* запускаются быстрее;
* потребляют меньше ресурсов;
* удобнее масштабируются.

При этом контейнер не является полноценной виртуальной машиной.

---

## Установка и проверка Docker

На Windows и macOS Docker обычно устанавливается через Docker Desktop.

На Linux можно установить Docker Engine через официальный репозиторий Docker, следуя документации для используемого дистрибутива.

Проверить установленную версию:

```bash
docker --version
```

Проверить состояние Docker Engine и получить информацию об окружении:

```bash
docker info
```

Если Docker Engine не запущен, команда `docker info` завершится ошибкой.

---

## Dockerfile

**Dockerfile** — текстовый файл с инструкциями, по которым Docker собирает образ.

Обычно файл называется именно:

```text
Dockerfile
```

без расширения.

### Основные инструкции Dockerfile

| Инструкция   | Назначение                                         |
| ------------ | -------------------------------------------------- |
| `FROM`       | Определяет базовый образ                           |
| `WORKDIR`    | Задаёт рабочую директорию внутри образа            |
| `COPY`       | Копирует файлы из build context внутрь образа      |
| `RUN`        | Выполняет команду во время сборки образа           |
| `ENV`        | Задаёт переменную окружения внутри образа          |
| `EXPOSE`     | Документирует порт, который использует приложение  |
| `CMD`        | Задаёт команду по умолчанию при запуске контейнера |
| `ENTRYPOINT` | Задаёт основную выполняемую команду контейнера     |

---

## Пример Dockerfile для Python-тестов

Файл `requirements.txt`:

```text
pytest
psycopg2-binary
```

Dockerfile:

```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]
```

### Разбор Dockerfile

```dockerfile
FROM python:3.9
```

Используем готовый базовый образ с Python 3.9.

```dockerfile
WORKDIR /app
```

Создаём рабочую директорию `/app` внутри образа. Следующие команды будут выполняться относительно неё.

```dockerfile
COPY requirements.txt .
```

Копируем файл зависимостей в текущую рабочую директорию контейнера.

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Устанавливаем зависимости во время сборки образа.

Флаг `--no-cache-dir` запрещает `pip` сохранять локальный кеш пакетов внутри образа и помогает уменьшить его размер.

```dockerfile
COPY . .
```

Копируем остальные файлы проекта внутрь образа.

```dockerfile
CMD ["pytest"]
```

Задаём команду по умолчанию, которая выполнится при запуске контейнера.

### Почему зависимости копируются отдельно

Если сначала скопировать `requirements.txt`, установить зависимости и только потом скопировать остальной проект, Docker сможет повторно использовать кеш слоя с установленными зависимостями.

Пока `requirements.txt` не меняется, зависимости не придётся устанавливать заново при каждой сборке образа.

---

## Основные команды Docker CLI

| Команда                             | Назначение                                        |
| ----------------------------------- | ------------------------------------------------- |
| `docker build -t myimage .`         | Собрать образ из Dockerfile                       |
| `docker run myimage`                | Создать и запустить контейнер из образа           |
| `docker run --rm myimage`           | Запустить контейнер и удалить его после остановки |
| `docker ps`                         | Показать запущенные контейнеры                    |
| `docker ps -a`                      | Показать все контейнеры                           |
| `docker stop <name_or_id>`          | Остановить контейнер                              |
| `docker start <name_or_id>`         | Повторно запустить остановленный контейнер        |
| `docker rm <name_or_id>`            | Удалить остановленный контейнер                   |
| `docker logs <name_or_id>`          | Посмотреть логи контейнера                        |
| `docker exec -it <name_or_id> bash` | Запустить Bash внутри работающего контейнера      |
| `docker exec -it <name_or_id> sh`   | Запустить `sh`, если Bash отсутствует             |
| `docker images`                     | Показать локальные образы                         |
| `docker rmi <image>`                | Удалить образ                                     |
| `docker pull postgres`              | Скачать образ PostgreSQL                          |
| `docker network ls`                 | Показать Docker-сети                              |
| `docker volume ls`                  | Показать Docker volumes                           |

Команда:

```bash
docker exec -it <name_or_id> bash
```

не подключается к контейнеру по SSH. Она запускает новый процесс Bash внутри уже работающего контейнера.

---

## Сборка образа

Команда:

```bash
docker build -t myapp .
```

означает:

* `docker build` — собрать образ;
* `-t myapp` — присвоить образу имя `myapp`;
* `.` — использовать текущую директорию как build context и найти в ней Dockerfile.

Посмотреть созданный образ:

```bash
docker images
```

---

## Запуск контейнера

Запустить контейнер из образа:

```bash
docker run myapp
```

Присвоить контейнеру имя:

```bash
docker run --name myapp-container myapp
```

Автоматически удалить контейнер после завершения:

```bash
docker run --rm myapp
```

Запустить контейнер в фоне:

```bash
docker run -d --name myapp-container myapp
```

Флаг `-d` означает detached mode — контейнер работает в фоне и не занимает терминал.

---

## Docker Network

Docker network позволяет контейнерам находить друг друга и обмениваться данными.

Создать сеть:

```bash
docker network create test-network
```

Посмотреть список сетей:

```bash
docker network ls
```

Подключить контейнер к сети можно во время его запуска:

```bash
docker run --network test-network myimage
```

Если несколько контейнеров подключены к одной пользовательской Docker-сети, они могут обращаться друг к другу по имени контейнера.

---

## `localhost` и имя контейнера

Это один из самых важных нюансов при работе с Docker.

### Подключение с компьютера

Если Python-приложение запускается на компьютере, а PostgreSQL — в Docker-контейнере, подключение выполняется через `localhost` и внешний порт:

```python
connection = psycopg2.connect(
    dbname="test_db",
    user="test_user",
    password="test_password",
    host="localhost",
    port="5433",
)
```

Это соответствует пробросу порта:

```bash
-p 5433:5432
```

Где:

* `5433` — порт компьютера;
* `5432` — внутренний порт PostgreSQL в контейнере.

### Подключение между контейнерами

Если Python-приложение и PostgreSQL запущены в разных контейнерах одной Docker-сети, `localhost` использовать нельзя.

Внутри контейнера `localhost` означает сам этот контейнер.

Для подключения к PostgreSQL необходимо использовать имя его контейнера и внутренний порт:

```python
connection = psycopg2.connect(
    dbname="test_db",
    user="test_user",
    password="test_password",
    host="db",
    port="5432",
)
```

В этом примере `db` — имя контейнера PostgreSQL.

Ключевое правило:

* с хоста — `localhost` и внешний порт;
* из одного контейнера в другой — имя контейнера или сервиса и внутренний порт.

---

## Docker Volume

Контейнеры считаются временными. Если удалить контейнер PostgreSQL, данные внутри него также могут быть потеряны.

Для сохранения данных отдельно от контейнера используется **volume**.

Создать volume:

```bash
docker volume create postgres-data
```

Посмотреть volumes:

```bash
docker volume ls
```

Подключить volume к PostgreSQL:

```bash
docker run -d \
  --name db \
  -e POSTGRES_USER=test_user \
  -e POSTGRES_PASSWORD=test_password \
  -e POSTGRES_DB=test_db \
  -v postgres-data:/var/lib/postgresql/data \
  postgres
```

Где:

```text
postgres-data
```

— имя Docker volume, а:

```text
/var/lib/postgresql/data
```

— директория, в которой PostgreSQL хранит данные внутри контейнера.

Теперь удаление контейнера не удалит данные из volume.

---

## Запуск PostgreSQL и приложения через `docker run`

Сначала создаём общую Docker-сеть:

```bash
docker network create test-network
```

Создаём volume для PostgreSQL:

```bash
docker volume create postgres-data
```

Запускаем PostgreSQL:

```bash
docker run -d \
  --name db \
  --network test-network \
  -e POSTGRES_USER=test_user \
  -e POSTGRES_PASSWORD=test_password \
  -e POSTGRES_DB=test_db \
  -v postgres-data:/var/lib/postgresql/data \
  postgres
```

Если к PostgreSQL также необходимо подключаться с компьютера, можно добавить проброс порта:

```bash
-p 5433:5432
```

Полная команда:

```bash
docker run -d \
  --name db \
  --network test-network \
  -p 5433:5432 \
  -e POSTGRES_USER=test_user \
  -e POSTGRES_PASSWORD=test_password \
  -e POSTGRES_DB=test_db \
  -v postgres-data:/var/lib/postgresql/data \
  postgres
```

Собираем образ Python-приложения:

```bash
docker build -t myapp .
```

Запускаем приложение в той же сети:

```bash
docker run --rm \
  --name app \
  --network test-network \
  myapp
```

Теперь приложение может обращаться к PostgreSQL по адресу:

```text
db:5432
```

Поскольку в Dockerfile указано:

```dockerfile
CMD ["pytest"]
```

тесты автоматически запустятся внутри контейнера приложения.

---

## Docker Compose

Docker Compose используется для описания и запуска нескольких связанных сервисов.

Например:

* Python-приложение;
* PostgreSQL;
* Redis;
* другие вспомогательные сервисы.

Все сервисы описываются в файле:

```text
docker-compose.yml
```

или:

```text
compose.yaml
```

Современный Docker Compose больше не требует указывать поле `version`.

---

## Пример Docker Compose

```yaml
services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: test_user
      POSTGRES_PASSWORD: test_password
      POSTGRES_DB: test_db
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U test_user -d test_db"]
      interval: 5s
      timeout: 5s
      retries: 5

  app:
    build: .
    depends_on:
      db:
        condition: service_healthy

volumes:
  postgres-data:
```

### Сервис `db`

```yaml
db:
  image: postgres
```

Используется готовый образ PostgreSQL. Отдельный Dockerfile для базы данных не требуется.

### Environment variables

```yaml
environment:
  POSTGRES_USER: test_user
  POSTGRES_PASSWORD: test_password
  POSTGRES_DB: test_db
```

При запуске контейнера создаются пользователь и база данных.

В реальном проекте пароли не следует хранить непосредственно в Compose-файле. Их лучше передавать через `.env`, secrets или настройки CI/CD.

### Volume

```yaml
volumes:
  - postgres-data:/var/lib/postgresql/data
```

Данные PostgreSQL сохраняются отдельно от контейнера.

### Healthcheck

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U test_user -d test_db"]
  interval: 5s
  timeout: 5s
  retries: 5
```

`healthcheck` проверяет, что PostgreSQL действительно готов принимать подключения.

### `depends_on`

```yaml
depends_on:
  db:
    condition: service_healthy
```

Приложение будет запущено после того, как сервис `db` пройдёт healthcheck.

Обычный короткий вариант:

```yaml
depends_on:
  - db
```

задаёт порядок запуска контейнеров, но сам по себе не гарантирует, что PostgreSQL уже готов принимать подключения.

---

## Запуск Docker Compose

Собрать образы и запустить сервисы:

```bash
docker compose up --build
```

Запустить в фоне:

```bash
docker compose up -d --build
```

Посмотреть запущенные сервисы:

```bash
docker compose ps
```

Посмотреть логи:

```bash
docker compose logs
```

Остановить и удалить контейнеры и сеть проекта:

```bash
docker compose down
```

Остановить проект и также удалить volumes:

```bash
docker compose down -v
```

Команду с `-v` следует использовать осторожно, потому что она удалит сохранённые данные базы.

---

## Нужен ли `ports` для связи контейнеров

Для взаимодействия контейнеров внутри одной Compose-сети проброс порта наружу не требуется.

Например, приложение может подключаться к:

```text
db:5432
```

даже если у сервиса `db` нет блока `ports`.

Блок:

```yaml
ports:
  - "5433:5432"
```

нужен только тогда, когда к PostgreSQL необходимо подключаться с компьютера, например через:

* локальное Python-приложение;
* DBeaver;
* PyCharm;
* `psql`;
* другой инструмент вне Docker-сети.

---

## Тестирование PostgreSQL через Docker

Тесты внутри Docker остаются обычными pytest-тестами.

```python
import psycopg2


def create_connection():
    return psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432",
    )


def test_database_connection():
    connection = create_connection()

    try:
        assert connection.closed == 0
    finally:
        connection.close()


def test_data_insertion():
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (id, name) VALUES (%s, %s)",
            (1, "John"),
        )
        connection.commit()

        cursor.execute(
            "SELECT name FROM users WHERE id = %s",
            (1,),
        )
        result = cursor.fetchone()

        assert result[0] == "John"
    finally:
        cursor.close()
        connection.close()
```

Параметры SQL-запросов передаются отдельно:

```python
cursor.execute(
    "SELECT name FROM users WHERE id = %s",
    (1,),
)
```

Это безопаснее, чем формировать SQL-запрос с помощью f-string.

В реальном проекте создание подключения и очистку данных обычно выносят в pytest fixtures.

---

## Dockerfile и Docker Compose выполняют разные задачи

### Dockerfile

Dockerfile отвечает за создание образа одного приложения:

```text
исходный код + зависимости + инструкции → Docker image
```

### Docker Compose

Docker Compose отвечает за совместный запуск и настройку нескольких сервисов:

```text
Python-приложение + PostgreSQL + сеть + volumes
```

Они не заменяют друг друга, а часто используются вместе:

* Dockerfile описывает, как собрать образ приложения;
* Compose описывает, как запустить приложение вместе с другими сервисами.

---

## Итог темы

Docker позволяет:

* создавать воспроизводимое окружение;
* упаковывать приложение и его зависимости в образ;
* запускать изолированные контейнеры;
* поднимать PostgreSQL без локальной установки;
* сохранять данные базы в Docker volume;
* связывать контейнеры через Docker network;
* запускать тесты внутри контейнера;
* управлять несколькими сервисами через Docker Compose;
* использовать одинаковое окружение локально и в CI/CD.

Ключевые правила:

1. Образ — шаблон, контейнер — запущенный экземпляр образа.
2. Внутри Docker-сети контейнеры общаются по имени контейнера или сервиса.
3. `localhost` внутри контейнера указывает на этот же контейнер.
4. Для связи контейнеров используется внутренний порт сервиса.
5. Проброс `ports` нужен для доступа с хоста, а не для внутреннего общения контейнеров.
6. Данные, которые должны пережить удаление контейнера, сохраняются в volume.
7. Обычный `depends_on` задаёт порядок запуска, но не гарантирует готовность базы данных.
8. Dockerfile собирает образ приложения, а Docker Compose управляет несколькими сервисами.
