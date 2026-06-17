# Constructor (__init__)
#
# __init__() — специальный метод класса.
#
# Он автоматически вызывается при создании объекта.
#
# Основная задача __init__():
# создавать и инициализировать атрибуты объекта.
#
# Без __init__():
#
# alex = Human()
# alex.name = "Alex"
# alex.age = 30
#
# С __init__():
#
# alex = Human("Alex", 30)
#
# Все необходимые атрибуты создаются автоматически.

# __init__() автоматически вызывается при созданении объекта
class Animal:

    def __init__(self):
        print("Constructor (__init__) called")


cat = Animal()

#----------------------------------------------------------------
class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        return (
            f"My name is {self.name}. "
            f"I am {self.age} years old. "
            f"I am {self.gender}."
        )

student = Human("Roman", 29, "M")
teacher = Human("Ignat", 40, "M")
director = Human("Tanya", 55, "F")

print(director.show_info())

# Создать класс Birds.
#
# При созданении объекта необходимо передавать:
# - race
# - age
#
# Если возраст меньше 3 лет,
# необходимо выбросить исключение ValueError.
class Bird:

    def __init__(self, race, age):
        if age < 3:
            raise ValueError("Bird age cannot be less than 3 years")

        self.race = race
        self.age = age

titmouse = Bird("titmouse", 2)

print(titmouse.age)

# Methods (методы класса)
#
# Метод может:
# 1. Использовать атрибуты объекта.
# 2. Изменять атрибуты объекта.
# 3. Выполнять определенную логику.