from lesson_23_api_testing.api.cars_api import CarsAPI
from lesson_23_api_testing.api.expenses_api import ExpensesAPI
from lesson_23_api_testing.api.qauto_session import QAutoSession


class QAutoAPI:
    def __init__(self):
        # Создаём общую сессию для всех API-клиентов
        self.session = QAutoSession()

        # Передаём одну сессию классам для работы с машинами и расходами
        self.cars = CarsAPI(
            self.session.session,
            self.session.base_url,
        )
        self.expenses = ExpensesAPI(
            self.session.session,
            self.session.base_url,
        )
