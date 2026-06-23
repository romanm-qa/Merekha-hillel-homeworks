"""
Створіть абстрактний клас "Фігура" з абстрактними методами
для отримання площі та периметру.

Наслідуйте від нього декілька (> 2) інших фігур та реалізуйте
математично вірні для них методи для площі та периметру.

Властивості по типу "довжина сторони", "радіус" і т.д.
повинні бути приватними та ініціалізуватись через конструктор.

Створіть декілька різних об'єктів фігур та у циклі
порахуйте і виведіть у консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod
import math

# Abstract class for all shapes
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return 4 * self.__side

# Create shape objects
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Square(4),
]

# Calculate and print area and perimeter for each shape
for shape in shapes:
    print(
        f"{shape.__class__.__name__}:"
        f" Area = {shape.get_area():.2f}, "
        f"Perimeter = {shape.get_perimeter():.2f}"
    )