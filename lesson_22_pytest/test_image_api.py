import pytest


@pytest.mark.positive
@pytest.mark.smoke
def test_upload_image(client, image_data):
    # Отправляем изображение на сервер
    response = client.post(
        "/upload",
        data=image_data,
        content_type="multipart/form-data",
    )
    # Проверяем успешную загрузку изображения
    assert response.status_code == 201

    # Проверяем ссылку на загруженное изображение в ответе
    response_data = response.get_json()
    assert response_data["image_url"].endswith("/uploads/test_image.jpg")


@pytest.mark.positive
@pytest.mark.smoke
def test_get_image(client, uploaded_image):
    filename = uploaded_image

    # Запрашиваем ранее загруженное изображение
    response = client.get(
        f"/image/{filename}",
        headers={"Content-Type": "image"}
    )
    # Проверяем успешное получение изображения
    assert response.status_code == 200
    # Проверяем тип полученного файла
    assert response.content_type == "image/jpeg"


@pytest.mark.positive
@pytest.mark.regression
def test_get_image_url(client, uploaded_image):
    filename = uploaded_image

    # Запрашиваем ссылку на ранее загруженное изображение
    response = client.get(
        f"/image/{filename}",
        headers={"Content-Type": "text"}
    )
    # Проверяем успешное получение ссылки
    assert response.status_code == 200

    # Проверяем ссылку на нужное изображение в ответе
    response_data = response.get_json()
    assert response_data["image_url"].endswith(f"/uploads/{filename}")


@pytest.mark.positive
@pytest.mark.smoke
def test_delete_image(client, uploaded_image):
    filename = uploaded_image

    # Удаляем ранее загруженное изображение
    response = client.delete(f"/delete/{filename}")
    # Проверяем успешное удаление
    assert response.status_code == 200

    # Пытаемся получить удалённое изображение
    get_response = client.get(
        f"/image/{filename}",
        headers={"Content-Type": "image"}
    )
    # Проверяем, что изображение больше не существует
    assert get_response.status_code == 404


@pytest.mark.negative
@pytest.mark.regression
def test_delete_nonexistent_image(client):
    # Пытаемся удалить несуществующее изображение
    response = client.delete("/delete/nonexistent.jpg")

    # Проверяем статус ошибки
    assert response.status_code == 404

    # Проверяем сообщение об отсутствующем изображении
    response_data = response.get_json()
    assert response_data["error"] == "Image not found"


@pytest.mark.negative
@pytest.mark.regression
def test_upload_without_image(client):
    # Отправляем запрос на загрузку без изображения
    response = client.post(
        "/upload",
        data={},
        content_type="multipart/form-data"
    )
    # Проверяем статус некорректного запроса
    assert response.status_code == 400

    # Проверяем сообщение об отсутствующем изображении
    response_data = response.get_json()
    assert response_data["error"] == "No image provided"


@pytest.mark.negative
@pytest.mark.regression
def test_get_nonexistent_image(client):
    # Пытаемся получить несуществующее изображение
    response = client.get(
        "/image/nonexistent.jpg",
        headers={"Content-Type": "image"}
    )
    # Проверяем статус отсутствующего ресурса
    assert response.status_code == 404

    # Проверяем сообщение об отсутствующем изображении
    response_data = response.get_json()
    assert response_data["error"] == "Image not found"


@pytest.mark.negative
@pytest.mark.regression
def test_get_image_with_unsupported_content_type(client, uploaded_image):
    filename = uploaded_image

    # Запрашиваем изображение с неподдерживаемым Content-Type
    response = client.get(
        f"/image/{filename}",
        headers={"Content-Type": "application/json"}
    )
    # Проверяем статус некорректного запроса
    assert response.status_code == 400

    # Проверяем сообщение о неподдерживаемом Content-Type
    response_data = response.get_json()
    assert response_data["error"] == "Unsupported Content-Type"
