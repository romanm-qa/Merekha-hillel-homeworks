# Список хранит элементы по порядку. В нём могут быть значения разных типов.
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "orange"]
mixed = [1, "Python", 3.14, True]
empty_list = []

print("Создание списков:")
print(f"Список чисел: {numbers!r}")
print(f"Список строк: {fruits!r}")
print(f"Список с разными типами: {mixed!r}")
print(f"Пустой список: {empty_list!r}")

# Индексы начинаются с 0. Обращение к несуществующему индексу вызывает IndexError.
fruits = ["apple", "banana", "orange", "kiwi"]

print("\nДоступ по индексу:")
print(f"Исходный список: {fruits!r}")
print(f"fruits[0] -> {fruits[0]!r}")
print(f"fruits[1] -> {fruits[1]!r}")
print(f"fruits[3] -> {fruits[3]!r}")

# Отрицательные индексы отсчитываются с конца: -1 — последний элемент.
print("\nОтрицательные индексы:")
print(f"Исходный список: {fruits!r}")
print(f"fruits[-1] -> {fruits[-1]!r}")
print(f"fruits[-2] -> {fruits[-2]!r}")
print(f"fruits[-3] -> {fruits[-3]!r}")

# Список изменяемый: присваивание по индексу заменяет элемент в самом списке.
print("\nИзменение элемента:")
print(f"До изменения: {fruits!r}")
fruits[1] = "pear"
print(f"После fruits[1] = 'pear': {fruits!r}")

# Срез [start:stop] включает start, но не включает stop.
# Срез создаёт новый список; для вложенных изменяемых элементов копия будет поверхностной.
numbers = [10, 20, 30, 40, 50, 60]
numbers_copy = numbers[:]

print("\nСрезы:")
print(f"Исходный список: {numbers!r}")
print(f"numbers[1:4] -> {numbers[1:4]!r}")
print(f"numbers[:3] -> {numbers[:3]!r}")
print(f"numbers[2:] -> {numbers[2:]!r}")
print(f"numbers[:] -> {numbers_copy!r}")
print(f"numbers_copy is numbers -> {numbers_copy is numbers!r}")

# Третий аргумент среза — шаг: [start:stop:step].
print("\nСрезы с шагом:")
print(f"Исходный список: {numbers!r}")
print(f"numbers[::2] -> {numbers[::2]!r}")
print(f"numbers[1::2] -> {numbers[1::2]!r}")

# Отрицательный шаг идёт справа налево. Срез [::-1] не меняет исходный список.
reversed_numbers = numbers[::-1]

print("\nРазворот через срез:")
print(f"Исходный список: {numbers!r}")
print(f"numbers[::-1] -> {reversed_numbers!r}")
print(f"Исходный список после среза: {numbers!r}")
