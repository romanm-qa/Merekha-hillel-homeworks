# Set comprehension создаёт новое множество из элементов коллекции.
numbers = [1, 2, 2, 3, 4]
unique_numbers = {number for number in numbers}

print("Создание множества — set comprehension:")
print(f"Исходный список: {numbers!r}")
print(f"Результат {{number for number in numbers}} -> {unique_numbers!r}")

# Выражение перед for преобразует каждый элемент.
numbers = [1, 2, 3, 4]
squares = {number ** 2 for number in numbers}

print("\nПреобразование элементов:")
print(f"Исходный список: {numbers!r}")
print(f"Квадраты чисел: {squares!r}")

# Условие после for оставляет только подходящие элементы.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = {number for number in numbers if number % 2 == 0}

print("\nФильтрация элементов:")
print(f"Исходный список: {numbers!r}")
print(f"Чётные числа: {even_numbers!r}")

# После преобразования одинаковые результаты остаются в одном экземпляре.
words = ["Cat", "cat", "DOG", "dog"]
lowercase_words = {word.lower() for word in words}

print("\nПреобразование с удалением повторов:")
print(f"Исходный список: {words!r}")
print(f"Слова в нижнем регистре: {lowercase_words!r}")
