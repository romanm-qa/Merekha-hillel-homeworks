# ==========================================
# Python Fundamentals
# Topic: Data Types — float
# ==========================================

# float (floating point number)
# Числа с плавающей точкой

float_example1 = 34.3
float_example2 = -34.3

float_example3 = 0.3
float_example4 = -0.3

float_example5 = .6
float_example6 = -.6

print("float_example1:", float_example1, type(float_example1))
print("float_example2:", float_example2, type(float_example2))
print("float_example3:", float_example3, type(float_example3))
print("float_example4:", float_example4, type(float_example4))
print("float_example5:", float_example5, type(float_example5))
print("float_example6:", float_example6, type(float_example6))

print()

# ==========================================
# Scientific notation
# ==========================================

# 4 * 10^5
large_number = 4e5

# 4 * 10^-3
small_number = 4e-3

print("large_number:", large_number, type(large_number))
print("small_number:", small_number, type(small_number))

print()

# ==========================================
# Conversion to float
# ==========================================

integer_number = 10
string_number = "25.5"

print(float(integer_number))
print(float(string_number))

print()

# ==========================================
# Basic operations with float
# ==========================================

a = 10.5
b = 2.5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print()

## ==========================================
# Float precision issue
# ==========================================

float_result = 0.1 + 0.2

print("Expected result:", 0.3)
print("Actual result:", float_result)

# Output:
# Expected result: 0.3
# Actual result: 0.30000000000000004


# ==========================================
# Decimal for precise calculations
# ==========================================

from decimal import Decimal

decimal_result = Decimal("0.1") + Decimal("0.2")

print("Decimal result:", decimal_result)

# Output:
# Decimal result: 0.3]