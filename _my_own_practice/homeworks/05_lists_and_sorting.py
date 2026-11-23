# 4, 24, 25 — нечётные числа, сортировка пузырьком, поиск пропущенного числа

# ==========================================
# Задача 4. Нечётные числа
# ==========================================
# Дан список случайных целых чисел.
# Найти все нечётные числа в списке.
# Вернуть список найденных чисел.

def find_odd_numbers(numbers):
    odd_numbers = []

    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)

    return odd_numbers


print("=" * 50)
print("Задача 4. Нечётные числа")
print("=" * 50)

print(f"numbers={[12, 7, 4, 15, 8, 21, 10]!r} → {find_odd_numbers([12, 7, 4, 15, 8, 21, 10])!r}")
print(f"numbers={[2, 4, 6, 8]!r} → {find_odd_numbers([2, 4, 6, 8])!r}")
print(f"numbers={[1, 3, 5, 7]!r} → {find_odd_numbers([1, 3, 5, 7])!r}")
print(f"numbers={[-3, -2, 0, 4, 9]!r} → {find_odd_numbers([-3, -2, 0, 4, 9])!r}")
print(f"numbers={[]!r} → {find_odd_numbers([])!r}")
print()


# ==========================================
# Задача 24. Сортировка пузырьком
# ==========================================
# Дан список целых чисел.
# Отсортировать список по возрастанию
# с помощью алгоритма Bubble Sort.
# Не использовать sort() или sorted().
# Вернуть отсортированный список.

def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


print("=" * 50)
print("Задача 24. Сортировка пузырьком")
print("=" * 50)

print(f"numbers={[5, 3, 8, 1]!r} → {bubble_sort([5, 3, 8, 1])!r}")
print(f"numbers={[1, 2, 3, 4]!r} → {bubble_sort([1, 2, 3, 4])!r}")
print(f"numbers={[9, 7, 5, 3, 1]!r} → {bubble_sort([9, 7, 5, 3, 1])!r}")
print(f"numbers={[4, 2, 4, 1, 2]!r} → {bubble_sort([4, 2, 4, 1, 2])!r}")
print(f"numbers={[-3, 5, 0, -1, 2]!r} → {bubble_sort([-3, 5, 0, -1, 2])!r}")
print(f"numbers={[]!r} → {bubble_sort([])!r}")
print()


# ==========================================
# Задача 25. Поиск пропущенного числа
# ==========================================
# Дан список чисел от 1 до n.
# Одно число в последовательности пропущено.
# Найти и вернуть пропущенное число.

def find_missing_number(numbers):
    n = len(numbers) + 1

    for num in range(1, n + 1):
        if num not in numbers:
            return num


print("=" * 50)
print("Задача 25. Поиск пропущенного числа")
print("=" * 50)

print(f"numbers={[1, 2, 3, 5, 6, 7]!r} → {find_missing_number([1, 2, 3, 5, 6, 7])!r}")
print(f"numbers={[1, 2, 4, 5]!r} → {find_missing_number([1, 2, 4, 5])!r}")
print(f"numbers={[2, 3, 4, 5]!r} → {find_missing_number([2, 3, 4, 5])!r}")
print(f"numbers={[1, 2, 3, 4]!r} → {find_missing_number([1, 2, 3, 4])!r}")
print(f"numbers={[1, 3]!r} → {find_missing_number([1, 3])!r}")
print()
