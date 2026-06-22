# Абстрактные классы (Abstract Classes)
# Абстрактный класс — это класс-шаблон.
# Его задача:
# - описать общую структуру для дочерних классов;
# - заставить дочерние классы реализовать нужные методы.
# Обычно объект абстрактного класса создавать нельзя.
# Абстрактный класс отвечает на вопрос:
# "Что обязаны уметь все наследники?"
# Например:
# Animal
# ├── Cat
# ├── Dog
# └── Bird
# Все животные должны уметь издавать звук, но для каждого животного реализация будет своей.

from abc import ABC, abstractmethod
from math import pi

PI = pi

# Абстрактный класс Shape.
# От него нельзя создавать объекты напрямую.
class Shape(ABC):
    def __init__(self, side):
        self.side = side

    # Каждый наследник обязан реализовать perimeter()
    @abstractmethod
    def perimeter(self):
        pass

    # Каждый наследник обязан реализовать area()
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def perimeter(self):
        return 2 * PI * self.side

    def area(self):
        return PI * self.side ** 2

class Square(Shape):
    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

circle1 = Circle(2)
square1 = Square(5)

print("Circle perimeter = ", circle1.perimeter())
print("Circle area = ", circle1.area())
print("*" * 35)
print("Square perimeter = ", square1.perimeter())
print("Square area = ", square1.area())

# Shape задает "контракт".
# Любая фигура должна иметь:
# - perimeter()
# - area()
# Как именно они будут работать —
# решает каждый дочерний класс самостоятельно.