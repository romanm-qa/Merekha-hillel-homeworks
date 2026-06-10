# ==========================================
# Python Fundamentals
# Topic: Arithmetic Operators
# ==========================================

a = 10
b = 2

# Addition (+)
print("10 + 2 =", a + b)

# Subtraction (-)
print("10 - 2 =", a - b)

# Multiplication (*)
print("10 * 2 =", a * b)

# Division (/)
# Всегда возвращает float

print("10 / 2 =", a / b)
print("Type:", type(a / b))

print()

# ==========================================
# Floor Division (//)
# ==========================================

d = 13
e = 4

print("13 / 4 =", d / e)
print("13 // 4 =", d // e)

print()

# ==========================================
# Modulo (%)
# ==========================================

print("13 % 4 =", d % e)

# Проверка на четность

print("10 % 2 =", 10 % 2)
print("11 % 2 =", 11 % 2)

print()

# ==========================================
# Exponentiation (**)
# ==========================================

print("2 ** 5 =", 2 ** 5)
print("10 ** 2 =", 10 ** 2)

print()

# ==========================================
# Priority of operations
# ==========================================

print(2 + 3 * 4)
print((2 + 3) * 4)

# ==========================================
# Square Root
# ==========================================

# Способ 1 - через степень

print("Square root of 25 =", 25 ** 0.5)
print("Square root of 81 =", 81 ** 0.5)

print()

# Способ 2 - через math.sqrt()

import math

print("Square root of 25 =", math.sqrt(25))
print("Square root of 81 =", math.sqrt(81))