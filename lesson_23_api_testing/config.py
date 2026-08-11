import os

from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
