from copy import deepcopy

# Присваивание не создаёт копию: обе переменные ссылаются на один словарь.
student = {"name": "Roman", "age": 25}
alias = student

print("Присваивание без копирования:")
print(f"Исходный словарь: {student!r}")
print(f"alias is student -> {alias is student!r}")
alias["age"] = 26
print(f"После alias['age'] = 26:")
print(f"student -> {student!r}")
print(f"alias -> {alias!r}")

# copy() создаёт новый словарь с теми же ключами и значениями.
student = {"name": "Roman", "age": 25}
copied = student.copy()

print("\nКопирование — copy():")
print(f"Исходный словарь: {student!r}")
print(f"Копия: {copied!r}")
print(f"copied == student -> {copied == student!r}")
print(f"copied is student -> {copied is student!r}")
copied["age"] = 26
print(f"После copied['age'] = 26:")
print(f"student -> {student!r}")
print(f"copied -> {copied!r}")

# dict(existing_dict) тоже создаёт поверхностную копию.
student = {"name": "Roman", "age": 25}
copied = dict(student)

print("\nКопирование — dict():")
print(f"Исходный словарь: {student!r}")
print(f"dict(student) -> {copied!r}")
print(f"copied is student -> {copied is student!r}")

# Поверхностная копия не копирует вложенные объекты.
# Вложенный список остаётся общим для исходного словаря и копии.
student = {"name": "Roman", "courses": ["Python", "SQL"]}
copied = student.copy()

print("\nПоверхностная копия и вложенный список:")
print(f"Исходный словарь: {student!r}")
print(f"Копия: {copied!r}")
print(f"copied is student -> {copied is student!r}")
print(
    f"copied['courses'] is student['courses'] -> "
    f"{copied['courses'] is student['courses']!r}"
)
copied["courses"].append("Git")
print(f"После copied['courses'].append('Git'):")
print(f"student -> {student!r}")
print(f"copied -> {copied!r}")

# Замена значения в копии не меняет значение исходного словаря.
student = {"name": "Roman", "courses": ["Python", "SQL"]}
copied = student.copy()

print("\nЗамена вложенного списка в копии:")
print(f"Исходный словарь: {student!r}")
print(f"Копия: {copied!r}")
copied["courses"] = ["Docker"]
print(f"После copied['courses'] = ['Docker']:")
print(f"student -> {student!r}")
print(f"copied -> {copied!r}")

# deepcopy() рекурсивно копирует вложенные коллекции.
student = {"name": "Roman", "courses": ["Python", "SQL"]}
copied = deepcopy(student)

print("\nГлубокое копирование — deepcopy():")
print(f"Исходный словарь: {student!r}")
print(f"Глубокая копия: {copied!r}")
print(
    f"copied['courses'] is student['courses'] -> "
    f"{copied['courses'] is student['courses']!r}"
)
copied["courses"].append("Git")
print(f"После copied['courses'].append('Git'):")
print(f"student -> {student!r}")
print(f"copied -> {copied!r}")

# Оператор | создаёт новый объединённый словарь.
# При совпадении ключей используется значение из правого словаря.
left = {"name": "Roman", "age": 25}
right = {"age": 26, "city": "Kyiv"}

print("\nОбъединение в новый словарь — |:")
print(f"Левый словарь: {left!r}")
print(f"Правый словарь: {right!r}")
merged = left | right
print(f"left | right -> {merged!r}")
print(f"Левый словарь после объединения: {left!r}")
print(f"Правый словарь после объединения: {right!r}")

# Порядок словарей влияет на значение совпадающего ключа.
left = {"name": "Roman", "age": 25}
right = {"age": 26, "city": "Kyiv"}

print("\nПорядок словарей при объединении:")
print(f"Левый словарь: {left!r}")
print(f"Правый словарь: {right!r}")
print(f"left | right -> {left | right!r}")
print(f"right | left -> {right | left!r}")

# Оператор |= изменяет существующий словарь.
left = {"name": "Roman", "age": 25}
right = {"age": 26, "city": "Kyiv"}

print("\nОбъединение с изменением исходного словаря — |=:")
print(f"Исходный словарь: {left!r}")
print(f"Добавляемый словарь: {right!r}")
left |= right
print(f"После left |= right: {left!r}")

# Распаковка ** тоже создаёт новый объединённый словарь.
# При совпадении ключей побеждает значение, указанное позже.
left = {"name": "Roman", "age": 25}
right = {"age": 26, "city": "Kyiv"}

print("\nОбъединение через распаковку — **:")
print(f"Левый словарь: {left!r}")
print(f"Правый словарь: {right!r}")
merged = {**left, **right}
print(f"{{**left, **right}} -> {merged!r}")

# update() изменяет исходный словарь и возвращает None.
left = {"name": "Roman", "age": 25}
right = {"age": 26, "city": "Kyiv"}

print("\nОбъединение через update():")
print(f"Исходный словарь: {left!r}")
print(f"Добавляемый словарь: {right!r}")
result = left.update(right)
print(f"После left.update(right): {left!r}")
print(f"Результат update(): {result!r}")
