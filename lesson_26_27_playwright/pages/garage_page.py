from playwright.sync_api import Page


class GaragePage:
    def __init__(self, page: Page):
        # Сохраняем вкладку браузера для работы со страницей гаража
        self.page = page

        # Локаторы страницы гаража и модальных окон
        self.add_car_button = page.get_by_role("button", name="Add car")
        self.brand_select = page.locator("#addCarBrand")
        self.model_select = page.locator("#addCarModel")
        self.mileage_input = page.locator("#addCarMileage")
        self.add_button = page.get_by_role("button", name="Add", exact=True)
        self.save_button = page.get_by_role("button", name="Save", exact=True)
        self.remove_car_button = page.get_by_role("button", name="Remove car", exact=True)
        self.confirm_remove_button = page.get_by_role("button", name="Remove", exact=True)
        self.cancel_button = page.get_by_role("button", name="Cancel", exact=True)

    def add_car(self, brand: str, model: str, mileage: int):
        self.add_car_button.click()
        self.brand_select.select_option(label=brand)
        self.model_select.select_option(label=model)
        self.mileage_input.fill(str(mileage))
        self.add_button.click()
        self.add_button.wait_for(state="hidden")

    # Находим карточку конкретного автомобиля по марке и модели
    def get_car_card(self, brand: str, model: str):
        car_name = f"{brand} {model}"
        return self.page.locator(".car-item").filter(has_text=car_name)

    # Изменяем пробег конкретного автомобиля
    def update_mileage(self, brand: str, model: str, new_mileage: int):
        car_card = self.get_car_card(brand, model)
        car_card.locator(".car_edit").click()
        self.mileage_input.fill(str(new_mileage))
        self.save_button.click()
        self.save_button.wait_for(state="hidden")

    # Удаляем конкретный автомобиль
    def delete_car(self, brand: str, model: str):
        car_card = self.get_car_card(brand, model).first
        car_card.locator(".car_edit").click()
        self.remove_car_button.click()
        self.confirm_remove_button.click()
        self.confirm_remove_button.wait_for(state="hidden")

    # Получаем текущий пробег конкретного автомобиля
    def get_car_mileage(self, brand: str, model: str) -> int:
        car_card = self.get_car_card(brand, model)
        car_card.locator(".car_edit").click()

        mileage = int(self.mileage_input.input_value())
        self.cancel_button.click()
        self.cancel_button.wait_for(state="hidden")

        return mileage
