# Параметры записываются в определении функции.
# Аргументы передаются при вызове.
# При позиционной передаче значения связываются по порядку.
def subtract(minuend, subtrahend):
    return minuend - subtrahend


print("Позиционные аргументы:")
print(f"subtract(10, 3) -> {subtract(10, 3)!r}")
print(f"subtract(3, 10) -> {subtract(3, 10)!r}")

# Именованные аргументы связываются с параметрами по имени.
# Порядок этих аргументов можно менять.
print("\nИменованные аргументы:")
print(f"subtract(minuend=10, subtrahend=3) -> {subtract(minuend=10, subtrahend=3)!r}")
print(f"subtract(subtrahend=3, minuend=10) -> {subtract(subtrahend=3, minuend=10)!r}")

# Позиционные и именованные аргументы можно использовать вместе.
# В обычном вызове позиционные аргументы идут перед именованными.
print("\nСмешанная передача аргументов:")
print(f"subtract(10, subtrahend=3) -> {subtract(10, subtrahend=3)!r}")

# Нельзя поставить обычный позиционный аргумент после именованного.
# Такой вызов вызовет SyntaxError, поэтому он закомментирован.
# subtract(minuend=10, 3)


# Один параметр нельзя заполнить дважды.
# Здесь minuend получает 10 позиционно и 20 по имени.
print("\nПовторная передача значения параметру:")

try:
    subtract(10, minuend=20, subtrahend=3)
except TypeError as error:
    print(f"subtract(10, minuend=20, subtrahend=3) -> {type(error).__name__}: {error}")

# Параметру без значения по умолчанию нужно передать аргумент.
print("\nПропущенный обязательный аргумент:")

try:
    subtract(10)
except TypeError as error:
    print(f"subtract(10) -> {type(error).__name__}: {error}")

# Если функция не принимает лишний аргумент, возникает TypeError.
print("\nЛишний позиционный аргумент:")

try:
    subtract(10, 3, 2)
except TypeError as error:
    print(f"subtract(10, 3, 2) -> {type(error).__name__}: {error}")

# Имя аргумента должно соответствовать параметру функции.
print("\nНеизвестный именованный аргумент:")

try:
    subtract(minuend=10, amount=3)
except TypeError as error:
    print(f"subtract(minuend=10, amount=3) -> {type(error).__name__}: {error}")


# Значение по умолчанию используется, если аргумент не передан.
# Его можно заменить при вызове позиционно или по имени.
def power(number, exponent=2):
    return number ** exponent


print("\nЗначение по умолчанию:")
print(f"power(5) -> {power(5)!r}")
print(f"power(5, 3) -> {power(5, 3)!r}")
print(f"power(5, exponent=3) -> {power(5, exponent=3)!r}")

# Переданное значение не заменяется значением по умолчанию,
# даже если оно ложное: например, 0, False или пустая строка.
print("\nЯвная передача нуля:")
print(f"power(5, exponent=0) -> {power(5, exponent=0)!r}")


# Среди обычных параметров обязательные идут перед параметрами
# со значениями по умолчанию.
def create_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print("\nОбязательный параметр и значение по умолчанию:")
print(f"create_greeting('Roman') -> {create_greeting('Roman')!r}")
print(f"create_greeting('Roman', 'Hi') -> {create_greeting('Roman', 'Hi')!r}")


# Такой порядок обычных параметров вызовет SyntaxError:
# def create_greeting(greeting="Hello", name):
#     return f"{greeting}, {name}!"


# Параметры перед / можно передавать только позиционно.
# Символ / не является отдельным параметром.
def divide(dividend, divisor, /):
    return dividend / divisor


print("\nТолько позиционные параметры:")
print(f"divide(10, 2) -> {divide(10, 2)!r}")

try:
    divide(dividend=10, divisor=2)
except TypeError as error:
    print(f"divide(dividend=10, divisor=2) -> {type(error).__name__}: {error}")


# Параметры после отдельного * передаются только по имени.
# Здесь name можно передать обоими способами, а greeting — только по имени.
def greet(name, *, greeting="Hello"):
    return f"{greeting}, {name}!"


print("\nТолько именованные параметры:")
print(f"greet('Roman') -> {greet('Roman')!r}")
print(f"greet('Roman', greeting='Hi') -> {greet('Roman', greeting='Hi')!r}")
print(f"greet(name='Roman', greeting='Hi') -> {greet(name='Roman', greeting='Hi')!r}")

try:
    greet("Roman", "Hi")
except TypeError as error:
    print(f"greet('Roman', 'Hi') -> {type(error).__name__}: {error}")


# Параметр после * может быть обязательным.
# Если значения по умолчанию нет, его нельзя пропустить.
def format_price(amount, *, currency):
    return f"{amount:.2f} {currency}"


print("\nОбязательный именованный параметр:")
print(f"format_price(100, currency='UAH') -> {format_price(100, currency='UAH')!r}")

try:
    format_price(100)
except TypeError as error:
    print(f"format_price(100) -> {type(error).__name__}: {error}")


# Среди параметров после * обязательный параметр может идти
# после параметра со значением по умолчанию.
def create_profile(*, role="student", name):
    return f"{name}: {role}"


print("\nПорядок только именованных параметров:")
print(f"create_profile(name='Roman') -> {create_profile(name='Roman')!r}")
print(f"create_profile(name='Roman', role='tester') -> {create_profile(name='Roman', role='tester')!r}")


# / и * можно использовать в одной функции.
# amount — только позиционно.
# discount — позиционно или по имени.
# currency — только по имени.
def calculate_price(amount, /, discount=0, *, currency="UAH"):
    final_amount = amount * (1 - discount / 100)
    return f"{final_amount:.2f} {currency}"


print("\nСовместное использование / и *:")
print(f"calculate_price(100) -> {calculate_price(100)!r}")
print(f"calculate_price(100, 10) -> {calculate_price(100, 10)!r}")
print(
    f"calculate_price(100, discount=10, currency='USD') -> "
    f"{calculate_price(100, discount=10, currency='USD')!r}"
)

try:
    calculate_price(amount=100)
except TypeError as error:
    print(f"calculate_price(amount=100) -> {type(error).__name__}: {error}")

try:
    calculate_price(100, 10, "USD")
except TypeError as error:
    print(f"calculate_price(100, 10, 'USD') -> {type(error).__name__}: {error}")

# Позиционный/именованный — способ передачи аргумента.
# Обязательный/необязательный — нужно ли передавать значение.
# Это разные характеристики:
# обязательный параметр тоже может приниматься только по имени.
#
# *args, **kwargs и распаковку разберём в следующем файле.
# Изменяемые значения по умолчанию — в отдельном файле после него.
