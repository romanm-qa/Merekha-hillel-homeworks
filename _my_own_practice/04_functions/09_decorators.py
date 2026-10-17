from functools import wraps
from time import perf_counter


# Декоратор принимает функцию и возвращает объект,
# который будет связан с её именем.
# Здесь возвращаем функцию-обёртку с дополнительным поведением.
def add_messages(function):
    def wrapper():
        print("Перед вызовом")
        function()
        print("После вызова")

    return wrapper


def say_hello():
    print("Hello!")


print("Ручное применение декоратора:")

decorated_hello = add_messages(say_hello)
decorated_hello()


# add_messages(say_hello) создаёт и возвращает wrapper.
# Тело say_hello выполняется только при вызове decorated_hello().


# Запись @decorator применяет декоратор при определении функции.
# Она эквивалентна greet = add_messages(greet).
@add_messages
def greet():
    print("Hi!")


print("\nПрименение через @:")
greet()


# Обёртка должна вернуть результат исходной функции,
# если нужно сохранить её возвращаемое значение.
# *args и **kwargs позволяют передать полученные аргументы дальше.
def log_call(function):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {function.__name__!r}")
        return function(*args, **kwargs)

    return wrapper


@log_call
def add(first_number, second_number):
    return first_number + second_number


print("\nАргументы и возвращаемое значение:")
print(f"add(10, 20) -> {add(10, 20)!r}")
print(
    f"add(first_number=10, second_number=20) -> "
    f"{add(first_number=10, second_number=20)!r}"
)


# Если забыть вернуть результат, обёртка вернёт None.
def lose_result(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper


@lose_result
def multiply(first_number, second_number):
    return first_number * second_number


print("\nПотеря возвращаемого значения:")
print(f"multiply(3, 4) -> {multiply(3, 4)!r}")

# Без wraps у обёртки остаются её собственные имя и документация.
print("\nИмя функции без wraps:")
print(f"add.__name__ -> {add.__name__!r}")


# wraps копирует основные метаданные исходной функции
# и добавляет __wrapped__ — ссылку на исходную функцию.
# Сама вызываемая функция при этом остаётся обёрткой.
def log_call_with_wraps(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {function.__name__!r}")
        return function(*args, **kwargs)

    return wrapper


@log_call_with_wraps
def subtract(minuend, subtrahend):
    """Возвращает разность двух чисел."""
    return minuend - subtrahend


print("\nСохранение метаданных через wraps:")
print(f"subtract.__name__ -> {subtract.__name__!r}")
print(f"subtract.__doc__ -> {subtract.__doc__!r}")
print(f"subtract(10, 3) -> {subtract(10, 3)!r}")

# Вызов через __wrapped__ обходит эту обёртку.
print(f"subtract.__wrapped__(10, 3) -> {subtract.__wrapped__(10, 3)!r}")


# Действие после вызова не выполнится, если функция выбросит исключение.
def report_success(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Перед вычислением")
        result = function(*args, **kwargs)
        print("Вычисление успешно завершено")
        return result

    return wrapper


@report_success
def divide(dividend, divisor):
    return dividend / divisor


print("\nИсключение внутри декорированной функции:")

try:
    divide(10, 0)
except ZeroDivisionError as error:
    print(f"divide(10, 0) -> {type(error).__name__}: {error}")


# Сообщение об успешном завершении не появится.
# Исключение передаётся вызывающему коду.


# Если завершающее действие нужно и при исключении,
# используем finally. Исключение при этом не подавляется.
def report_finish(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Начало вызова")

        try:
            return function(*args, **kwargs)
        finally:
            print("Вызов завершён")

    return wrapper


@report_finish
def calculate_ratio(dividend, divisor):
    return dividend / divisor


print("\nЗавершающее действие через finally:")

try:
    calculate_ratio(10, 0)
except ZeroDivisionError as error:
    print(f"calculate_ratio(10, 0) -> {type(error).__name__}: {error}")


# К одной функции можно применить несколько декораторов.
def first_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Первый: начало")
        result = function(*args, **kwargs)
        print("Первый: конец")
        return result

    return wrapper


def second_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Второй: начало")
        result = function(*args, **kwargs)
        print("Второй: конец")
        return result

    return wrapper


@first_decorator
@second_decorator
def show_message():
    print("Тело исходной функции")


print("\nНесколько декораторов:")
show_message()


# Применение:
# show_message = first_decorator(second_decorator(show_message))
#
# Порядок вывода:
# Первый: начало
# Второй: начало
# Тело исходной функции
# Второй: конец
# Первый: конец


# Фабрика декораторов принимает настройки и возвращает декоратор.
# repeat(times) получает настройку.
# decorator(function) получает функцию.
# wrapper(*args, **kwargs) получает аргументы вызова.
def repeat(times):
    if not isinstance(times, int) or isinstance(times, bool):
        raise TypeError("Количество повторений должно быть целым числом")

    if times < 1:
        raise ValueError("Количество повторений должно быть больше нуля")

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def create_greeting(name):
    print(f"Создаём приветствие для {name!r}")
    return f"Hello, {name}!"


print("\nДекоратор с параметром:")
result = create_greeting("Roman")
print(f"Результат последнего вызова: {result!r}")

# Исходная функция вызывается три раза.
# Обёртка возвращает результат последнего вызова.
# Запись @repeat(3) эквивалентна:
# create_greeting = repeat(3)(create_greeting)


# Ошибка в настройке возникает при вызове фабрики декоратора.
print("\nНеверный параметр декоратора:")

try:
    repeat(0)
except ValueError as error:
    print(f"repeat(0) -> {type(error).__name__}: {error}")


# Замыкание внутри декоратора может хранить состояние.
def count_calls(function):
    calls = 0

    @wraps(function)
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"Количество вызовов {function.__name__!r}: {calls!r}")
        return function(*args, **kwargs)

    return wrapper


@count_calls
def square(number):
    return number ** 2


print("\nПодсчёт вызовов:")
print(f"square(3) -> {square(3)!r}")
print(f"square(4) -> {square(4)!r}")
print(f"square(5) -> {square(5)!r}")


# Счётчик увеличивается перед вызовом исходной функции.
# Поэтому учитывает и вызовы, закончившиеся исключением.


# Для измерения длительности используем perf_counter().
# finally позволяет вывести время и при исключении.
def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        started_at = perf_counter()

        try:
            return function(*args, **kwargs)
        finally:
            elapsed = perf_counter() - started_at
            print(f"Время {function.__name__!r}: {elapsed:.6f} секунд")

    return wrapper


@measure_time
def calculate_sum(limit):
    return sum(range(limit))


limit = 100_000

print("\nИзмерение времени:")
print(f"Исходная граница range: {limit!r}")

result = calculate_sum(limit)

print(f"Результат вычисления: {result!r}")

# Время зависит от компьютера и меняется между запусками.


# Главное:
# декоратор применяется при выполнении определения функции;
# wrapper выполняется при вызове декорированной функции;
# аргументы нужно передать исходной функции;
# возвращаемый результат нужно явно сохранить через return;
# wraps сохраняет основные метаданные;
# несколько декораторов применяются снизу вверх;
# настройки декоратора и аргументы функции — разные вещи.
