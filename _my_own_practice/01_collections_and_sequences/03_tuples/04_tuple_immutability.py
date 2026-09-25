# Кортеж неизменяемый: заменить его элемент по индексу нельзя.
numbers = (10, 20, 30)

print("Неизменяемость кортежа:")
print(f"Исходный кортеж: {numbers!r}")

try:
    numbers[1] = 99
except TypeError as error:
    print(f"numbers[1] = 99 -> {type(error).__name__}: {error}")

print(f"Кортеж после попытки изменения: {numbers!r}")

# При сложении создаётся новый кортеж; исходный остаётся прежним.
extended_numbers = numbers + (40, 50)

print("\nСоздание нового кортежа:")
print(f"Исходный кортеж: {numbers!r}")
print(f"numbers + (40, 50) -> {extended_numbers!r}")
print(f"Исходный кортеж после сложения: {numbers!r}")
print(f"extended_numbers is numbers -> {extended_numbers is numbers!r}")

# Список внутри кортежа можно менять, хотя сам кортеж неизменяемый.
data = ("Roman", ["Python", "SQL"])

print("\nСписок внутри кортежа:")
print(f"Исходный кортеж: {data!r}")

data[1].append("Docker")
print(f"После data[1].append('Docker'): {data!r}")

# Заменить список целиком как элемент кортежа нельзя.
try:
    data[1] = ["Git"]
except TypeError as error:
    print(f"data[1] = ['Git'] -> {type(error).__name__}: {error}")

print(f"Кортеж после попытки замены списка: {data!r}")
