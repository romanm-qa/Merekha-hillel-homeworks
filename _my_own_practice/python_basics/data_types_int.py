camelCase = "Hello World!"
snake_case = "Hello World!"

# Python - тот язык который поддерживает несколько систем вычисления

# ==========================================
# Python Fundamentals
# Topic: Data Types — int
# ==========================================

# Python поддерживает разные системы счисления.
# Но все эти значения всё равно относятся к типу int.

# 10-я система счисления (decimal)
decimal_number = 123

# 16-я система счисления (hexadecimal)
# Используются цифры 0-9 и буквы A-F
hex_number = 0xFF

# 2-я система счисления (binary)
# Используются только 0 и 1
binary_number = 0b10

# 8-я система счисления (octal)
# Используются цифры от 0 до 7
octal_number = 0o17


print("Decimal:", decimal_number)
print("Hexadecimal:", hex_number)
print("Binary:", binary_number)
print("Octal:", octal_number)

print()

print("Type of decimal_number:", type(decimal_number))
print("Type of hex_number:", type(hex_number))
print("Type of binary_number:", type(binary_number))
print("Type of octal_number:", type(octal_number))

print()

# Функции для перевода обычного числа в разные системы счисления

number = 10

print("Original number:", number)
print("Binary view:", bin(number))
print("Hexadecimal view:", hex(number))
print("Octal view:", oct(number))