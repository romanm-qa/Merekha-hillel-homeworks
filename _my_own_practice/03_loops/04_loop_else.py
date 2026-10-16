# else у цикла выполняется после его нормального завершения:
# for перебрал все элементы, а условие while стало ложным.
# Если выполнится break, блок else будет пропущен.
# else стоит на одном уровне отступов с for или while.


# for заканчивает перебор — выполняется else.
numbers = [1, 2, 3]

print("for...else без break:")
print(f"Исходный список: {numbers!r}")

for number in numbers:
    print(f"Текущее число: {number!r}")
else:
    print("Все элементы перебраны")

print("Выполнение после цикла")

# Если число найдено, break завершает цикл и пропускает else.
numbers = [5, 8, 12, 18, 21]
target = 12

print("\nПоиск с успешным результатом:")
print(f"Исходный список: {numbers!r}")
print(f"Искомое число: {target!r}")

for number in numbers:
    print(f"Проверяем число: {number!r}")

    if number == target:
        print(f"Число найдено: {number!r}")
        break
else:
    print(f"Число {target!r} не найдено")

# Если число не найдено, for переберёт весь список.
# break не выполнится, поэтому выполнится else.
target = 99

print("\nПоиск без результата:")
print(f"Исходный список: {numbers!r}")
print(f"Искомое число: {target!r}")

for number in numbers:
    print(f"Проверяем число: {number!r}")

    if number == target:
        print(f"Число найдено: {number!r}")
        break
else:
    print(f"Число {target!r} не найдено")

# while заканчивается, когда условие становится ложным.
# Если выхода через break не было, выполняется else.
countdown = 3

print("\nwhile...else без break:")
print(f"Начальное значение countdown: {countdown!r}")

while countdown > 0:
    print(f"Текущее значение countdown: {countdown!r}")
    countdown -= 1
else:
    print(f"Условие стало ложным: countdown = {countdown!r}")

print("Выполнение после цикла")

# break пропускает else и в цикле while.
countdown = 3

print("\nwhile...else с break:")
print(f"Начальное значение countdown: {countdown!r}")

while countdown > 0:
    print(f"Текущее значение countdown: {countdown!r}")

    if countdown == 2:
        print("Выходим через break")
        break

    countdown -= 1
else:
    print("Этот блок не выполнится")

print(f"Значение после цикла: {countdown!r}")

# continue пропускает остаток итерации, но не завершает цикл.
# Поэтому он не мешает выполнению else после полного перебора.
numbers = [1, 2, 3, 4, 5]

print("\ncontinue и else:")
print(f"Исходный список: {numbers!r}")

for number in numbers:
    if number % 2 == 0:
        continue

    print(f"Нечётное число: {number!r}")
else:
    print("Перебор завершён, блок else выполнился")

# Даже если continue сработал на каждой итерации, else выполнится.
numbers = [2, 4, 6]

print("\nПропуск всех элементов через continue:")
print(f"Исходный список: {numbers!r}")

for number in numbers:
    if number % 2 == 0:
        continue

    print(f"Нечётное число: {number!r}")
else:
    print("Все элементы пропущены, но перебор завершён")

# У пустого объекта нет элементов, но перебор нормально завершается.
# Поэтому else выполняется даже без единой итерации.
numbers = []

print("\nfor...else с пустым списком:")
print(f"Исходный список: {numbers!r}")

for number in numbers:
    print(f"Эта строка не появится: {number!r}")
else:
    print("Список пуст, блок else выполнился")

# Если условие while сразу ложно, else тоже выполняется.
countdown = 0

print("\nwhile...else без итераций:")
print(f"Начальное значение countdown: {countdown!r}")
print(f"countdown > 0 -> {countdown > 0!r}")

while countdown > 0:
    print("Эта строка не появится")
else:
    print("Условие сразу ложно, блок else выполнился")

# else у цикла не означает «условие if оказалось ложным».
# Он относится к циклу целиком.
# Исключение или return из функции также могут прервать выполнение
# до блока else, поэтому важен именно нормальный конец цикла.
