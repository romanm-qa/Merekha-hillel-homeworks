# ==========================================
# Print Function
# ==========================================

print("Hello World")
print(123)
print(True)

# Вывод нескольких значений
# По умолчанию между значениями ставится пробел
print(1, 2, 3, 4, 5)

# Можно изменить разделитель:
print(1, 2, 3, sep="-")

# Параметр end
# По умолчанию после print() идет перенос строки:
print("Hello")
print("World")

# Можно изменить:
print("Hello", end=" ")
print("World")

# Символы переноса строки
print("Line 1\nLine 2")

# ==========================================
# Input Example
# Calculate circle area
# ==========================================

import math

print("PI:", math.pi)

# Получаем радиус от пользователя
# input всегда возвращает строку
radius = float(input("Please enter radius >>> "))

# Формула площади круга:
# S = π * r²

# Длина окружности
# C = 2 * π * r

area = round(math.pi * pow(radius, 2), 2)
circumference = round((2 * math.pi * radius), 2)

print("Radius:", radius)
print("Area:", area)
print("Circumference:", circumference)