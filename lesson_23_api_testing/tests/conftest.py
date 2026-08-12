import pytest

from lesson_23_api_testing.api.qauto_api import QAutoAPI


@pytest.fixture(scope="session")
def qauto_api():
    # Создаём API-клиент с общей HTTP-сессией
    api = QAutoAPI()

    # Авторизуем тестового пользователя
    api.session.sign_in()

    # Передаём авторизованный API-клиент тестам
    yield api

    # Завершаем и закрываем пользовательскую сессию
    api.session.sign_out()
    api.session.close()


@pytest.fixture
def created_car(qauto_api):
    # Создаём машину перед запуском тестов
    response = qauto_api.cars.create_car()

    created_car_data = response.json()["data"]

    # Передаём данные созданной машины тестам
    yield created_car_data

    # Удаляем тестовую машину после завершения теста
    qauto_api.cars.delete_car(
        created_car_data["id"],
    )


@pytest.fixture
def created_expense(qauto_api, created_car):
    # Создаём расход для тестовой машины
    response = qauto_api.expenses.create_expense(
        created_car["id"],
    )

    created_expense_data = response.json()["data"]

    # Передаём данные расхода тестам
    yield created_expense_data

    # Проверяем, существует ли расход после теста
    get_response = qauto_api.expenses.get_expense(
        created_expense_data["id"],
    )

    # Удаляем расход, только если тест сам его не удалил
    if get_response.status_code == 200:
        qauto_api.expenses.delete_expense(
            created_expense_data["id"],
        )
