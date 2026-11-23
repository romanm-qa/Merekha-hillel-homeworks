# 21, 27, 30 — простые числа и наименьшее общее кратное

# ==========================================
# Задача 21. Проверка простого числа
# ==========================================
# Дано целое число.
# Проверить, является ли оно простым.
# Вернуть True, если простое, иначе False.

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print("=" * 50)
print("Задача 21. Проверка простого числа")
print("=" * 50)

print(f"number=2 → {is_prime(2)!r}")
print(f"number=3 → {is_prime(3)!r}")
print(f"number=7 → {is_prime(7)!r}")
print(f"number=9 → {is_prime(9)!r}")
print(f"number=13 → {is_prime(13)!r}")
print(f"number=25 → {is_prime(25)!r}")
print(f"number=1 → {is_prime(1)!r}")
print(f"number=0 → {is_prime(0)!r}")
print(f"number=-5 → {is_prime(-5)!r}")
print()


# ==========================================
# Задача 27. Простые числа в диапазоне
# ==========================================
# Даны начало и конец диапазона.
# Найти все простые числа в этом диапазоне.
# Вернуть список найденных чисел.

def find_primes(start, end):
    prime_numbers = []

    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers


print("=" * 50)
print("Задача 27. Простые числа в диапазоне")
print("=" * 50)

print(f"start=1, end=10 → {find_primes(1, 10)!r}")
print(f"start=1, end=20 → {find_primes(1, 20)!r}")
print(f"start=10, end=30 → {find_primes(10, 30)!r}")
print(f"start=2, end=2 → {find_primes(2, 2)!r}")
print(f"start=4, end=4 → {find_primes(4, 4)!r}")
print(f"start=-5, end=5 → {find_primes(-5, 5)!r}")
print()


# ==========================================
# Задача 30. Наименьшее общее кратное
# ==========================================
# Даны два целых положительных числа.
# Найти их наименьшее общее кратное.
# Вернуть результат.

def find_lcm(a, b):
    lcm = max(a, b)

    while lcm % a != 0 or lcm % b != 0:
        lcm += 1
    return lcm


print("=" * 50)
print("Задача 30. Наименьшее общее кратное")
print("=" * 50)

print(f"a=4, b=6 → {find_lcm(4, 6)!r}")
print(f"a=6, b=8 → {find_lcm(6, 8)!r}")
print(f"a=3, b=5 → {find_lcm(3, 5)!r}")
print(f"a=10, b=20 → {find_lcm(10, 20)!r}")
print(f"a=7, b=7 → {find_lcm(7, 7)!r}")
print(f"a=1, b=9 → {find_lcm(1, 9)!r}")
print()
