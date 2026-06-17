# Function vs Method

# Функция (Function) — это самостоятельный блок кода, который можно вызвать по имени.
# Метод (Method) — это функция, принадлежащая классу или объекту.
# Проще говоря:
# Функция -> отдельно
# Метод -> внутри класса

# Функция
def greet(name):
    print(f"Hello, {name}")

greet("Roman")
print(type(greet))

# Метод
class Human:

    def say_hello(self):
        print("Hello")

alex = Human()

alex.say_hello()

print(type(alex.say_hello))

# Глобальная функция - это обычная функция, которая не принадлежит классу.
# Ее можно вызвать напрямую по имени.
def deposit_money(self, amount):
    self.balance += amount
    print(f"New balance: {self.balance}$")

# Класс банковского счета
# Здесь мы используем глобальную функцию как метод класса.
class BankAccount:
    deposit = deposit_money

# Создаем объект
# !!! OLD WAY !!!
# Атрибут создается вручную после создания объекта.
# После изучения __init__() лучше так не делать.
account = BankAccount()

# Добавляем объекту баланс
account.balance = 1000

# Вызываем метод deposit()
# На самом деле Python делает примерно так:
# deposit_money(account, 500)
# Поэтому объект account автоматически попадает в параметр self.
account.deposit(500)

# ==========================================
# CORRECT WAY (WITH __init__)
# ==========================================
# Глобальная функция не принадлежит классу.Позже будет использоваться как метод класса.

def add_points(player, points):
    player.score += points
    print(f"{player.nickname} received {points} points")

# Класс игрока
class Player:

    def __init__(self, nickname, score):
        self.nickname = nickname
        self.score = score

    add_score = add_points

# Создаем объект сразу с нужными данными
player = Player("Roman", 100)

print(player.score)

player.add_score(50)

print(player.score)