import os

from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

BASIC_AUTH_LOGIN = os.getenv("BASIC_AUTH_LOGIN")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
