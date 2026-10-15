# Если ключа нет, присваивание добавляет новую пару.
# Если ключ есть, заменяет его значение.
student = {"name": "Roman", "age": 25}

print("Добавление и изменение через []:")
print(f"Исходный словарь: {student!r}")
student["city"] = "Kyiv"
print(f"После student['city'] = 'Kyiv': {student!r}")
student["age"] = 26
print(f"После student['age'] = 26: {student!r}")

# update() добавляет новые пары и заменяет значения существующих ключей.
# Изменяет исходный словарь и возвращает None.
student = {"name": "Roman", "age": 25}
updates = {"age": 26, "city": "Kyiv"}

print("\nОбновление из другого словаря — update():")
print(f"Исходный словарь: {student!r}")
print(f"Добавляемые данные: {updates!r}")
result = student.update(updates)
print(f"После student.update(updates): {student!r}")
print(f"Результат update(): {result!r}")

# update() также принимает именованные аргументы.
student = {"name": "Roman", "age": 25}

print("\nОбновление через именованные аргументы:")
print(f"Исходный словарь: {student!r}")
student.update(age=26, city="Kyiv")
print(f"После student.update(age=26, city='Kyiv'): {student!r}")

# update() также принимает итерируемый объект с парами ключ–значение.
student = {"name": "Roman", "age": 25}
updates = [("age", 26), ("city", "Kyiv")]

print("\nОбновление из списка пар:")
print(f"Исходный словарь: {student!r}")
print(f"Добавляемые пары: {updates!r}")
student.update(updates)
print(f"После student.update(updates): {student!r}")

# setdefault() возвращает значение существующего ключа, не заменяя его.
# Если ключа нет, добавляет его с указанным значением и возвращает это значение.
student = {"name": "Roman", "age": 25}

print("\nДобавление только отсутствующего ключа — setdefault():")
print(f"Исходный словарь: {student!r}")
age = student.setdefault("age", 0)
print(f"student.setdefault('age', 0) -> {age!r}")
print(f"Словарь после проверки существующего ключа: {student!r}")
city = student.setdefault("city", "Kyiv")
print(f"student.setdefault('city', 'Kyiv') -> {city!r}")
print(f"Словарь после добавления нового ключа: {student!r}")

# Если значение по умолчанию не указано, setdefault() использует None.
student = {"name": "Roman"}

print("\nsetdefault() без значения по умолчанию:")
print(f"Исходный словарь: {student!r}")
phone = student.setdefault("phone")
print(f"student.setdefault('phone') -> {phone!r}")
print(f"Словарь после setdefault(): {student!r}")

# pop(key) удаляет пару по ключу и возвращает её значение.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nУдаление с получением значения — pop():")
print(f"Исходный словарь: {student!r}")
removed_city = student.pop("city")
print(f"student.pop('city') -> {removed_city!r}")
print(f"Словарь после pop(): {student!r}")

# Если ключа нет и default не указан, pop() вызывает KeyError.
student = {"name": "Roman", "age": 25}

print("\nУдаление отсутствующего ключа — pop():")
print(f"Исходный словарь: {student!r}")
try:
    student.pop("city")
except KeyError as error:
    print(f"student.pop('city') -> {type(error).__name__}: {error}")

# Второй аргумент pop() возвращается, если ключа нет.
# В этом случае словарь не меняется.
student = {"name": "Roman", "age": 25}

print("\nУдаление без KeyError — pop(key, default):")
print(f"Исходный словарь: {student!r}")
removed_city = student.pop("city", "Unknown")
print(f"student.pop('city', 'Unknown') -> {removed_city!r}")
print(f"Словарь после pop(): {student!r}")

# popitem() удаляет последнюю добавленную пару.
# Возвращает кортеж (ключ, значение).
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nУдаление последней добавленной пары — popitem():")
print(f"Исходный словарь: {student!r}")
removed_pair = student.popitem()
print(f"student.popitem() -> {removed_pair!r}")
print(f"Словарь после popitem(): {student!r}")

# Для пустого словаря popitem() вызывает KeyError.
student = {}

print("\npopitem() для пустого словаря:")
print(f"Исходный словарь: {student!r}")
try:
    student.popitem()
except KeyError as error:
    print(f"student.popitem() -> {type(error).__name__}: {error}")

# del удаляет пару по ключу, не возвращая значение.
# Это инструкция Python, а не метод словаря.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nУдаление по ключу — del:")
print(f"Исходный словарь: {student!r}")
del student["city"]
print(f"После del student['city']: {student!r}")

# Если ключа нет, del вызывает KeyError.
print("\nУдаление отсутствующего ключа — del:")
print(f"Исходный словарь: {student!r}")
try:
    del student["city"]
except KeyError as error:
    print(f"del student['city'] -> {type(error).__name__}: {error}")

# clear() удаляет все пары, но сам словарь остаётся.
# Возвращает None.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nОчистка словаря — clear():")
print(f"Исходный словарь: {student!r}")
result = student.clear()
print(f"Словарь после clear(): {student!r}")
print(f"Результат clear(): {result!r}")
