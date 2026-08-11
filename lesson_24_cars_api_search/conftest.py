import logging
import os
from pathlib import Path

import pytest
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Загружаем настройки Cars API из файла .env
load_dotenv()

BASE_URL = os.getenv("CARS_API_URL")
USERNAME = os.getenv("CARS_API_USERNAME")
PASSWORD = os.getenv("CARS_API_PASSWORD")

# Настраиваем запись логов в консоль и файл рядом с тестами
LOG_FILE = Path(__file__).with_name("test_search.log")

logger = logging.getLogger("cars_api_tests")
logger.setLevel(logging.INFO)
logger.propagate = False

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# Не добавляем обработчики повторно при повторной загрузке conftest.py
if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


@pytest.fixture(scope="class")
def authenticated_session():
    """Создаёт авторизованную HTTP-сессию для тестового класса."""
    if not all((BASE_URL, USERNAME, PASSWORD)):
        pytest.fail("Cars API environment variables are not configured")

    session = requests.Session()

    try:
        logger.info("Authenticating in Cars API")

        response = session.post(
            f"{BASE_URL}/auth",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10,
        )
        response.raise_for_status()

        access_token = response.json().get("access_token")

        if not access_token:
            pytest.fail("Authentication response does not contain access_token")

        session.headers.update(
            {"Authorization": f"Bearer {access_token}"}
        )

        logger.info("Cars API authentication was successful")

        yield session

    finally:
        session.close()
        logger.info("Cars API session was closed")


@pytest.fixture(scope="session")
def cars_api_url():
    """Возвращает базовый URL Cars API."""
    if not BASE_URL:
        pytest.fail("CARS_API_URL environment variable is not configured")

    return BASE_URL
