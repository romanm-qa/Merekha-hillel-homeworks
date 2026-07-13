# ==========================
# Task 1. Iterators
# ==========================
class ReverseIterator:
    def __init__(self, items):
        # Сохраняем список и устанавливаем индекс на последний элемент
        self.items = items
        self.index = len(items) - 1

    def __iter__(self):
        # Возвращаем сам объект-итератор
        return self

    def __next__(self):
        # Если элементы закончились — завершаем итерацию
        if self.index < 0:
            raise StopIteration

        # Возвращаем текущий элемент и переходим к предыдущему
        item = self.items[self.index]
        self.index -= 1
        return item


test_cases = [
    "Login test",
    "API test",
    "Checkout test",
]

reverse_iterator = ReverseIterator(test_cases)

for test_case in reverse_iterator:
    print(test_case)


# ==========================
# Task 2. Iterators
# ==========================
class EvenNumbersIterator:
    def __init__(self, n):
        # Сохраняем верхнюю границу и начинаем с 0
        self.n = n
        self.current = 0

    def __iter__(self):
        # Возвращаем сам объект-итератор
        return self

    def __next__(self):
        # Завершаем итерацию, когда текущее число больше N
        if self.current > self.n:
            raise StopIteration

        # Сохраняем текущее число и переходим к следующему чётному
        number = self.current
        self.current += 2
        return number


even_numbers = EvenNumbersIterator(7)

for number in even_numbers:
    print(number)


# ============================
# Task 1. Generators
# ============================

# Генератор возвращает последовательность чётных чисел от 0 до N
def even_numbers(n):
    # Проходим по всем числам от 0 до N включительно
    for number in range(n + 1):
        # Если число чётное — возвращаем его через yield
        if number % 2 == 0:
            yield number


# Перебираем все значения, которые возвращает генератор
for number in even_numbers(5):
    print(number)


# ============================
# Task 2. Generators
# ============================

# Генератор возвращает последовательность чисел Фибоначчи до N
def fibonacci(n):
    # Начинаем последовательность с первых двух чисел
    first_number = 0
    second_number = 1

    # Генерируем числа, пока текущее значение не превысит N
    while first_number <= n:
        # Возвращаем текущее число последовательности
        yield first_number
        # Вычисляем следующие два числа Фибоначчи
        first_number, second_number = second_number, first_number + second_number


# Перебираем все значения, которые возвращает генератор
for number in fibonacci(5):
    print(number)


# ============================
# Task 1. Decorators
# ============================

# Декоратор выводит аргументы и результат вызова функции
def log_function(func):
    def wrapper(*args, **kwargs):
        # Выводим все переданные аргументы
        print(f"Аргументы: {args}")

        # Вызываем исходную функцию и сохраняем результат
        result = func(*args, **kwargs)

        # Выводим результат работы функции
        print(f"Результат: {result}")

        # Возвращаем результат вызывающему коду
        return result

    # Возвращаем новую функцию с логированием
    return wrapper


# Передаем функцию add_numbers в декоратор log_function
@log_function
def add_numbers(first_number, second_number):
    return first_number + second_number


add_numbers(5, 3)


# ============================
# Task 2. Decorators
# ============================

# Декоратор обрабатывает исключения, возникающие при вызове функции
def security(func):
    def wrapper(*args, **kwargs):
        try:
            # Вызываем исходную функцию
            return func(*args, **kwargs)
        except Exception as error:
            # Выводим сообщение об ошибке
            print(f"Ошибка: {error}")

    # Возвращаем новую функцию с обработкой исключений
    return wrapper


# Передаем функцию withdraw_money в декоратор security
@security
def withdraw_money(balance, amount):
    if amount > balance:
        raise ValueError("Недостаточно средств")

    print(f"Выдано {amount} грн")


# Вызываем декорированную функцию
withdraw_money(1000, 500)
withdraw_money(1000, 1500)
