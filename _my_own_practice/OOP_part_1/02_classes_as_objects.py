# Classes as Objects
#
# В Python все является объектом.
#
# Объекты создаются на основе классов.
#
# Примеры:
#
# 5        -> объект класса int
# "hello"  -> объект класса str
# [1, 2]   -> объект класса list
#
# Пользовательские объекты также создаются на основе классов.
#
# Важно:
# Класс в Python тоже является объектом.
# Все классы создаются специальным классом type.
#
# Иерархия выглядит так:
#
# type
#   ↓
# MyClass
#   ↓
# obj


# Создаем пустой класс

class MyClass:
    pass


# Создаем объект (экземпляр класса)

obj = MyClass()


# Показывает класс объекта

print(type(obj))

# Результат:
# <class '__main__.MyClass'>
# Показывает тип самого класса

print(type(MyClass))

# Результат:
# <class 'type'>


# Сохраняем ссылку на класс

a = MyClass


# Переменная a содержит сам класс,
# а не объект класса

print(type(a))

# Результат:
# <class 'type'>


# Выводим сам класс

print(a)

# Результат:
# <class '__main__.MyClass'>


# Проверяем, является ли obj экземпляром класса MyClass

print(isinstance(obj, a))

# Результат:
# True

# Число является объектом класса int
number = 10

print(isinstance(number, int))
# True


# Строка является объектом класса str
text = "Hello"

print(isinstance(text, str))
# True