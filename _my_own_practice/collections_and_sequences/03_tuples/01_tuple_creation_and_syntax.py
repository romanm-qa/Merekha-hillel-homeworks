# =========================================
# СОЗДАНИЕ КОРТЕЖА (Tuple Creation)
# =========================================

numbers = (10, 20, 30, 40, 50)
print(numbers)
print(type(numbers))

fruits = ("apple", "banana", "orange")
print(fruits)

mixed = (1, "Python", 3.14, True)
print(mixed)

empty_tuple = ()
print(empty_tuple)

print(30 * "-")

# =========================================
# СОЗДАНИЕ С ПОМОЩЬЮ tuple()
# =========================================

empty_tuple = tuple()

print(empty_tuple)
print(type(empty_tuple))

print(30 * "-")

# =========================================
# КОРТЕЖ ИЗ ОДНОГО ЭЛЕМЕНТА
# =========================================

single_number = (5,)
print(single_number)
print(type(single_number))

not_a_tuple = (5)
print(not_a_tuple)
print(type(not_a_tuple))

# Кортеж определяет запятая, а не круглые скобки
another_single_number = 10,
print(another_single_number)
print(type(another_single_number))

print(30 * "-")

# =========================================
# СОЗДАНИЕ БЕЗ КРУГЛЫХ СКОБОК
# =========================================

coordinates = 10, 20
print(coordinates)
print(type(coordinates))

user_data = "Roman", 29, "QA Engineer"
print(user_data)

print(30 * "-")

# =========================================
# ВЛОЖЕННЫЕ КОРТЕЖИ (Nested Tuples)
# =========================================

route_coordinates = (
    (8, 3),
    (2, 8),
    (3, 4),
)

print(route_coordinates)

print(30 * "-")

# =========================================
# ПРЕОБРАЗОВАНИЕ В КОРТЕЖ (Tuple Conversion)
# =========================================

numbers_list = [10, 20, 30, 40]
numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
print(type(numbers_tuple))

letters_tuple = tuple("Python")
print(letters_tuple)

numbers_from_range = tuple(range(1, 6))
print(numbers_from_range)

print(30 * "-")
