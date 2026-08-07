from pathlib import Path

import pytest

from lesson_18_requests import app as app_module


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Используем временную папку вместо настоящей папки uploads
    monkeypatch.setattr(app_module, "upload_directory", str(tmp_path))
    app_module.app.config["TESTING"] = True

    # Создаём тестовый клиент Flask без запуска сервера
    with app_module.app.test_client() as test_client:
        yield test_client


@pytest.fixture
def image_data():
    # Указываем путь к изображению, которое будем загружать в тестах
    image_path = Path("lesson_18_requests/mars_photo1.jpg")

    with image_path.open("rb") as image_file:
        yield {
            "image": (image_file, "test_image.jpg")
        }


@pytest.fixture
def uploaded_image(client, image_data):
    # Загружаем изображение перед выполнением теста
    response = client.post(
        "/upload",
        data=image_data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 201

    filename = "test_image.jpg"
    yield filename

    # Удаляем тестовое изображение, если тест сам его не удалил
    image_path = Path(app_module.upload_directory) / filename

    if image_path.exists():
        image_path.unlink()
