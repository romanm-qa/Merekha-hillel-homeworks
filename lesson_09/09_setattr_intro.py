# __setattr__ (магический метод)
#
# ВНИМАНИЕ:
# ЭТО НЕ ДОМАШКА.
# ЭТО МОЯ ЛИЧНАЯ ПРАКТИКА ДЛЯ ПОНИМАНИЯ,
# КАК РАБОТАЕТ __setattr__.
# __setattr__ (магический метод)

class User:

    def __setattr__(self, key, value):
        print(f"Устанавливаем атрибут: {key} = {value}")

        super().__setattr__(key, value)


user = User()

user.name = "Roman"
user.age = 29

# другой пример---- __setattr__
# Обычно используется для:
# - проверки данных перед сохранением;
# - автоматического изменения связанных атрибутов;
# - запрета некорректных значений.
class Car:

    def __init__(self, brand, year):

        self.brand = brand
        self.year = year

    def __setattr__(self, key, value):

        # Не позволяем указать год раньше появления автомобиля
        if key == "year" and value < 1886:
            raise ValueError("Car year cannot be less than 1886")

        super().__setattr__(key, value)


car = Car("Toyota", 2021)

print(car.brand)
print(car.year)

# Попытка записать некорректный год
car.year = 1885

# Что происходит под капотом:
#
# car.year = 2021
#
# ↓
#
# car.__setattr__("year", 2021)
#
# ↓
#
# super().__setattr__("year", 2021)
#
# ↓
#
# Атрибут сохраняется в объекте