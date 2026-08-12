import pytest


@pytest.mark.api
@pytest.mark.positive
def test_get_all_expenses(qauto_api):
    # Отправляем запрос на получение всех расходов
    response = qauto_api.expenses.get_expenses()
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["status"] == "ok"
    assert isinstance(response_data["data"], list)


@pytest.mark.api
@pytest.mark.positive
def test_create_expense(created_expense, created_car):
    # Проверяем данные созданного расхода
    assert created_expense["id"] is not None
    assert created_expense["carId"] == created_car["id"]
    assert created_expense["mileage"] == 1100
    assert created_expense["liters"] == 20
    assert created_expense["totalCost"] == 100


@pytest.mark.api
@pytest.mark.positive
def test_get_expense_by_id(qauto_api, created_expense):
    # Получаем созданный расход по его ID
    response = qauto_api.expenses.get_expense(created_expense["id"])
    response_data = response.json()

    # Проверяем статус и данные расхода
    assert response.status_code == 200
    assert response_data["status"] == "ok"
    assert response_data["data"]["id"] == created_expense["id"]
    assert response_data["data"]["carId"] == created_expense["carId"]


@pytest.mark.api
@pytest.mark.positive
def test_update_expense(qauto_api, created_expense, created_car):
    # Изменяем данные созданного расхода
    response = qauto_api.expenses.update_expense(
        expense_id=created_expense["id"],
        car_id=created_car["id"],
    )
    response_data = response.json()

    # Проверяем ответ на PUT-запрос
    assert response.status_code == 200
    assert response_data["status"] == "ok"
    assert response_data["data"]["mileage"] == 1200
    assert response_data["data"]["liters"] == 25
    assert response_data["data"]["totalCost"] == 150

    # Повторно получаем расход и проверяем сохранение изменений
    get_response = qauto_api.expenses.get_expense(created_expense["id"])
    updated_expense = get_response.json()["data"]

    assert get_response.status_code == 200
    assert updated_expense["mileage"] == 1200
    assert updated_expense["liters"] == 25
    assert updated_expense["totalCost"] == 150


@pytest.mark.api
@pytest.mark.positive
def test_delete_expense(qauto_api, created_expense):
    expense_id = created_expense["id"]

    # Удаляем созданный расход
    response = qauto_api.expenses.delete_expense(expense_id)

    assert response.status_code == 200
    assert response.json()["status"] == "ok"

    # Проверяем, что удалённый расход больше недоступен
    get_response = qauto_api.expenses.get_expense(expense_id)

    assert get_response.status_code == 404
