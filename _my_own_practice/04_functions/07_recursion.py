# Рекурсия — вызов функции из неё самой.
# Для завершения нужен базовый случай — условие остановки.
# Каждый следующий вызов должен приближать выполнение к нему.
# В числовых примерах используем целые неотрицательные числа.


# Здесь сначала выводится число, затем выполняется следующий вызов.
def countdown(number):
    if number < 0:
        raise ValueError("Число должно быть неотрицательным")

    print(f"Текущее число: {number!r}")

    if number == 0:
        return

    countdown(number - 1)


number = 3

print("Рекурсивный обратный отсчёт:")
print(f"Исходное число: {number!r}")
countdown(number)


# Вызовы: countdown(3), countdown(2), countdown(1), countdown(0).
# При number == 0 следующий вызов уже не выполняется.


# Если print() стоит после рекурсивного вызова,
# вывод происходит при возвращении из вложенных вызовов.
def count_up_on_return(number):
    if number < 0:
        raise ValueError("Число должно быть неотрицательным")

    if number == 0:
        return

    count_up_on_return(number - 1)
    print(f"Число при возвращении: {number!r}")


number = 3

print("\nВывод после рекурсивного вызова:")
print(f"Исходное число: {number!r}")
count_up_on_return(number)


# Вывод: 1, 2, 3.
# Каждый вызов ждёт завершения следующего,
# а затем продолжает выполнение со строки после вызова.


# Каждый вызов получает своё локальное значение number.
# Сообщения показывают углубление и возвращение.
def trace_calls(number):
    print(f"Вход в вызов: number = {number!r}")

    if number == 0:
        print("Базовый случай")
        return

    trace_calls(number - 1)

    print(f"Возвращение в вызов: number = {number!r}")


number = 3

print("\nПорядок рекурсивных вызовов:")
print(f"Исходное число: {number!r}")
trace_calls(number)


# Этот пример рассчитан на целое number >= 0.
# Число во внешнем вызове не меняется из-за аргумента number - 1:
# следующий вызов получает своё значение.


# Факториал: n! = n * (n - 1) * ... * 1.
# По определению 0! = 1 — это базовый случай.
def factorial(number):
    if number < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")

    if number == 0:
        return 1

    return number * factorial(number - 1)


print("\nРекурсивный факториал:")
print(f"factorial(0) -> {factorial(0)!r}")
print(f"factorial(1) -> {factorial(1)!r}")
print(f"factorial(5) -> {factorial(5)!r}")


# factorial(3) возвращает 3 * factorial(2).
# factorial(2) возвращает 2 * factorial(1).
# factorial(1) возвращает 1 * factorial(0).
# factorial(0) возвращает 1.
# Затем результаты возвращаются вверх: 1, 1, 2, 6.


# return нужен, чтобы передать результат предыдущему вызову.
# Здесь вычисление выполняется, но его результат теряется.
def factorial_without_return(number):
    if number == 0:
        return 1

    number * factorial_without_return(number - 1)


print("\nПропущенный return:")
print(f"factorial_without_return(1) -> {factorial_without_return(1)!r}")

# Вызов с 1 вычисляет 1 * 1, затем доходит до конца и возвращает None.
# На следующем уровне попытка умножить число на None вызовет TypeError.
try:
    factorial_without_return(2)
except TypeError as error:
    print(
        f"factorial_without_return(2) -> "
        f"{type(error).__name__}: {error}"
    )

# Ошибочные аргументы можно отклонить до рекурсивного вызова.
print("\nПроверка отрицательного аргумента:")

try:
    factorial(-1)
except ValueError as error:
    print(f"factorial(-1) -> {type(error).__name__}: {error}")


# Ту же задачу можно решить через цикл.
def factorial_loop(number):
    if number < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")

    result = 1

    for factor in range(1, number + 1):
        result *= factor

    return result


number = 5

print("\nСравнение рекурсии и цикла:")
print(f"Исходное число: {number!r}")
print(f"factorial(number) -> {factorial(number)!r}")
print(f"factorial_loop(number) -> {factorial_loop(number)!r}")


# Цикл здесь не создаёт цепочку вложенных вызовов.
# Для простого повторения он обычно удобнее и экономнее по памяти.


# Рекурсия подходит для обработки вложенных структур.
# Встретили список — обрабатываем его тем же способом.
# Встретили другой элемент — добавляем его в результат.
def flatten_list(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


nested_numbers = [1, [2, 3], [], [4, [5, 6]]]

print("\nОбработка вложенного списка:")
print(f"Исходный список: {nested_numbers!r}")
print(f"flatten_list(nested_numbers) -> {flatten_list(nested_numbers)!r}")
print(f"Исходный список после вызова: {nested_numbers!r}")
print(f"flatten_list([]) -> {flatten_list([])!r}")


# Здесь остановка происходит, когда больше нет вложенных списков.
# Пустой список сразу возвращает пустой результат.
# Пример рассчитан на списки без циклических ссылок.


# Числа Фибоначчи: 0, 1, 1, 2, 3, 5, 8...
# Используем индексы с нуля: fibonacci(0) = 0, fibonacci(1) = 1.
def fibonacci(number):
    if number < 0:
        raise ValueError("Индекс должен быть неотрицательным")

    if number < 2:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print("\nРекурсивное вычисление Фибоначчи:")
print(f"fibonacci(0) -> {fibonacci(0)!r}")
print(f"fibonacci(1) -> {fibonacci(1)!r}")
print(f"fibonacci(6) -> {fibonacci(6)!r}")


# Такая реализация повторно вычисляет одинаковые значения.
# Для больших индексов она работает очень медленно.


# Цикл вычисляет каждое следующее число один раз.
def fibonacci_loop(number):
    if number < 0:
        raise ValueError("Индекс должен быть неотрицательным")

    previous = 0
    current = 1

    for _ in range(number):
        previous, current = current, previous + current

    return previous


number = 6

print("\nФибоначчи через цикл:")
print(f"Исходный индекс: {number!r}")
print(f"fibonacci(number) -> {fibonacci(number)!r}")
print(f"fibonacci_loop(number) -> {fibonacci_loop(number)!r}")

# Python ограничивает глубину рекурсивных вызовов.
# RecursionError возможен и при правильном базовом случае,
# если до него нужно сделать слишком много вложенных вызовов.
#
# Здесь аргумент не меняется: базовый случай не будет достигнут.
# Пример закомментирован, чтобы не запускать ошибочную рекурсию.

# def broken_countdown(number):
#     if number == 0:
#         return
#
#     broken_countdown(number)
#
#
# broken_countdown(3)


# Главное:
# определить базовый случай;
# приближать выполнение к нему;
# возвращать результат через return, если он нужен вызывающему коду;
# учитывать глубину вызовов и повторные вычисления;
# выбирать рекурсию, когда она упрощает решение задачи.
