# while повторяет тело цикла, пока условие истинно.
# Условие проверяется перед каждой итерацией.
# Итерация — одно выполнение тела цикла.
countdown = 3

print("Цикл while:")
print(f"Начальное значение countdown: {countdown!r}")

while countdown > 0:
    print(f"Текущее значение countdown: {countdown!r}")
    countdown -= 1

print(f"Значение после цикла: {countdown!r}")

# Если условие сразу ложно, тело цикла не выполнится ни разу.
countdown = 0

print("\nЛожное условие перед первой итерацией:")
print(f"Начальное значение countdown: {countdown!r}")
print(f"countdown > 0 -> {countdown > 0!r}")

while countdown > 0:
    print("Эта строка не появится")

print(f"Значение после цикла: {countdown!r}")

# В условии можно использовать сам объект.
# Для чисел while number эквивалентно while number != 0.
# Любое ненулевое число истинно, а 0 — ложно.
number = 3

print("\nПроверка истинности числа:")
print(f"Начальное значение number: {number!r}")

while number:
    print(f"number: {number!r}; bool(number) -> {bool(number)!r}")
    number -= 1

print(f"После цикла number: {number!r}")
print(f"bool(number) -> {bool(number)!r}")

# Отрицательные числа тоже считаются истинными.
number = -5

print("\nИстинность отрицательного числа:")
print(f"Исходное число: {number!r}")
print(f"bool(number) -> {bool(number)!r}")

# Условие может зависеть от содержимого коллекции.
# Непустой список истинен, пустой — ложен.
# pop() удаляет и возвращает последний элемент.
numbers = [10, 20, 30]

print("\nЦикл while со списком:")
print(f"Исходный список: {numbers!r}")

while numbers:
    removed_number = numbers.pop()
    print(f"Удалённый элемент: {removed_number!r}")
    print(f"Список после pop(): {numbers!r}")

print(f"Список после цикла: {numbers!r}")
print(f"bool(numbers) -> {bool(numbers)!r}")

# Если условие всегда истинно, цикл будет бесконечным.
# Здесь countdown не изменяется, поэтому остаётся равным 3.
# Пример закомментирован, чтобы файл можно было запустить целиком.
# В терминале такой цикл можно остановить сочетанием Ctrl+C.

# countdown = 3
#
# while countdown > 0:
#     print(f"countdown: {countdown!r}")
