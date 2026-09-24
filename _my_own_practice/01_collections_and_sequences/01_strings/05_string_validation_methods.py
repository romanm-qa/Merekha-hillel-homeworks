# Методы проверки строк возвращают bool: True или False.
# Для isalpha(), isdigit(), isalnum(), isspace() пустая строка даёт False.

# isdigit() проверяет символы цифр, но не знак и не десятичную точку.
digits = "123456"
signed_number = "-123"
decimal_number = "123.45"
unicode_digit = "²"

digits_result = digits.isdigit()
signed_result = signed_number.isdigit()
decimal_result = decimal_number.isdigit()
unicode_result = unicode_digit.isdigit()

print("Проверка цифр — isdigit():")
print(f"{digits!r}.isdigit() -> {digits_result}")
print(f"{signed_number!r}.isdigit() -> {signed_result}")
print(f"{decimal_number!r}.isdigit() -> {decimal_result}")
print(f"{unicode_digit!r}.isdigit() -> {unicode_result}")
print("Важно: isdigit() == True не гарантирует успешный int().")

# isalpha() допускает только буквы, isalnum() — буквы и цифры.
letters = "Python"
letters_with_number = "Python3"
letters_with_space = "Python QA"

letters_result = letters.isalpha()
alpha_with_number = letters_with_number.isalpha()
alnum_with_number = letters_with_number.isalnum()
alnum_with_space = letters_with_space.isalnum()

print("\nПроверка букв и цифр:")
print(f"{letters!r}.isalpha() -> {letters_result}")
print(f"{letters_with_number!r}.isalpha() -> {alpha_with_number}")
print(f"{letters_with_number!r}.isalnum() -> {alnum_with_number}")
print(f"{letters_with_space!r}.isalnum() -> {alnum_with_space}")

# isspace() принимает пробельные символы, в том числе \t и \n.
whitespace = " \t\n"
text_with_space = "Hello World"
only_whitespace = whitespace.isspace()
mixed_whitespace = text_with_space.isspace()

print("\nПроверка пробельных символов — isspace():")
print(f"{whitespace!r}.isspace() -> {only_whitespace}")
print(f"{text_with_space!r}.isspace() -> {mixed_whitespace}")

# islower() и isupper() проверяют регистр букв.
# Для True должна быть хотя бы одна буква с регистром.
lower_text = "python 3"
upper_text = "PYTHON 3"
no_letters = "123"

is_lower = lower_text.islower()
is_upper = upper_text.isupper()
digits_are_upper = no_letters.isupper()

print("\nПроверка регистра:")
print(f"{lower_text!r}.islower() -> {is_lower}")
print(f"{upper_text!r}.isupper() -> {is_upper}")
print(f"{no_letters!r}.isupper() -> {digits_are_upper}")

empty_text = ""
empty_is_alpha = empty_text.isalpha()
empty_is_digit = empty_text.isdigit()
empty_is_alnum = empty_text.isalnum()
empty_is_space = empty_text.isspace()

print("\nПустая строка:")
print(f"{empty_text!r}.isalpha() -> {empty_is_alpha}")
print(f"{empty_text!r}.isdigit() -> {empty_is_digit}")
print(f"{empty_text!r}.isalnum() -> {empty_is_alnum}")
print(f"{empty_text!r}.isspace() -> {empty_is_space}")
