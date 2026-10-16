# Вложенный цикл — цикл внутри другого цикла.
# На каждой итерации внешнего цикла внутренний запускается заново.
print("Вложенные циклы:")
print(f"Значения внешнего цикла: {list(range(2))!r}")
print(f"Значения внутреннего цикла: {list(range(3))!r}")

for outer_index in range(2):
    print(f"Внешняя итерация: {outer_index!r}")

    for inner_index in range(3):
        print(f"    Внутренняя итерация: {inner_index!r}")

# Внешнее тело выполнится 2 раза, внутреннее — 2 * 3 = 6 раз.


# Через вложенные циклы можно получить все сочетания элементов.
colors = ["red", "blue"]
sizes = ["S", "M"]

print("\nВсе сочетания цветов и размеров:")
print(f"Исходные цвета: {colors!r}")
print(f"Исходные размеры: {sizes!r}")

for color in colors:
    for size in sizes:
        print(f"Цвет: {color!r}; размер: {size!r}")

# Внешний цикл получает очередной вложенный список.
# Внутренний цикл перебирает числа этого списка.
rows = [
    [1, 2, 3],
    [4, 5],
    [6],
]

print("\nПеребор списка списков:")
print(f"Исходный список: {rows!r}")

for row in rows:
    print(f"Текущая строка: {row!r}")

    for number in row:
        print(f"    Текущее число: {number!r}")

# Вложенные списки могут иметь разную длину.


# Результат можно накапливать во внутреннем цикле.
rows = [
    [1, 2, 3],
    [4, 5],
    [6],
]
total = 0

print("\nСумма всех чисел:")
print(f"Исходный список: {rows!r}")

for row in rows:
    for number in row:
        total += number

print(f"Сумма: {total!r}")

# Чтобы собрать плоский список, добавляем каждый элемент отдельно.
# У пустого вложенного списка внутренний цикл не выполнится.
rows = [
    [1, 2],
    [],
    [3, 4, 5],
]
flat_numbers = []

print("\nПреобразование в плоский список:")
print(f"Исходный список: {rows!r}")

for row in rows:
    for number in row:
        flat_numbers.append(number)

print(f"Плоский список: {flat_numbers!r}")
print(f"Исходный список после перебора: {rows!r}")

# enumerate() позволяет получить индексы строки и элемента.
rows = [
    [10, 20],
    [30, 40],
]

print("\nИндексы во вложенном списке:")
print(f"Исходный список: {rows!r}")

for row_index, row in enumerate(rows):
    for column_index, number in enumerate(row):
        print(
            f"rows[{row_index}][{column_index}] -> {number!r}"
        )

# break завершает только ближайший, то есть внутренний цикл.
# Внешний цикл продолжает переходить к следующим строкам.
rows = [
    [1, -2, 3],
    [4, -5, 6],
]

print("\nbreak во внутреннем цикле:")
print(f"Исходный список: {rows!r}")

for row in rows:
    print(f"Текущая строка: {row!r}")

    for number in row:
        if number < 0:
            print(f"Найдено отрицательное число: {number!r}")
            break

        print(f"Неотрицательное число: {number!r}")

    print("Выполнение после внутреннего цикла")

# continue пропускает итерацию только ближайшего цикла.
# Здесь отрицательные числа пропускаются внутри каждой строки.
rows = [
    [1, -2, 3],
    [-4, 5, -6],
]

print("\ncontinue во внутреннем цикле:")
print(f"Исходный список: {rows!r}")

for row in rows:
    print(f"Текущая строка: {row!r}")

    for number in row:
        if number < 0:
            continue

        print(f"Неотрицательное число: {number!r}")

# continue во внешнем цикле может пропустить целую строку.
# Здесь строки, содержащие 0, не передаются внутреннему циклу.
rows = [
    [1, 2],
    [0, 3],
    [4, 5],
]

print("\ncontinue во внешнем цикле:")
print(f"Исходный список: {rows!r}")

for row in rows:
    if 0 in row:
        print(f"Пропускаем строку: {row!r}")
        continue

    print(f"Обрабатываем строку: {row!r}")

    for number in row:
        print(f"    Текущее число: {number!r}")

# Вложенные циклы могут выводить таблицу символов.
# end=" " заменяет перевод строки пробелом.
# Пустой print() переводит вывод на следующую строку.
size = 4

print("\nШахматный узор:")
print(f"Размер: {size!r} на {size!r}")

for row_index in range(size):
    for column_index in range(size):
        if (row_index + column_index) % 2 == 0:
            char = "0"
        else:
            char = "*"

        print(char, end=" ")

    print()
