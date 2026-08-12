import logging

from lesson_23_api_testing.api.models import CarResponse, StatusResponse

logger = logging.getLogger(__name__)


class CarsAPI:
    def __init__(self, session, base_url):
        # Используем общую авторизованную сессию для запросов к API машин
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

        self._validate_response(
            response,
            CarResponse,
            expected_status_code=201,
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

        self._validate_response(response, StatusResponse)

        return response
