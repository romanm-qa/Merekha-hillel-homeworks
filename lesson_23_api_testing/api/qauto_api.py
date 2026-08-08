import logging

import requests

from datetime import date

from lesson_23_api_testing.config import (
    BASE_URL,
    BASIC_AUTH_LOGIN,
    BASIC_AUTH_PASSWORD,
    TEST_USER_EMAIL,
    TEST_USER_PASSWORD,
)

logger = logging.getLogger(__name__)


class QAutoAPI:
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

        logger.info("Sign-in response status: %s", response.status_code)

        return response

    def get_expenses(self):
        # Получаем список всех расходов пользователя
        logger.info("Getting all expenses")

        response = self.session.get(
            f"{self.base_url}/expenses",
        )

        logger.info(
            "Get expenses response status: %s",
            response.status_code,
        )

        return response

    def create_car(self, car_brand_id=1, car_model_id=1, mileage=1000):
        # Формируем данные тестовой машины
        car_data = {
            "carBrandId": car_brand_id,
            "carModelId": car_model_id,
            "mileage": mileage,
        }

        logger.info("Creating a test car")

        response = self.session.post(
            f"{self.base_url}/cars",
            json=car_data,
        )

        logger.info(
            "Create car response status: %s",
            response.status_code,
        )

        return response

    def delete_car(self, car_id):
        logger.info("Deleting test car with id: %s", car_id)

        response = self.session.delete(
            f"{self.base_url}/cars/{car_id}",
        )

        logger.info(
            "Delete car response status: %s",
            response.status_code,
        )

        return response

    def create_expense(
            self,
            car_id,
            mileage=1100,
            liters=20,
            total_cost=100,
            reported_at=None,
    ):
        # Если дата не передана, используем текущую дату
        if reported_at is None:
            reported_at = date.today().isoformat()

        expense_data = {
            "carId": car_id,
            "reportedAt": reported_at,
            "mileage": mileage,
            "liters": liters,
            "totalCost": total_cost,
            "forceMileage": False,
        }

        logger.info("Creating an expense for car id: %s", car_id)

        response = self.session.post(
            f"{self.base_url}/expenses",
            json=expense_data,
        )

        logger.info(
            "Create expense response status: %s",
            response.status_code,
        )

        return response

    def delete_expense(self, expense_id):
        logger.info("Deleting expense with id: %s", expense_id)

        response = self.session.delete(
            f"{self.base_url}/expenses/{expense_id}",
        )

        logger.info(
            "Delete expense response status: %s",
            response.status_code,
        )

        return response

    def get_expense(self, expense_id):
        logger.info("Getting expense with id: %s", expense_id)

        response = self.session.get(
            f"{self.base_url}/expenses/{expense_id}",
        )

        logger.info(
            "Get expense response status: %s",
            response.status_code,
        )

        return response

    def update_expense(
            self,
            expense_id,
            car_id,
            mileage=1200,
            liters=25,
            total_cost=150,
            reported_at=None,
    ):
        # Если дата не передана, используем текущую дату
        if reported_at is None:
            reported_at = date.today().isoformat()

        updated_expense_data = {
            "carId": car_id,
            "reportedAt": reported_at,
            "mileage": mileage,
            "liters": liters,
            "totalCost": total_cost,
            "forceMileage": False,
        }

        logger.info("Updating expense with id: %s", expense_id)

        response = self.session.put(
            f"{self.base_url}/expenses/{expense_id}",
            json=updated_expense_data,
        )

        logger.info(
            "Update expense response status: %s",
            response.status_code,
        )

        return response
