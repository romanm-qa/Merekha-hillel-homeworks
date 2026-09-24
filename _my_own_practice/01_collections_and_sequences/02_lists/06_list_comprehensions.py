# List comprehension создаёт новый список из итерируемого объекта.
# Сначала сравним обычный цикл и краткую запись на одной задаче.
source_numbers = list(range(15))
odd_numbers_with_loop = []

for number in source_numbers:
    if number % 2 == 1:
        odd_numbers_with_loop.append(number)

print("Создание списка через цикл for:")
print(f"Исходный список: {source_numbers!r}")
print(f"Нечётные числа: {odd_numbers_with_loop!r}")

# Общая форма: [выражение for элемент in коллекция if условие].
# Часть if в конце оставляет только элементы, которые подходят под условие.
odd_numbers = [number for number in source_numbers if number % 2 == 1]

print("\nТот же результат — list comprehension:")
print(f"Исходный список: {source_numbers!r}")
print(f"[number for number in source_numbers if number % 2 == 1] -> {odd_numbers!r}")
print(f"Исходный список после создания нового: {source_numbers!r}")

# Без if в конце новый список содержит результат выражения для каждого элемента.
numbers = [1, 2, 3, 4]
squares = [number ** 2 for number in numbers]

print("\nПреобразование каждого элемента:")
print(f"Исходный список: {numbers!r}")
print(f"[number ** 2 for number in numbers] -> {squares!r}")

# Условие в конце фильтрует элементы: в список попадут только чётные числа.
even_numbers = [number for number in numbers if number % 2 == 0]

print("\nФильтрация элементов:")
print(f"Исходный список: {numbers!r}")
print(f"[number for number in numbers if number % 2 == 0] -> {even_numbers!r}")

# if/else перед for выбирает значение для каждого элемента, а не отбрасывает его.
labels = ["чётное" if number % 2 == 0 else "нечётное" for number in numbers]

print("\nВыбор значения для каждого элемента — if/else:")
print(f"Исходный список: {numbers!r}")
print(f"Метки чётности: {labels!r}")
print(f"Количество элементов до и после: {len(numbers)} -> {len(labels)}")
