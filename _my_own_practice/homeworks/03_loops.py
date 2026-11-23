# 7, 8, 10, 11, 13, 15, 19, 20, 26 — суммы, диапазоны, произведение, факториал, таблица умножения, последовательность Сиракуз

# ==========================================
# Практика. Сумма чисел с выбором чётности
# ==========================================
# Функция принимает два аргумента:
# stop — конец диапазона от 0 до stop, не включая stop;
# type_ — режим: "even" для чётных, "odd" для нечётных.
# Вернуть сумму чисел выбранной чётности.
# Для неизвестного режима вызвать ValueError.

def count_sum(stop, type_):
    total = 0

    if type_ == "even":
        for value in range(stop):
            if value % 2 == 0:
                total += value
    elif type_ == "odd":
        for value in range(stop):
            if value % 2 == 1:
                total += value
    else:
        raise ValueError('Режим должен быть "even" или "odd"')

    return total


print("=" * 50)
print("Практика. Сумма чисел с выбором чётности")
print("=" * 50)

# Позиционные аргументы
print(f"Диапазон: range(7), режим: 'even' → сумма: {count_sum(7, 'even')!r}")
print(f"Диапазон: range(7), режим: 'odd' → сумма: {count_sum(7, 'odd')!r}")

# Именованные аргументы
print(f"Диапазон: range(10), режим: 'even' → сумма: {count_sum(stop=10, type_='even')!r}")
print(f"Диапазон: range(10), режим: 'odd' → сумма: {count_sum(stop=10, type_='odd')!r}")
print()


# ==========================================
# Задача 15. Банковский вклад
# ==========================================
# Пользователь делает вклад в размере N долларов
# на несколько лет под 11.5% годовых.
# Каждый год сумма вклада увеличивается на 11.5%.
# Начисленные проценты добавляются к сумме вклада
# и в следующем году также приносят проценты.
# Написать программу, которая принимает a и years
# и вычисляет сумму на счёте через years лет.

def calculate_deposit(a, years):
    total_amount = a

    for i in range(years):
        yearly_interest = total_amount * 11.5 / 100
        total_amount += yearly_interest

    return total_amount


print("=" * 50)
print("Задача 15. Банковский вклад")
print("=" * 50)

print(f"a=1000, years=1 → {calculate_deposit(1000, 1)!r}")
print(f"a=1000, years=2 → {calculate_deposit(1000, 2)!r}")
print(f"a=1000, years=3 → {calculate_deposit(1000, 3)!r}")
print()


# ==========================================
# Задача 7. Сумма пяти цифр
# ==========================================
# По очереди вводятся 5 цифр.
# Вывести их сумму, используя цикл for.

def sum_five_digits(numbers):
    sum_of_digits = 0

    for digit in numbers:
        sum_of_digits += digit

    return sum_of_digits


print("=" * 50)
print("Задача 7. Сумма пяти цифр")
print("=" * 50)

print(f"numbers=[1, 2, 3, 4, 5] → {sum_five_digits([1, 2, 3, 4, 5])!r}")
print(f"numbers=[5, 5, 5, 5, 5] → {sum_five_digits([5, 5, 5, 5, 5])!r}")
print(f"numbers=[0, 0, 0, 0, 0] → {sum_five_digits([0, 0, 0, 0, 0])!r}")
print()


# ==========================================
# Задача 8. Вывод чисел в диапазоне
# ==========================================
# Даны два целых числа A и B.
# Вывести все числа от A до B включительно
# в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.

def print_numbers(a, b):
    if a < b:
        for num in range(a, b + 1):
            print(num)
    else:
        for num in range(a, b - 1, -1):
            print(num)


print("=" * 50)
print("Задача 8. Вывод чисел в диапазоне")
print("=" * 50)

print("a=2, b=6 →")
print_numbers(2, 6)

print("a=6, b=2 →")
print_numbers(6, 2)

print("a=4, b=4 →")
print_numbers(4, 4)

print()


# ==========================================
# Задача 10. Сумма числового ряда
# ==========================================
# Посчитать сумму числового ряда от 0 до 14 включительно.
# Например: 0 + 1 + 2 + 3 + ... + 14.

def calculate_sum(end):
    total_sum = 0

    for num in range(end + 1):
        total_sum += num
    return total_sum


print("=" * 50)
print("Задача 10. Сумма числового ряда")
print("=" * 50)

print(f"Диапазон: 0–14 → сумма: {calculate_sum(14)!r}")
print(f"Диапазон: 0–5 → сумма: {calculate_sum(5)!r}")
print(f"Диапазон: 0–0 → сумма: {calculate_sum(0)!r}")
print()


# ==========================================
# Задача 11. Произведение чётных чисел
# ==========================================
# Перемножить все чётные числа в диапазоне
# от 0 до 436 включительно.

def multiply_even_numbers():
    multiply_digits = 1

    for digit in range(2, 436 + 1):
        if digit % 2 == 0:
            multiply_digits *= digit
    return multiply_digits


print("=" * 50)
print("Практика. Произведение положительных чётных чисел")
print("=" * 50)

result = multiply_even_numbers()
print(f"Произведение чётных чисел от 2 до 436: {result!r}")
print()


# ==========================================
# Задача 13. Факториал числа
# ==========================================
# Факториалом числа n называется число
# n! = 1 * 2 * 3 * ... * n.
# Создать программу, которая вычисляет факториал
# введённого пользователем числа, используя цикл.

def calculate_factorial(n):
    result = 1

    for digit in range(1, n + 1):
        result *= digit

    return result


print("=" * 50)
print("Задача 13. Факториал числа")
print("=" * 50)

print(f"n=0 → {calculate_factorial(0)!r}")
print(f"n=1 → {calculate_factorial(1)!r}")
print(f"n=3 → {calculate_factorial(3)!r}")
print(f"n=5 → {calculate_factorial(5)!r}")
print(f"n=6 → {calculate_factorial(6)!r}")
print()


# ==========================================
# Задача 19. Сумма чисел от 1 до n
# ==========================================
# Запросить у пользователя число n.
# Найти сумму всех чисел от 1 до n.

def sum_numbers(n):
    sum_of_total_digits = 0

    for digit in range(1, n + 1):
        sum_of_total_digits += digit
    return sum_of_total_digits


print("=" * 50)
print("Задача 19. Сумма чисел от 1 до n")
print("=" * 50)

print(f"n=5 → {sum_numbers(5)!r}")
print(f"n=10 → {sum_numbers(10)!r}")
print(f"n=1 → {sum_numbers(1)!r}")
print(f"n=0 → {sum_numbers(0)!r}")
print()


# ==========================================
# Задача 20. Таблица умножения
# ==========================================
# Вывести таблицу умножения для числа,
# которое вводит пользователь.
# Например, таблицу умножения для 5.

def multiplication_table(n):
    for digit in range(1, 11):
        print(f"{n} * {digit} = {n * digit}")


print("=" * 50)
print("Задача 20. Таблица умножения")
print("=" * 50)

print("n=5 →")
multiplication_table(5)

print()


# ==========================================
# Задача 26. Сиракузская последовательность
# ==========================================
# Запросить у пользователя начальное число.
# Вывести последовательность чисел по правилу:
# если число чётное — разделить его на 2,
# иначе — умножить на 3 и прибавить 1.
# Повторять процесс, пока число не станет равным 1.

def syracuse_sequence(n):
    our_numbers = [n]

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

        our_numbers.append(n)

    return our_numbers


print("=" * 50)
print("Задача 26. Сиракузская последовательность")
print("=" * 50)

print(f"n=6 → {syracuse_sequence(6)!r}")
print(f"n=3 → {syracuse_sequence(3)!r}")
print(f"n=1 → {syracuse_sequence(1)!r}")
print(f"n=10 → {syracuse_sequence(10)!r}")
print()
