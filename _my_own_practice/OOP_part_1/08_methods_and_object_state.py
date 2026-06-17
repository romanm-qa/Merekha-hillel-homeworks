# Методы могут принимать дополнительные параметры.
# self - текущий объект
# amount - значение, которое передается при вызове метода
# employee.increase_salary(1000)
# self автоматически получает объект employee
# amount получает значение 1000
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Employee name: {self.name}, salary: {self.salary}$")

    def increase_salary(self, amount):
        self.salary += amount
        print(f"Salary increased by {amount}$")

employee = Employee("Roman", 3500)

employee.show_info()
employee.increase_salary(1000)
employee.show_info()

# Private Attributes (приватные атрибуты)

class User:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password


user = User("Roman", "123456")

print(user.username)

# print(user.__password)  # Ошибка

print(user.get_password())