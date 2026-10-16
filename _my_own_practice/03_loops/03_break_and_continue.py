# break досрочно завершает ближайший цикл.
# После выхода программа продолжает выполняться за пределами цикла.
numbers = [5, 8, 12, 18, 21]
target = 12

print("break в цикле for:")
print(f"Исходный список: {numbers!r}")
print(f"Искомое число: {target!r}")

for number in numbers:
    print(f"Проверяем число: {number!r}")

    if number == target:
        print(f"Число найдено: {number!r}")
        break

print("Выполнение после цикла")

# break работает и в цикле while.
# При number == 3 цикл завершится, хотя условие number > 0 ещё истинно.
number = 5

print("\nbreak в цикле while:")
print(f"Начальное значение number: {number!r}")

while number > 0:
    print(f"Текущее значение number: {number!r}")

    if number == 3:
        break

    number -= 1

print(f"Значение после цикла: {number!r}")

# while True сам по себе не остановится из-за ложного условия.
# В этом примере выход происходит через break.
number = 1

print("\nВыход из while True:")
print(f"Начальное значение number: {number!r}")

while True:
    print(f"Текущее значение number: {number!r}")

    if number == 3:
        break

    number += 1

print(f"Значение после цикла: {number!r}")

# continue пропускает оставшуюся часть текущей итерации.
# Цикл for после этого переходит к следующему элементу.
numbers = [1, 2, 3, 4, 5]

print("\ncontinue в цикле for:")
print(f"Исходный список: {numbers!r}")

for number in numbers:
    if number == 3:
        continue

    print(f"Число: {number!r}")

# Через continue можно пропускать элементы по условию.
# Остаток от деления чётного числа на 2 равен 0.
numbers = [1, 2, 3, 4, 5, 6]

print("\nПропуск чётных чисел:")
print(f"Исходный список: {numbers!r}")

for number in numbers:
    if number % 2 == 0:
        continue

    print(f"Нечётное число: {number!r}")

# Пустая строка считается ложной.
# Непустые имена выводятся, пустые записи пропускаются.
names = ["Roman", "", "Alex", "", "Kate"]

print("\nПропуск пустых строк:")
print(f"Исходный список: {names!r}")

for name in names:
    if not name:
        continue

    print(f"Непустое имя: {name!r}")

# Можно собрать результат, пропуская ненужные символы.
text = "hello world"
result = ""

print("\nПропуск символов строки:")
print(f"Исходная строка: {text!r}")
print(f"Пропускаемый символ: {'o'!r}")

for char in text:
    if char == "o":
        continue

    result += char

print(f"Строка без буквы 'o': {result!r}")

# В while continue возвращает выполнение к проверке условия.
# Счётчик изменяем ДО continue, чтобы изменение не было пропущено.
number = 0

print("\ncontinue в цикле while:")
print(f"Начальное значение number: {number!r}")

while number < 5:
    number += 1

    if number == 3:
        continue

    print(f"Число: {number!r}")

print(f"Значение после цикла: {number!r}")

# Сравнение на одинаковых данных:
# break останавливает весь цикл на числе 3.
# continue пропускает только обработку числа 3.
numbers = [1, 2, 3, 4, 5]

print("\nСравнение break и continue:")
print(f"Исходный список: {numbers!r}")

print("Результат с break:")

for number in numbers:
    if number == 3:
        break

    print(f"Число: {number!r}")

print("Результат с continue:")

for number in numbers:
    if number == 3:
        continue

    print(f"Число: {number!r}")

# Ошибка: continue пропускает изменение счётчика.
# Когда number станет равным 3, цикл застрянет на этом значении.
# Пример закомментирован, чтобы файл запускался целиком.

# number = 0
#
# while number < 5:
#     if number == 3:
#         continue
#
#     print(f"Число: {number!r}")
#     number += 1
