# Dict comprehension создаёт новый словарь.
# Общая запись: {ключ: значение for элемент in источник}.
numbers = [1, 2, 3, 4]
squares = {number: number ** 2 for number in numbers}

print("Создание словаря — dict comprehension:")
print(f"Исходный список: {numbers!r}")
print(f"Числа и их квадраты: {squares!r}")

# Тот же результат можно получить обычным циклом.
numbers = [1, 2, 3, 4]
squares = {}

print("\nСоздание словаря обычным циклом:")
print(f"Исходный список: {numbers!r}")
for number in numbers:
    squares[number] = number ** 2
print(f"Числа и их квадраты: {squares!r}")

# Ключ и значение можно вычислять из одного элемента.
words = ["cat", "python", "dog"]
word_lengths = {word: len(word) for word in words}

print("\nСлова и их длины:")
print(f"Исходный список: {words!r}")
print(f"Словарь длин: {word_lengths!r}")

# Условие после for фильтрует элементы источника.
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print("\nФильтрация элементов:")
print(f"Исходный список: {numbers!r}")
print(f"Квадраты только чётных чисел: {even_squares!r}")

# Через items() можно преобразовать значения существующего словаря.
# Исходный словарь не меняется.
scores = {"Roman": 80, "Anna": 90, "Alex": 70}
increased_scores = {
    name: score + 5
    for name, score in scores.items()
}

print("\nПреобразование значений:")
print(f"Исходный словарь: {scores!r}")
print(f"Результаты с добавленными 5 баллами: {increased_scores!r}")
print(f"Исходный словарь после преобразования: {scores!r}")

# Можно отбирать пары по их значениям.
scores = {"Roman": 80, "Anna": 90, "Alex": 70}
passed_scores = {
    name: score
    for name, score in scores.items()
    if score >= 80
}

print("\nФильтрация пар словаря:")
print(f"Исходный словарь: {scores!r}")
print(f"Результаты не ниже 80: {passed_scores!r}")

# Можно преобразовывать ключи.
scores = {"Roman": 80, "Anna": 90, "Alex": 70}
lowercase_scores = {
    name.lower(): score
    for name, score in scores.items()
}

print("\nПреобразование ключей:")
print(f"Исходный словарь: {scores!r}")
print(f"Ключи в нижнем регистре: {lowercase_scores!r}")

# if/else перед for выбирает значение для каждой пары.
# В отличие от фильтрации, все элементы источника участвуют в результате.
scores = {"Roman": 80, "Anna": 90, "Alex": 70}
statuses = {
    name: "Passed" if score >= 80 else "Failed"
    for name, score in scores.items()
}

print("\nВыбор значения через if/else:")
print(f"Исходный словарь: {scores!r}")
print(f"Статусы студентов: {statuses!r}")

# Ключи и значения можно поменять местами.
# Новые ключи должны быть хешируемыми.
codes = {"Ukraine": "UA", "Poland": "PL", "Germany": "DE"}
countries = {
    code: country
    for country, code in codes.items()
}

print("\nОбмен ключей и значений:")
print(f"Исходный словарь: {codes!r}")
print(f"Словарь с обратным соответствием: {countries!r}")

# Если получаются одинаковые ключи, остаётся последнее значение.
# При обмене ключей и значений это может привести к потере пар.
scores = {"Roman": 90, "Anna": 90, "Alex": 80}
students_by_score = {
    score: name
    for name, score in scores.items()
}

print("\nСовпадение новых ключей:")
print(f"Исходный словарь: {scores!r}")
print(f"Баллы как ключи: {students_by_score!r}")
print(f"len(scores) -> {len(scores)!r}")
print(f"len(students_by_score) -> {len(students_by_score)!r}")

# zip() позволяет создавать пары из двух источников.
names = ["Roman", "Anna", "Alex"]
scores = [80, 90, 70]
student_scores = {
    name: score
    for name, score in zip(names, scores)
}

print("\nСоздание из двух списков:")
print(f"Исходные имена: {names!r}")
print(f"Исходные баллы: {scores!r}")
print(f"Словарь результатов: {student_scores!r}")
