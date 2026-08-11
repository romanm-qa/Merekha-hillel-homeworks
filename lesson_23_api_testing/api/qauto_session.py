import logging

import requests

from lesson_23_api_testing.config import (
    BASE_URL,
    BASIC_AUTH_LOGIN,
    BASIC_AUTH_PASSWORD,
    TEST_USER_EMAIL,
    TEST_USER_PASSWORD,
)

logger = logging.getLogger(__name__)


class QAutoSession:
    def __init__(self):
        self.base_url = BASE_URL
        # Создаём общую сессию и настраиваем Basic Auth для всех запросов
        self.session = requests.Session()
        self.session.auth = (
            BASIC_AUTH_LOGIN,
            BASIC_AUTH_PASSWORD,
        )

    def sign_in(self):
        # Формируем данные для входа тестового пользователя
        login_data = {
            "email": TEST_USER_EMAIL,
            "password": TEST_USER_PASSWORD,
            "remember": False,
        }

        logger.info("Signing in to QAuto")

        # Авторизуем пользователя и сохраняем полученную cookie в сессии
        response = self.session.post(
            f"{self.base_url}/auth/signin",
            json=login_data,
        )

        logger.info(
            "Sign-in response status: %s",
            response.status_code,
        )

        return response

    def sign_out(self):
        logger.info("Signing out from QAuto")

        response = self.session.get(
            f"{self.base_url}/auth/logout",
        )

        logger.info(
            "Sign-out response status: %s",
            response.status_code,
        )

        return response

    def close(self):
        # Закрываем HTTP-сессию после завершения всех тестов
        self.session.close()
