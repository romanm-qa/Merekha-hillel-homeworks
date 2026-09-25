# Распаковка присваивает элементы списка отдельным переменным.
# Без звёздочки число переменных должно совпадать с числом элементов,
# иначе возникнет ValueError.
numbers = [10, 20, 30]
first, second, third = numbers

print("Простая распаковка:")
print(f"Исходный список: {numbers!r}")
print(f"first -> {first!r}")
print(f"second -> {second!r}")
print(f"third -> {third!r}")

# Список можно распаковать сразу, не сохраняя его в отдельную переменную.
name, age = ["Roman", 29]

print("\nРаспаковка напрямую:")
print(f"Исходные значения: {['Roman', 29]!r}")
print(f"name -> {name!r}")
print(f"age -> {age!r}")

# При обмене значениями Python сначала вычисляет правую часть,
# затем присваивает результаты переменным слева.
a = 5
b = 17

print("\nОбмен значениями:")
print(f"До обмена: a = {a!r}, b = {b!r}")
a, b = b, a
print(f"После a, b = b, a: a = {a!r}, b = {b!r}")

# Звёздочка собирает оставшиеся элементы в новый список.
# В одной распаковке может быть только одна переменная со звёздочкой.
numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers

print("\nРаспаковка со звёздочкой:")
print(f"Исходный список: {numbers!r}")
print(f"first -> {first!r}")
print(f"middle -> {middle!r}")
print(f"last -> {last!r}")

# Если между первым и последним элементами ничего нет, получится пустой список.
short_numbers = [10, 20]
short_first, *short_middle, short_last = short_numbers

print("\nЗвёздочка без оставшихся элементов:")
print(f"Исходный список: {short_numbers!r}")
print(f"short_middle -> {short_middle!r}")

# Имя _ используют по соглашению, когда значение не понадобится.
# Элемент всё равно присваивается переменной _, он не исчезает из списка.
numbers = [10, 20, 30]
first, _, third = numbers

print("\nПропуск ненужного значения:")
print(f"Исходный список: {numbers!r}")
print(f"first -> {first!r}")
print(f"third -> {third!r}")

# На каждом шаге цикла вложенный список распаковывается в две переменные.
users = [
    ["Roman", 29],
    ["Anna", 25],
]

print("\nРаспаковка в цикле:")
print(f"Исходный список: {users!r}")

for name, age in users:
    print(f"name -> {name!r}, age -> {age!r}")
