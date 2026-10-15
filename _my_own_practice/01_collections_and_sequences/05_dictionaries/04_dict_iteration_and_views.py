# При обычном переборе словаря получаем его ключи.
# Перебор идёт в порядке добавления ключей.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("Перебор словаря — ключи:")
print(f"Исходный словарь: {student!r}")
for key in student:
    print(f"Ключ: {key!r}")

# keys() возвращает представление ключей словаря.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nКлючи словаря — keys():")
print(f"Исходный словарь: {student!r}")
print(f"student.keys() -> {student.keys()!r}")
for key in student.keys():
    print(f"Ключ: {key!r}")

# values() возвращает представление значений словаря.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nЗначения словаря — values():")
print(f"Исходный словарь: {student!r}")
print(f"student.values() -> {student.values()!r}")
for value in student.values():
    print(f"Значение: {value!r}")

# items() возвращает представление пар (ключ, значение).
# Каждая пара при переборе — кортеж.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nПары словаря — items():")
print(f"Исходный словарь: {student!r}")
print(f"student.items() -> {student.items()!r}")
for pair in student.items():
    print(f"Пара: {pair!r}")

# Пару можно сразу распаковать в две переменные.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nПеребор с распаковкой ключа и значения:")
print(f"Исходный словарь: {student!r}")
for key, value in student.items():
    print(f"Ключ: {key!r}, значение: {value!r}")

# По ключу из цикла можно получить соответствующее значение.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nПолучение значений по ключам в цикле:")
print(f"Исходный словарь: {student!r}")
for key in student:
    print(f"student[{key!r}] -> {student[key]!r}")

# Представления можно преобразовать в списки.
# list(student) тоже создаёт список ключей.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}

print("\nПреобразование в списки:")
print(f"Исходный словарь: {student!r}")
print(f"list(student) -> {list(student)!r}")
print(f"list(student.keys()) -> {list(student.keys())!r}")
print(f"list(student.values()) -> {list(student.values())!r}")
print(f"list(student.items()) -> {list(student.items())!r}")

# Представления не поддерживают доступ по индексу.
# Для доступа по индексу можно создать список.
student = {"name": "Roman", "age": 25, "city": "Kyiv"}
keys_view = student.keys()

print("\nИндексы и представления:")
print(f"Исходный словарь: {student!r}")
print(f"Представление ключей: {keys_view!r}")
try:
    print(keys_view[0])
except TypeError as error:
    print(f"keys_view[0] -> {type(error).__name__}: {error}")

keys_list = list(keys_view)
print(f"Список ключей: {keys_list!r}")
print(f"keys_list[0] -> {keys_list[0]!r}")

# Представления динамические: отражают изменения исходного словаря.
# Созданный список сохраняет состав ключей на момент преобразования.
student = {"name": "Roman", "age": 25}
keys_view = student.keys()
values_view = student.values()
items_view = student.items()
keys_list = list(student)

print("\nДинамические представления:")
print(f"Исходный словарь: {student!r}")
print(f"Ключи до изменения: {keys_view!r}")
print(f"Значения до изменения: {values_view!r}")
print(f"Пары до изменения: {items_view!r}")
print(f"Список ключей до изменения: {keys_list!r}")

student["age"] = 26
student["city"] = "Kyiv"

print(f"Словарь после изменения: {student!r}")
print(f"Ключи после изменения: {keys_view!r}")
print(f"Значения после изменения: {values_view!r}")
print(f"Пары после изменения: {items_view!r}")
print(f"Ранее созданный список ключей: {keys_list!r}")

# in для keys() проверяет ключ, для values() — значение.
# Для items() проверяет целую пару (ключ, значение).
student = {"name": "Roman", "age": 25}

print("\nПроверка наличия в представлениях:")
print(f"Исходный словарь: {student!r}")
print(f"'name' in student.keys() -> {'name' in student.keys()!r}")
print(f"'Roman' in student.values() -> {'Roman' in student.values()!r}")
print(f"('name', 'Roman') in student.items() -> {('name', 'Roman') in student.items()!r}")
print(f"('name', 'Alex') in student.items() -> {('name', 'Alex') in student.items()!r}")

# Значения существующих ключей можно заменять во время перебора.
scores = {"Roman": 80, "Anna": 90, "Alex": 70}

print("\nИзменение значений во время перебора:")
print(f"Исходный словарь: {scores!r}")
for name in scores:
    scores[name] += 5
print(f"После добавления 5 баллов: {scores!r}")

# Добавлять и удалять ключи при прямом переборе словаря нельзя.
# Для удаления перебираем отдельный список ключей.
scores = {"Roman": 80, "Anna": 90, "Alex": 70}

print("\nУдаление во время перебора списка ключей:")
print(f"Исходный словарь: {scores!r}")
for name in list(scores):
    if scores[name] < 80:
        del scores[name]
print(f"После удаления результатов ниже 80: {scores!r}")
