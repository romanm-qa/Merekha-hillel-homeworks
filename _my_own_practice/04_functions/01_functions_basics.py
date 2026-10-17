# Функция — блок кода для выполнения определённой задачи.
# def создаёт функцию, но не запускает её тело.
# Для запуска нужно вызвать функцию: написать её имя со скобками.
def say_hello():
    print("Hello!")


print("Создание и вызов функции:")
print("Функция создана. Теперь вызываем её:")
say_hello()

# При каждом вызове тело функции выполняется заново.
print("\nПовторные вызовы функции:")
say_hello()
say_hello()


# Параметр — имя в определении функции.
# Аргумент — значение, переданное при вызове.
# Здесь name — параметр, а "Roman" и "Alex" — аргументы.
def greet(name):
    print(f"Hello, {name}!")


print("\nФункция с параметром:")
greet("Roman")
greet("Alex")

# Параметру можно передать значение из переменной.
# Имя переменной снаружи не обязано совпадать с именем параметра.
user_name = "Kate"

print("\nПередача значения из переменной:")
print(f"Исходное имя: {user_name!r}")
greet(user_name)


# return возвращает результат вызывающему коду.
# Полученное значение можно сохранить в переменной.
def add(first_number, second_number):
    return first_number + second_number


first_number = 10
second_number = 5

print("\nВозврат результата:")
print(f"Исходные числа: {first_number!r}, {second_number!r}")

result = add(first_number, second_number)

print(f"add(first_number, second_number) -> {result!r}")

# Возвращённое значение можно использовать в выражениях.
print("\nИспользование результата в вычислении:")
print(f"Исходные числа: {first_number!r}, {second_number!r}")
print(f"add(first_number, second_number) * 2 -> {add(first_number, second_number) * 2!r}")


# print() выводит информацию, а return возвращает значение.
# Если функция дошла до конца без return, она возвращает None.
def print_sum(first_number, second_number):
    print(f"Сумма внутри функции: {first_number + second_number!r}")


def return_sum(first_number, second_number):
    return first_number + second_number


print("\nРазница между print и return:")
print(f"Исходные числа: {first_number!r}, {second_number!r}")

printed_result = print_sum(first_number, second_number)
returned_result = return_sum(first_number, second_number)

print(f"Результат вызова print_sum(): {printed_result!r}")
print(f"Результат вызова return_sum(): {returned_result!r}")


# return без значения завершает функцию и возвращает None.
# Здесь пустое имя обрабатывается отдельной веткой.
def create_greeting(name):
    if not name:
        return

    return f"Hello, {name}!"


print("\nreturn без значения:")
print(f"create_greeting('Roman') -> {create_greeting('Roman')!r}")
print(f"create_greeting('') -> {create_greeting('')!r}")


# return завершает текущий вызов функции.
# Код после выполненного return в этой функции не выполняется.
def check_number(number):
    if number > 0:
        return "Положительное число"

    if number < 0:
        return "Отрицательное число"

    return "Ноль"


print("\nДосрочное завершение через return:")
print(f"check_number(5) -> {check_number(5)!r}")
print(f"check_number(-3) -> {check_number(-3)!r}")
print(f"check_number(0) -> {check_number(0)!r}")


# Если return есть только в одной ветке, другая может вернуть None.
def describe_positive(number):
    if number > 0:
        return "Положительное число"


print("\nНеявный возврат None:")
print(f"describe_positive(5) -> {describe_positive(5)!r}")
print(f"describe_positive(0) -> {describe_positive(0)!r}")


# Запись return first, second возвращает один объект — кортеж.
def get_min_max(numbers):
    return min(numbers), max(numbers)


numbers = [4, 8, 2, 6]

print("\nВозврат нескольких значений:")
print(f"Исходный список: {numbers!r}")

result = get_min_max(numbers)

print(f"get_min_max(numbers) -> {result!r}")
print(f"Тип результата: {type(result).__name__}")

# Возвращённый кортеж можно распаковать в отдельные переменные.
minimum, maximum = get_min_max(numbers)

print("\nРаспаковка результата:")
print(f"Исходный список: {numbers!r}")
print(f"Минимум: {minimum!r}")
print(f"Максимум: {maximum!r}")


# Функция может вернуть список или другой объект.
# Здесь создаётся новый список, исходный не изменяется.
def get_positive_numbers(numbers):
    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)

    return positive_numbers


numbers = [3, -1, 0, 8, -5, 2]

print("\nВозврат списка:")
print(f"Исходный список: {numbers!r}")
print(f"get_positive_numbers(numbers) -> {get_positive_numbers(numbers)!r}")
print(f"Исходный список после вызова: {numbers!r}")


# Docstring — строка документации в начале тела функции.
# Она объясняет назначение функции и доступна через __doc__.
def square(number):
    """Возвращает квадрат числа."""
    return number ** 2


print("\nДокументация функции:")
print(f"square.__name__ -> {square.__name__!r}")
print(f"square.__doc__ -> {square.__doc__!r}")
print(f"square(4) -> {square(4)!r}")


# pass ничего не делает и подходит для временной заглушки.
# Такая функция при вызове возвращает None.
def future_function():
    pass


print("\nФункция-заглушка:")
print(f"future_function() -> {future_function()!r}")

# Для имён функций используем snake_case и понятные названия.
# Например: calculate_total, find_user, get_positive_numbers.
# Не называем свои функции list, sum или print:
# это перекроет доступ к встроенным объектам через эти имена.
