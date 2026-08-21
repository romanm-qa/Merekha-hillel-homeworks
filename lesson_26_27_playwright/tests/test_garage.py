from playwright.sync_api import Page, expect


def test_user_login(logged_in_page: Page):
    assert logged_in_page.url.endswith("/panel/garage")


def test_add_car(garage_page):
    garage_page.add_car("BMW", "X5", 1000)

    expect(garage_page.get_car_card("BMW", "X5")).to_be_visible()


def test_update_car_mileage(garage_page):
    garage_page.add_car("BMW", "X5", 1000)

    garage_page.update_mileage("BMW", "X5", 2000)

    assert garage_page.get_car_mileage("BMW", "X5") == 2000


def test_delete_car(garage_page):
    garage_page.add_car("BMW", "X5", 1000)

    garage_page.delete_car("BMW", "X5")

    expect(garage_page.get_car_card("BMW", "X5")).to_be_hidden()
