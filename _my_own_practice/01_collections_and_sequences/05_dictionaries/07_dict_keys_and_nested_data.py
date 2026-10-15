# Ключи словаря должны быть хешируемыми.
# Например, можно использовать строки, числа и кортежи из хешируемых элементов.
data = {"name": "Roman", 100: "student_id", (1, 2): "coordinates"}

print("Хешируемые ключи:")
print(f"Исходный словарь: {data!r}")
print(f"data['name'] -> {data['name']!r}")
print(f"data[100] -> {data[100]!r}")
print(f"data[(1, 2)] -> {data[(1, 2)]!r}")

# Список не хешируется, поэтому не может быть ключом.
data = {"name": "Roman"}
invalid_key = [1, 2]

print("\nПопытка использовать список как ключ:")
print(f"Исходный словарь: {data!r}")
print(f"Новый ключ: {invalid_key!r}")
try:
    data[invalid_key] = "coordinates"
except TypeError as error:
    print(f"{type(error).__name__}: {error}")

# set и dict тоже не хешируются.
data = {"name": "Roman"}
invalid_keys = [{1, 2}, {"id": 100}]

print("\nПопытка использовать set и dict как ключи:")
print(f"Исходный словарь: {data!r}")
for key in invalid_keys:
    print(f"Проверяемый ключ: {key!r}")
    try:
        data[key] = "value"
    except TypeError as error:
        print(f"{type(error).__name__}: {error}")

# Кортеж хешируется только тогда, когда все его элементы хешируемые.
data = {}
valid_key = (1, 2)
invalid_key = (1, [2, 3])

print("\nКортежи как ключи:")
print(f"Исходный словарь: {data!r}")
data[valid_key] = "valid"
print(f"После добавления ключа {valid_key!r}: {data!r}")
print(f"Нехешируемый кортеж: {invalid_key!r}")
try:
    data[invalid_key] = "invalid"
except TypeError as error:
    print(f"{type(error).__name__}: {error}")

# frozenset хешируется и может быть ключом.
group = frozenset({"Roman", "Anna"})
groups = {group: "Python"}

print("\nfrozenset как ключ:")
print(f"Исходный словарь: {groups!r}")
print(f"Ключ группы: {group!r}")
print(f"groups[group] -> {groups[group]!r}")

# Равные числовые ключи относятся к одной записи.
# 1, 1.0 и True равны и имеют одинаковый хеш.
data = {1: "integer"}

print("\nРавные числовые ключи:")
print(f"Исходный словарь: {data!r}")
data[1.0] = "float"
print(f"После data[1.0] = 'float': {data!r}")
data[True] = "boolean"
print(f"После data[True] = 'boolean': {data!r}")
print(f"len(data) -> {len(data)!r}")
print(f"data[1] -> {data[1]!r}")

# Значения словаря могут быть любого типа, включая списки и словари.
student = {
    "name": "Roman",
    "age": 25,
    "courses": ["Python", "SQL"],
    "address": {"city": "Kyiv", "country": "Ukraine"},
}

print("\nВложенные данные:")
print(f"Исходный словарь: {student!r}")
print(f"student['courses'] -> {student['courses']!r}")
print(f"student['address'] -> {student['address']!r}")

# Сначала получаем список по ключу, затем его элемент по индексу.
student = {"name": "Roman", "courses": ["Python", "SQL"]}

print("\nДоступ к элементу вложенного списка:")
print(f"Исходный словарь: {student!r}")
print(f"student['courses'][0] -> {student['courses'][0]!r}")
print(f"student['courses'][1] -> {student['courses'][1]!r}")

# Сначала получаем вложенный словарь, затем значение по его ключу.
student = {
    "name": "Roman",
    "address": {"city": "Kyiv", "country": "Ukraine"},
}

print("\nДоступ к вложенному словарю:")
print(f"Исходный словарь: {student!r}")
print(f"student['address']['city'] -> {student['address']['city']!r}")
print(f"student['address']['country'] -> {student['address']['country']!r}")

# Вложенные изменяемые коллекции можно изменять.
student = {
    "name": "Roman",
    "courses": ["Python", "SQL"],
    "address": {"city": "Kyiv", "country": "Ukraine"},
}

print("\nИзменение вложенных данных:")
print(f"Исходный словарь: {student!r}")
student["courses"].append("Git")
print(f"После student['courses'].append('Git'): {student!r}")
student["address"]["city"] = "Lviv"
print(f"После student['address']['city'] = 'Lviv': {student!r}")

# get() проверяет только тот словарь, на котором вызван.
# Здесь address отсутствует: вместо него получаем пустой словарь.
student = {"name": "Roman"}

print("\nПолучение отсутствующих вложенных данных:")
print(f"Исходный словарь: {student!r}")
address = student.get("address", {})
city = address.get("city", "Unknown")
print(f"student.get('address', {{}}) -> {address!r}")
print(f"address.get('city', 'Unknown') -> {city!r}")

# Если address есть со значением None, default {} не используется.
# Проверка типа позволяет обработать такое значение.
student = {"name": "Roman", "address": None}

print("\nПроверка типа вложенного значения:")
print(f"Исходный словарь: {student!r}")
address = student.get("address")
if isinstance(address, dict):
    city = address.get("city", "Unknown")
else:
    city = "Unknown"
print(f"Полученный город: {city!r}")

# Список может содержать несколько словарей.
students = [
    {"name": "Roman", "score": 80},
    {"name": "Anna", "score": 90},
    {"name": "Alex", "score": 70},
]

print("\nПеребор списка словарей:")
print(f"Исходный список: {students!r}")
for student in students:
    print(f"Имя: {student['name']!r}, баллы: {student['score']!r}")
