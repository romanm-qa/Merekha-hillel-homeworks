# *args собирает дополнительные позиционные аргументы в кортеж.
# Даже один аргумент будет упакован в кортеж.
def collect_args(*args):
    return args


print("Упаковка позиционных аргументов:")
print(f"collect_args(10, 20, 30) -> {collect_args(10, 20, 30)!r}")
print(f"collect_args(10) -> {collect_args(10)!r}")
print(f"collect_args() -> {collect_args()!r}")

# Если передать список без *, он станет одним аргументом.
numbers = [10, 20, 30]

print("\nПередача списка одним аргументом:")
print(f"Исходный список: {numbers!r}")
print(f"collect_args(numbers) -> {collect_args(numbers)!r}")


# args — обычный кортеж: его можно перебирать и передавать в sum().
def sum_numbers(*args):
    return sum(args)


print("\nРабота с упакованными аргументами:")
print(f"sum_numbers(10, 20, 30) -> {sum_numbers(10, 20, 30)!r}")
print(f"sum_numbers() -> {sum_numbers()!r}")


# Обычные параметры получают свои значения первыми.
# Оставшиеся позиционные аргументы попадают в args.
def collect_remaining(first, *args):
    return first, args


print("\nОбычный параметр перед *args:")
print(f"collect_remaining(10, 20, 30) -> {collect_remaining(10, 20, 30)!r}")
print(f"collect_remaining(10) -> {collect_remaining(10)!r}")


# **kwargs собирает дополнительные именованные аргументы в словарь.
def collect_kwargs(**kwargs):
    return kwargs


print("\nУпаковка именованных аргументов:")
print(
    f"collect_kwargs(name='Roman', age=29) -> "
    f"{collect_kwargs(name='Roman', age=29)!r}"
)
print(f"collect_kwargs() -> {collect_kwargs()!r}")


# Обычные параметры забирают соответствующие аргументы.
# В kwargs попадают только оставшиеся именованные аргументы.
def create_profile(name, **kwargs):
    return name, kwargs


print("\nОбычный параметр перед **kwargs:")
print(
    f"create_profile(name='Roman', age=29, role='student') -> "
    f"{create_profile(name='Roman', age=29, role='student')!r}"
)


# args и kwargs — принятые имена, но не ключевые слова.
# Поведение определяют звёздочки, а не названия параметров.
def collect_values(*values, **options):
    return values, options


print("\nДругие имена параметров:")
print(
    f"collect_values(10, 20, language='Python') -> "
    f"{collect_values(10, 20, language='Python')!r}"
)


# *args и **kwargs можно использовать вместе.
def collect_arguments(*args, **kwargs):
    return args, kwargs


print("\nСовместная упаковка:")
print(
    f"collect_arguments(10, 20, name='Roman') -> "
    f"{collect_arguments(10, 20, name='Roman')!r}"
)
print(f"collect_arguments() -> {collect_arguments()!r}")


# Параметры после *args передаются только по имени.
# **kwargs располагается последним в определении функции.
def describe_order(customer, *items, delivery=False, **details):
    return customer, items, delivery, details


print("\nСочетание разных параметров:")
print(
    f"describe_order('Roman', 'book', 'pen', delivery=True, city='Kyiv') -> "
    f"{describe_order('Roman', 'book', 'pen', delivery=True, city='Kyiv')!r}"
)


# При вызове * распаковывает итерируемый объект
# в отдельные позиционные аргументы.
def add(first_number, second_number):
    return first_number + second_number


numbers = [10, 20]

print("\nРаспаковка списка:")
print(f"Исходный список: {numbers!r}")
print(f"add(*numbers) -> {add(*numbers)!r}")
print(f"collect_args(*numbers) -> {collect_args(*numbers)!r}")

# Распаковывать через * можно не только списки, но и другие
# итерируемые объекты: кортежи, строки, range.
values = (3, 4)
text = "cat"

print("\nРаспаковка других итерируемых объектов:")
print(f"Исходный кортеж: {values!r}")
print(f"add(*values) -> {add(*values)!r}")
print(f"Исходная строка: {text!r}")
print(f"collect_args(*text) -> {collect_args(*text)!r}")
print(f"collect_args(*range(3)) -> {collect_args(*range(3))!r}")

# При вызове ** распаковывает отображение, например словарь,
# в именованные аргументы. Его ключи должны быть строками.
data = {"first_number": 10, "second_number": 20}

print("\nРаспаковка словаря в именованные аргументы:")
print(f"Исходный словарь: {data!r}")
print(f"add(**data) -> {add(**data)!r}")

# Одна звёздочка у словаря распаковывает его ключи.
data = {"name": "Roman", "age": 29}

print("\nРазница между *data и **data:")
print(f"Исходный словарь: {data!r}")
print(f"collect_args(*data) -> {collect_args(*data)!r}")
print(f"collect_kwargs(**data) -> {collect_kwargs(**data)!r}")

# В одном вызове можно распаковать несколько объектов.
first_values = [10, 20]
second_values = (30, 40)

print("\nРаспаковка нескольких последовательностей:")
print(f"Первый объект: {first_values!r}")
print(f"Второй объект: {second_values!r}")
print(
    f"collect_args(*first_values, *second_values) -> "
    f"{collect_args(*first_values, *second_values)!r}"
)

# Ключи разных словарей при передаче через ** не должны повторяться.
personal_data = {"name": "Roman"}
extra_data = {"age": 29, "role": "student"}

print("\nРаспаковка нескольких словарей:")
print(f"Первый словарь: {personal_data!r}")
print(f"Второй словарь: {extra_data!r}")
print(
    f"collect_kwargs(**personal_data, **extra_data) -> "
    f"{collect_kwargs(**personal_data, **extra_data)!r}"
)

# После распаковки действуют обычные правила вызова функции:
# количество и имена аргументов должны подходить её параметрам.
numbers = [10, 20, 30]

print("\nЛишний аргумент после распаковки:")
print(f"Исходный список: {numbers!r}")

try:
    add(*numbers)
except TypeError as error:
    print(f"add(*numbers) -> {type(error).__name__}: {error}")

# Неизвестный параметр тоже вызывает TypeError,
# если функция не собирает дополнительные аргументы через **kwargs.
data = {"first_number": 10, "amount": 20}

print("\nНеизвестное имя после распаковки:")
print(f"Исходный словарь: {data!r}")

try:
    add(**data)
except TypeError as error:
    print(f"add(**data) -> {type(error).__name__}: {error}")

# Повторная передача одного имени при вызове вызывает TypeError.
data = {"name": "Roman"}

print("\nПовторяющиеся именованные аргументы:")
print(f"Исходный словарь: {data!r}")

try:
    collect_kwargs(name="Alex", **data)
except TypeError as error:
    print(
        f"collect_kwargs(name='Alex', **data) -> "
        f"{type(error).__name__}: {error}"
    )

# Для ** ключи должны быть строками.
data = {1: "Roman"}

print("\nНестроковый ключ при распаковке через **:")
print(f"Исходный словарь: {data!r}")

try:
    collect_kwargs(**data)
except TypeError as error:
    print(f"collect_kwargs(**data) -> {type(error).__name__}: {error}")

# Одна звёздочка требует итерируемый объект.
number = 5

print("\nПопытка распаковать число:")
print(f"Исходное число: {number!r}")

try:
    collect_args(*number)
except TypeError as error:
    print(f"collect_args(*number) -> {type(error).__name__}: {error}")


# Функция-посредник может собрать аргументы,
# а затем распаковать их при вызове другой функции.
def call_function(function, *args, **kwargs):
    return function(*args, **kwargs)


print("\nПередача аргументов через функцию-посредник:")
print(f"call_function(add, 10, 20) -> {call_function(add, 10, 20)!r}")
print(
    f"call_function(add, first_number=10, second_number=20) -> "
    f"{call_function(add, first_number=10, second_number=20)!r}"
)

# В определении функции звёздочки УПАКОВЫВАЮТ аргументы.
# При вызове функции звёздочки РАСПАКОВЫВАЮТ объекты.
#
# *args и **kwargs нужны, когда функция действительно должна
# принимать переменное количество аргументов.
# Они не делают функцию автоматически безопаснее:
# для известных входных данных понятнее явно назвать параметры.
