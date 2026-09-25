# Кортеж хранит элементы по порядку. В нём могут быть значения разных типов.
numbers = (10, 20, 30, 40, 50)
fruits = ("apple", "banana", "orange")
mixed = (1, "Python", 3.14, True)
empty_tuple = ()

print("Создание кортежей:")
print(f"Кортеж чисел: {numbers!r}")
print(f"Кортеж строк: {fruits!r}")
print(f"Кортеж с разными типами: {mixed!r}")
print(f"Пустой кортеж: {empty_tuple!r}")

# tuple() создаёт пустой кортеж или собирает элементы из итерируемого объекта.
empty_from_tuple = tuple()
numbers_list = [10, 20, 30, 40]
numbers_tuple = tuple(numbers_list)
letters_tuple = tuple("Python")
numbers_from_range = tuple(range(1, 6))

print("\nСоздание с помощью tuple():")
print(f"tuple() -> {empty_from_tuple!r}")
print(f"Исходный список: {numbers_list!r}")
print(f"tuple(numbers_list) -> {numbers_tuple!r}")
print(f"tuple('Python') -> {letters_tuple!r}")
print(f"tuple(range(1, 6)) -> {numbers_from_range!r}")

# Кортеж из одного элемента создаёт запятая, а не круглые скобки.
single_number = (5,)
not_a_tuple = (5)
another_single_number = 10,

print("\nКортеж из одного элемента:")
print(f"(5,) -> {single_number!r}, тип: {type(single_number)!r}")
print(f"(5) -> {not_a_tuple!r}, тип: {type(not_a_tuple)!r}")
print(f"10, -> {another_single_number!r}, тип: {type(another_single_number)!r}")

# Если элементы разделены запятыми, круглые скобки можно опустить.
coordinates = 10, 20
user_data = "Roman", 29, "QA Engineer"

print("\nСоздание без круглых скобок:")
print(f"10, 20 -> {coordinates!r}")
print(f"'Roman', 29, 'QA Engineer' -> {user_data!r}")

# Элементами кортежа могут быть другие кортежи.
route_coordinates = (
    (8, 3),
    (2, 8),
    (3, 4),
)

print("\nВложенные кортежи:")
print(f"Исходный кортеж: {route_coordinates!r}")
print(f"Первый вложенный кортеж: {route_coordinates[0]!r}")
