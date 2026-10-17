from functools import reduce


# Функция — объект: её можно сохранить в переменной,
# передать другой функции, вернуть или положить в коллекцию.
# Без скобок получаем саму функцию, со скобками — вызываем её.
def square(number):
    return number ** 2


operation = square

print("Функция в переменной:")
print(f"operation is square -> {operation is square!r}")
print(f"operation.__name__ -> {operation.__name__!r}")
print(f"operation(5) -> {operation(5)!r}")

result = square(5)

print(f"Результат вызова square(5): {result!r}")
print(f"Тип результата: {type(result).__name__}")


# Переданная функция вызывается внутри другой функции.
def apply_function(function, value):
    return function(value)


print("\nПередача функции как аргумента:")
print(f"apply_function(square, 5) -> {apply_function(square, 5)!r}")
print(f"apply_function(abs, -10) -> {apply_function(abs, -10)!r}")


# Функции можно хранить в коллекциях.
def cube(number):
    return number ** 3


operations = {
    "square": square,
    "cube": cube,
}

print("\nФункции в словаре:")
print(f"Названия операций: {list(operations)!r}")
print(f"operations['square'](3) -> {operations['square'](3)!r}")
print(f"operations['cube'](3) -> {operations['cube'](3)!r}")


# Функция может вернуть другую функцию, не вызывая её.
def get_operation():
    return square


selected_operation = get_operation()

print("\nВозврат функции:")
print(f"selected_operation is square -> {selected_operation is square!r}")
print(f"selected_operation(4) -> {selected_operation(4)!r}")

# lambda создаёт функцию из одного выражения.
# Результат выражения возвращается автоматически, без return.
# Здесь присваивание имени используется для сравнения с def.
square_lambda = lambda number: number ** 2

print("\nLambda-функция:")
print(f"square(5) -> {square(5)!r}")
print(f"square_lambda(5) -> {square_lambda(5)!r}")

# Если функции нужно постоянное имя, обычно лучше использовать def.
# lambda удобна для короткой операции прямо в месте передачи.


# Lambda может принимать несколько аргументов.
print("\nLambda с двумя аргументами:")
print(
    f"apply_function(lambda pair: pair[0] + pair[1], (10, 20)) -> "
    f"{apply_function(lambda pair: pair[0] + pair[1], (10, 20))!r}"
)

add_lambda = lambda first_number, second_number: first_number + second_number

print(f"add_lambda(10, 20) -> {add_lambda(10, 20)!r}")

# Условное выражение тоже является одним выражением.
describe_number = lambda number: "Чётное" if number % 2 == 0 else "Нечётное"

print("\nУсловное выражение в lambda:")
print(f"describe_number(4) -> {describe_number(4)!r}")
print(f"describe_number(5) -> {describe_number(5)!r}")

# key получает функцию, которая вычисляет ключ для каждого элемента.
# Передаём len без скобок: sorted() сам вызовет её для элементов.
words = ["pear", "fig", "banana", "kiwi"]

print("\nСортировка с готовой функцией:")
print(f"Исходный список: {words!r}")
print(f"sorted(words, key=len) -> {sorted(words, key=len)!r}")
print(f"Исходный список после сортировки: {words!r}")

# sorted() возвращает новый список.
# Элементы с одинаковыми ключами сохраняют взаимный порядок.


# Через lambda можно выбрать поле для сортировки.
students = [
    ("Roman", 90),
    ("Alex", 85),
    ("Kate", 95),
]

print("\nСортировка по второму элементу кортежа:")
print(f"Исходный список: {students!r}")

sorted_students = sorted(students, key=lambda student: student[1])

print(f"По возрастанию баллов: {sorted_students!r}")
print(
    f"По убыванию баллов: "
    f"{sorted(students, key=lambda student: student[1], reverse=True)!r}"
)
print(f"Исходный список после sorted(): {students!r}")

# list.sort() тоже принимает key, но изменяет исходный список.
# Сам метод возвращает None.
students_copy = students.copy()

print("\nСортировка на месте:")
print(f"Исходный список: {students_copy!r}")

sort_result = students_copy.sort(key=lambda student: student[1])

print(f"Список после sort(): {students_copy!r}")
print(f"Результат метода sort(): {sort_result!r}")

# map() применяет функцию к элементам и возвращает итератор.
# Вычисления происходят по мере получения элементов.
numbers = [1, 2, 3, 4]

print("\nПреобразование через map():")
print(f"Исходный список: {numbers!r}")

squares = map(square, numbers)

print(f"Тип результата: {type(squares).__name__}")
print(f"Первый list(squares) -> {list(squares)!r}")
print(f"Повторный list(squares) -> {list(squares)!r}")

# Итератор уже исчерпан, поэтому повторный обход даёт пустой список.


# Lambda можно передать непосредственно в map().
print("\nmap() с lambda:")
print(f"Исходный список: {numbers!r}")
print(
    f"list(map(lambda number: number * 2, numbers)) -> "
    f"{list(map(lambda number: number * 2, numbers))!r}"
)

# Для простого преобразования часто удобен list comprehension.
print(f"[number * 2 for number in numbers] -> {[number * 2 for number in numbers]!r}")

# filter() оставляет элементы, для которых результат функции истинен.
# Результат проверки не обязан быть именно объектом True.
# filter() возвращает итератор.
numbers = [3, -1, 0, 8, -5, 2]

print("\nОтбор элементов через filter():")
print(f"Исходный список: {numbers!r}")

positive_numbers = filter(lambda number: number > 0, numbers)

print(f"Тип результата: {type(positive_numbers).__name__}")
print(f"list(positive_numbers) -> {list(positive_numbers)!r}")
print(
    f"[number for number in numbers if number > 0] -> "
    f"{[number for number in numbers if number > 0]!r}"
)

# filter(None, values) оставляет только истинные элементы.
values = [0, "", None, False, [], 10, "Python", [0]]

print("\nfilter() без функции проверки:")
print(f"Исходный список: {values!r}")
print(f"list(filter(None, values)) -> {list(filter(None, values))!r}")

# [0] остаётся: непустой список истинен, хотя его элемент равен 0.


# reduce() сводит элементы к результату через функцию двух аргументов.
# На каждом шаге передаёт накопленный результат и следующий элемент.
numbers = [1, 2, 3, 4]

print("\nСвёртка через reduce():")
print(f"Исходный список: {numbers!r}")

total = reduce(lambda accumulated, number: accumulated + number, numbers)

print(f"Сумма через reduce(): {total!r}")
print(f"Сумма через sum(): {sum(numbers)!r}")

# Здесь шаги: 1 + 2 -> 3; 3 + 3 -> 6; 6 + 4 -> 10.
# Для обычного сложения проще использовать sum().


# Начальное значение становится первым накопленным результатом.
# Для пустого объекта reduce() возвращает это значение.
print("\nНачальное значение reduce():")
print(f"Исходный список: {numbers!r}")
print(
    f"reduce(..., numbers, 10) -> "
    f"{reduce(lambda accumulated, number: accumulated + number, numbers, 10)!r}"
)
print(
    f"reduce(..., [], 0) -> "
    f"{reduce(lambda accumulated, number: accumulated + number, [], 0)!r}"
)

# Пустой объект без начального значения вызывает TypeError.
print("\nreduce() с пустым списком без начального значения:")

try:
    reduce(lambda accumulated, number: accumulated + number, [])
except TypeError as error:
    print(f"reduce(..., []) -> {type(error).__name__}: {error}")

# all() проверяет, все ли элементы истинны.
# any() проверяет, есть ли хотя бы один истинный элемент.
values = [1, "Python", 0]

print("\nПроверка истинности элементов:")
print(f"Исходный список: {values!r}")
print(f"all(values) -> {all(values)!r}")
print(f"any(values) -> {any(values)!r}")

# Пустой список сам по себе ложен.
# Но all([]) возвращает True: в нём нет ни одного ложного элемента.
# any([]) возвращает False: в нём нет ни одного истинного элемента.
values = []

print("\nПустой список: bool, all и any:")
print(f"Исходный список: {values!r}")
print(f"bool(values) -> {bool(values)!r}")
print(f"all(values) -> {all(values)!r}")
print(f"any(values) -> {any(values)!r}")

# all() останавливается на первом ложном элементе.
# any() останавливается на первом истинном элементе.
# Если им передать итератор, он может быть использован лишь частично.


# Главное:
# function — сама функция, function() — её вызов;
# функции можно передавать и возвращать как другие объекты;
# lambda содержит одно выражение и автоматически возвращает результат;
# key принимает функцию для вычисления ключей сортировки;
# map() преобразует, filter() отбирает, reduce() накапливает результат;
# all() и any() проверяют истинность элементов.
