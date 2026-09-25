# При распаковке каждому элементу кортежа соответствует переменная.
user_data = ("Roman", 29, "QA Engineer")
name, age, profession = user_data

print("Распаковка кортежа:")
print(f"Исходный кортеж: {user_data!r}")
print(f"name -> {name!r}")
print(f"age -> {age!r}")
print(f"profession -> {profession!r}")

# Если значение не нужно, переменную обычно называют _.
coordinates = (10, 20, 30)
x, _, z = coordinates

print("\nПропуск ненужного значения:")
print(f"Исходный кортеж: {coordinates!r}")
print(f"x -> {x!r}")
print(f"z -> {z!r}")

# Переменная со звёздочкой собирает оставшиеся значения в список.
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers

print("\nРаспаковка со звёздочкой:")
print(f"Исходный кортеж: {numbers!r}")
print(f"first -> {first!r}")
print(f"middle -> {middle!r}")
print(f"last -> {last!r}")
print(f"type(middle) -> {type(middle)!r}")

# Вложенный кортеж тоже можно распаковать за один раз.
person = ("Roman", (29, "QA Engineer"))
name, (age, profession) = person

print("\nРаспаковка вложенного кортежа:")
print(f"Исходный кортеж: {person!r}")
print(f"name -> {name!r}")
print(f"age -> {age!r}")
print(f"profession -> {profession!r}")

# На каждом шаге цикла один кортеж распаковывается в переменные.
users = (
    ("Roman", 29),
    ("Anna", 25),
)

print("\nРаспаковка в цикле:")
print(f"Исходные данные: {users!r}")
for name, age in users:
    print(f"name -> {name!r}, age -> {age!r}")

# Звёздочка позволяет обработать кортежи с разным количеством элементов.
users_with_details = (
    ("Roman", 29, "QA Engineer"),
    ("Anna", 25),
)

print("\nКортежи разной длины:")
print(f"Исходные данные: {users_with_details!r}")
for name, *details in users_with_details:
    print(f"name -> {name!r}, details -> {details!r}")

# zip() соединяет элементы по одинаковым позициям.
# Обычный zip() останавливается на самой короткой последовательности.
names = ("Roman", "Anna", "Oleg")
ages = (29, 25)

print("\nРаспаковка результатов zip():")
print(f"Имена: {names!r}")
print(f"Возраст: {ages!r}")
for name, age in zip(names, ages):
    print(f"name -> {name!r}, age -> {age!r}")

# Без звёздочки количество переменных должно совпадать с количеством элементов.
values = (10, 20, 30)

print("\nНесовпадение количества элементов:")
print(f"Исходный кортеж: {values!r}")

try:
    first, second = values
except ValueError as error:
    print(f"first, second = values -> {type(error).__name__}: {error}")
