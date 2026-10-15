# Словарь хранит пары ключ: значение.
# dict изменяем и сохраняет порядок добавления ключей.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("Создание словаря:")
print(f"Исходный словарь: {student!r}")
print(f"type(student) -> {type(student)!r}")
print(f"len(student) -> {len(student)!r}")

# Пустой словарь можно создать через {} или dict().
empty_braces = {}
empty_dict = dict()

print("\nПустой словарь:")
print(f"{{}} -> {empty_braces!r}")
print(f"dict() -> {empty_dict!r}")
print(f"type(empty_braces) -> {type(empty_braces)!r}")
print(f"len(empty_dict) -> {len(empty_dict)!r}")

# dict() может создавать словарь из именованных аргументов.
# Имена аргументов становятся строковыми ключами.
student = dict(name="Roman", age=25, city="Kyiv")

print("\nСоздание через dict() — именованные аргументы:")
print(f"dict(name='Roman', age=25, city='Kyiv') -> {student!r}")

# dict() также принимает итерируемый объект с парами ключ–значение.
pairs = [("name", "Roman"), ("age", 25), ("city", "Kyiv")]
student = dict(pairs)

print("\nСоздание словаря из пар:")
print(f"Исходный список пар: {pairs!r}")
print(f"dict(pairs) -> {student!r}")

# zip() объединяет ключи и значения в пары.
# Если длины различаются, обычный zip() остановится на коротком источнике.
keys = ["name", "age", "city"]
values = ["Roman", 25, "Kyiv"]
student = dict(zip(keys, values))

print("\nСоздание из ключей и значений — dict(zip()):")
print(f"Исходные ключи: {keys!r}")
print(f"Исходные значения: {values!r}")
print(f"dict(zip(keys, values)) -> {student!r}")

# Ключи уникальны: при повторе ключа остаётся последнее значение.
pairs = [("name", "Roman"), ("age", 25), ("name", "Alex")]
student = dict(pairs)

print("\nПовторяющиеся ключи:")
print(f"Исходный список пар: {pairs!r}")
print(f"dict(pairs) -> {student!r}")
print(f"len(student) -> {len(student)!r}")

# Значения могут повторяться у разных ключей.
scores = {"Roman": 90, "Anna": 90, "Alex": 80}

print("\nПовторяющиеся значения:")
print(f"Исходный словарь: {scores!r}")
print(f"len(scores) -> {len(scores)!r}")

# Ключи должны быть хешируемыми, например строками или числами.
# Значения могут быть любого типа.
data = {"name": "Roman", "courses": ["Python", "SQL"], 100: True}

print("\nРазные типы ключей и значений:")
print(f"Исходный словарь: {data!r}")

# Словарь изменяем: значение существующего ключа можно заменить.
# Новый ключ добавляется в конец. Замена значения не перемещает ключ.
student = {"name": "Roman", "age": 25}

print("\nИзменяемость и порядок ключей:")
print(f"Исходный словарь: {student!r}")
student["age"] = 26
print(f"После student['age'] = 26: {student!r}")
student["city"] = "Kyiv"
print(f"После student['city'] = 'Kyiv': {student!r}")

# Равенство словарей зависит от пар ключ–значение, а не от порядка.
first = {"name": "Roman", "age": 25}
second = {"age": 25, "name": "Roman"}

print("\nРавенство словарей:")
print(f"Первый словарь: {first!r}")
print(f"Второй словарь: {second!r}")
print(f"first == second -> {first == second!r}")
