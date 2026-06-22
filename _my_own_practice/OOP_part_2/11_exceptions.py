# Exceptions (исключения)
# Исключение (Exception) — это ошибка, возникающая во время выполнения программы.
# Исключения позволяют:
# - сообщать о возникновении ошибки
# - не завершать программу аварийно
# - обрабатывать ошибки через try/except
# - создавать собственные типы ошибок
# Основные конструкции:
# - raise       -> вызвать ошибку
# - try/except  -> обработать ошибку
# - finally     -> выполнить код в любом случае
# Можно создавать свои исключения, наследуясь от Exception или его потомков.

try:
    number = int("hello")
except ValueError:
    print("Не удалось преобразовать строку в число")

#--------------------------------------------------------
# Создаем собственный тип ошибки для неверной роли пользователя
class UserRoleError(ValueError):
    def __init__(self, message):
        # Передаем текст ошибки в родительский класс ValueError
        super().__init__(message)
        # Добавляем свой дополнительный атрибут
        self.custom_text = "Invalid role"

try:
    # Создаем объект ошибки и выбрасываем его
    raise UserRoleError("Role does not exist")

except UserRoleError as error:
    # Получаем объект ошибки в переменную error
    print(error)
    # Обращаемся к своему атрибуту объекта ошибки
    print(error.custom_text)

#--------------------------------------------------------------
# Собственный тип ошибки для ситуации, когда на счете недостаточно средств
class FundsError(ValueError):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        # Формируем понятное сообщение об ошибке
        self.message = f"Не хватает денег на счету [{self.account}]. Невозможно снять {self.amount}"

    # Метод для вывода сообщения об ошибке
    def show(self):
        print(self.message)

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        # Если денег недостаточно — выбрасываем нашу ошибку
        if amount > self.balance:
            raise FundsError(account=self.account_number, amount=amount)
        else:
            # Иначе списываем деньги со счета
            self.balance -= amount
            return f"Снято {amount}. Новый баланс - {self.balance}\n"

account = BankAccount(123456, 13000)

try:
    print(account.withdraw(500))
    print(account.withdraw(4000))
    print(account.withdraw(8501))

# Ловим объект ошибки FundsError
except FundsError as error:
    # Вызываем метод объекта ошибки
    error.show()