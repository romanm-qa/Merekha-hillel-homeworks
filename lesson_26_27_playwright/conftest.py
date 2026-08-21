import os
import pytest

from dotenv import load_dotenv
from playwright.sync_api import Page

from lesson_26_27_playwright.pages.login_page import LoginPage
from lesson_26_27_playwright.pages.garage_page import GaragePage

load_dotenv()

# Настройки окружения и данные для авторизации
QAUTO_UI_URL = os.getenv("QAUTO_UI_URL")
BASIC_AUTH_LOGIN = os.getenv("BASIC_AUTH_LOGIN")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")


# Передаём данные Basic Auth при создании контекста браузера
@pytest.fixture
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "http_credentials": {
            "username": BASIC_AUTH_LOGIN,
            "password": BASIC_AUTH_PASSWORD,
        },
    }


# Открываем сайт и авторизуем тестового пользователя через UI
@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page, QAUTO_UI_URL)
    login_page.open()
    login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    page.wait_for_url("**/panel/garage")
    return page


@pytest.fixture
def garage_page(logged_in_page: Page):
    garage = GaragePage(logged_in_page)

    yield garage

    # Удаляем все тестовые автомобили, оставшиеся после теста
    while garage.get_car_card("BMW", "X5").count() > 0:
        garage.delete_car("BMW", "X5")
