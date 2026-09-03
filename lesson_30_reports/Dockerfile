# Базовый образ с Python
FROM python:3.14

# Рабочая папка внутри контейнера
WORKDIR /app

# Копируем код приложения из новой домашней работы в контейнер
COPY lesson_30_reports /app

# Копируем файл зависимостей из корня репозитория
COPY requirements.txt /app

# Устанавливаем все зависимости из requirements.txt
RUN pip install -r requirements.txt

# Команда, которая выполнится при запуске контейнера — прогон тестов
CMD ["pytest"]