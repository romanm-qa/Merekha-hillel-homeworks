# ==========================================
# Python Fundamentals
# Topic: Data Types — complex
# ==========================================

# Complex number:
# a + bj
#
# a - real part
# b - imaginary part
# j² = -1

complex_number1 = 5 + 6j
complex_number2 = -5 - 2j
complex_number3 = 7 + 1j

print(complex_number1, type(complex_number1))
print(complex_number2, type(complex_number2))
print(complex_number3, type(complex_number3))

print()

# Real and imaginary parts

print("Real part:", complex_number1.real)
print("Imaginary part:", complex_number1.imag)