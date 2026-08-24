from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page, base_url: str):
        # Сохраняем вкладку браузера и адрес сайта
        self.page = page
        self.base_url = base_url

        # Локаторы формы авторизации
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto(self.base_url)

    def login(self, email: str, password: str):
        self.sign_in_button.click()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
