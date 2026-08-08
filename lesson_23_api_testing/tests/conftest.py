import pytest

from lesson_23_api_testing.api.qauto_api import QAutoAPI


@pytest.fixture(scope="session")
def qauto_api():
    # Создаём API-клиент с общей HTTP-сессией
    api = QAutoAPI()

    # Авторизуем тестового пользователя
    response = api.sign_in()

    # Проверяем успешность авторизации
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

    # Передаём авторизованный API-клиент тестам
    yield api

    # Завершаем пользовательскую сессию после всех тестов
    api.session.get(f"{api.base_url}/auth/logout")
    api.session.close()


@pytest.fixture
def created_car(qauto_api):
    # Создаём машину перед запуском тестов
    response = qauto_api.create_car()

    assert response.status_code == 201
    assert response.json()["status"] == "ok"

    created_car_data = response.json()["data"]

    # Передаём данные созданной машины тестам
    yield created_car_data

    # Удаляем тестовую машину после завершения всех тестов
    delete_response = qauto_api.delete_car(created_car_data["id"])

    assert delete_response.status_code == 200
    assert delete_response.json()["status"] == "ok"


@pytest.fixture
def created_expense(qauto_api, created_car):
    # Создаём расход для тестовой машины
    response = qauto_api.create_expense(created_car["id"])

    assert response.status_code == 200
    assert response.json()["status"] == "ok"

    created_expense_data = response.json()["data"]

    # Передаём данные расхода тестам
    yield created_expense_data

    # Проверяем, существует ли расход после теста
    get_response = qauto_api.get_expense(created_expense_data["id"])

    # Удаляем расход, только если тест сам его не удалил
    if get_response.status_code == 200:
        delete_response = qauto_api.delete_expense(
            created_expense_data["id"],
        )

        assert delete_response.status_code == 200
        assert delete_response.json()["status"] == "ok"
