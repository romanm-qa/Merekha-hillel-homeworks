# Способ №1
# Обращаемся к атрибутам объекта напрямую

class Car:

    def __init__(self, brand, year, engine_volume):
        self.brand = brand
        self.year = year
        self.engine_volume = engine_volume


car = Car("Toyota", 2021, 1.6)

print(car.brand)
print(car.year)
print(car.engine_volume)

# Способ №2
# Метод сам выводит информацию
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print(
            f"{self.name} is {self.age} years old "
            f"and studies {self.course}"
        )

student = Student("Roman", 29, "Python")

student.show_info()

# Способ №3
# Метод возвращает строку
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return (
            f"'{self.title}' by {self.author}, "
            f"{self.pages} pages"
        )


book = Book("Clean Code", "Robert Martin", 464)

print(book.get_info())