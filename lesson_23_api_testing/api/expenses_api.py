import logging
from datetime import date

from lesson_23_api_testing.api.models import ExpenseResponse, StatusResponse

logger = logging.getLogger(__name__)


class ExpensesAPI:
    def __init__(self, session, base_url):
        # Используем общую авторизованную сессию для запросов к API расходов
        self.session = session
        self.base_url = base_url

    @staticmethod
    def _validate_response(
            response,
            response_model,
            expected_status_code=200,
    ):
        assert response.status_code == expected_status_code
        return response_model.model_validate(response.json())

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

        self._validate_response(response, ExpenseResponse)

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

        self._validate_response(response, StatusResponse)

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
