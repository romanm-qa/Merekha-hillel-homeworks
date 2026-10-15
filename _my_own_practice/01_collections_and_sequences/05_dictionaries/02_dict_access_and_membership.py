# Квадратные скобки возвращают значение по ключу.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("Доступ по ключу:")
print(f"Исходный словарь: {student!r}")
print(f"student['name'] -> {student['name']!r}")
print(f"student['age'] -> {student['age']!r}")

# Если ключа нет, обращение через [] вызывает KeyError.
student = {"name": "Roman", "age": 25}

print("\nОбращение к отсутствующему ключу:")
print(f"Исходный словарь: {student!r}")
try:
    print(student["city"])
except KeyError as error:
    print(f"student['city'] -> {type(error).__name__}: {error}")

# Число в квадратных скобках тоже является ключом, а не индексом.
items = {5: "apple", 0: "banana"}

print("\nЧисловые ключи:")
print(f"Исходный словарь: {items!r}")
print(f"items[0] -> {items[0]!r}")
print(f"items[5] -> {items[5]!r}")

# get(key) возвращает значение по ключу.
# Если ключа нет, возвращает None без KeyError.
student = {"name": "Roman", "age": 25}

print("\nПолучение значения — get():")
print(f"Исходный словарь: {student!r}")
print(f"student.get('name') -> {student.get('name')!r}")
print(f"student.get('city') -> {student.get('city')!r}")

# Второй аргумент get() — результат на случай отсутствующего ключа.
# get() не добавляет отсутствующий ключ в словарь.
student = {"name": "Roman", "age": 25}

print("\nЗначение по умолчанию — get(key, default):")
print(f"Исходный словарь: {student!r}")
print(f"student.get('city', 'Unknown') -> {student.get('city', 'Unknown')!r}")
print(f"student.get('age', 0) -> {student.get('age', 0)!r}")
print(f"Словарь после get(): {student!r}")

# in и not in проверяют наличие ключа, а не значения.
student = {"name": "Roman", "age": 25}

print("\nПроверка наличия ключа — in и not in:")
print(f"Исходный словарь: {student!r}")
print(f"'name' in student -> {'name' in student!r}")
print(f"'city' in student -> {'city' in student!r}")
print(f"'city' not in student -> {'city' not in student!r}")
print(f"'Roman' in student -> {'Roman' in student!r}")

# Для проверки значения используем values().
student = {"name": "Roman", "age": 25}

print("\nПроверка наличия значения:")
print(f"Исходный словарь: {student!r}")
print(f"'Roman' in student.values() -> {'Roman' in student.values()!r}")
print(f"25 in student.values() -> {25 in student.values()!r}")
print(f"'Kyiv' in student.values() -> {'Kyiv' in student.values()!r}")

# Наличие ключа можно проверить перед обращением через [].
student = {"name": "Roman", "age": 25}
key = "city"

print("\nПроверка перед обращением:")
print(f"Исходный словарь: {student!r}")
print(f"Проверяемый ключ: {key!r}")
if key in student:
    print(f"Значение: {student[key]!r}")
else:
    print(f"Ключ {key!r} отсутствует")

# get() возвращает default только при отсутствии ключа.
# Если ключ есть со значением None, результатом будет None.
student = {"name": "Roman", "city": None}

print("\nОтсутствующий ключ и значение None:")
print(f"Исходный словарь: {student!r}")
print(f"student.get('city', 'Unknown') -> {student.get('city', 'Unknown')!r}")
print(f"student.get('country', 'Unknown') -> {student.get('country', 'Unknown')!r}")
print(f"'city' in student -> {'city' in student!r}")
print(f"'country' in student -> {'country' in student!r}")
