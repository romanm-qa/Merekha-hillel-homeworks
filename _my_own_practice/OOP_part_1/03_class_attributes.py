# Class Attributes (атрибуты класса)
#
# Атрибут — это переменная внутри класса.
#
# Атрибуты класса принадлежат самому классу
# и являются общими для всех объектов этого класса.


class User:

    role = "Student"
    academy = "Web Academy"

# Доступ к атрибутам через класс
print(User.role)
print(User.academy)
# Результат:
# Student
# Web Academy


# Создаем объект класса
user_1 = User()
user_2 = User()

# Доступ к атрибутам через объект
print(user_1.role)
print(user_2.academy)
# Результат:
# Student
# Web Academy

# Атрибуты класса можно изменять
User.role = "QA Engineer"

print(User.role)
print(user_1.role)
print(user_2.role)
# QA Engineer
# QA Engineer
# QA Engineer

# Создаем атрибут только для одного объекта
user_1.role = "Python Developer"

print(User.role)
print(user_1.role)
print(user_2.role)
# QA Engineer
# Python Developer
# QA Engineer