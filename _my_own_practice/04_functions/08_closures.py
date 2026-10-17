# Вложенную функцию можно создать и вызвать внутри другой функции.
# Само наличие вложенной функции ещё не означает замыкание.
def call_inner_function():
    def say_hello():
        return "Hello!"

    return say_hello()


print("Вложенная функция:")
print(f"call_inner_function() -> {call_inner_function()!r}")


# Замыкание — функция, сохраняющая доступ к переменным
# из области внешней функции.
# Этот доступ может сохраняться после завершения внешней функции.
def create_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"

    return greet


say_hello = create_greeting("Hello")

print("\nСоздание замыкания:")
print(f"Тип say_hello: {type(say_hello).__name__}")
print(f"say_hello('Roman') -> {say_hello('Roman')!r}")
print(f"say_hello('Alex') -> {say_hello('Alex')!r}")

# create_greeting("Hello") уже завершилась.
# Возвращённая функция продолжает использовать greeting.


# return greet возвращает функцию, не вызывая её.
# greet(name) вызывает функцию и возвращает результат её работы.
print("\nФункция и результат её вызова:")
print(f"Имя функции: {say_hello.__name__!r}")

message = say_hello("Kate")

print(f"Результат вызова: {message!r}")
print(f"Тип результата: {type(message).__name__}")

# Каждый вызов фабрики создаёт отдельную функцию
# со своей связью с параметром greeting.
say_hi = create_greeting("Hi")
say_good_morning = create_greeting("Good morning")

print("\nРазные замыкания:")
print(f"say_hi('Roman') -> {say_hi('Roman')!r}")
print(f"say_good_morning('Roman') -> {say_good_morning('Roman')!r}")
print(f"say_hi is say_good_morning -> {say_hi is say_good_morning!r}")


# Через замыкание можно сохранить настройку для будущих вызовов.
def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply


multiply_by_two = create_multiplier(2)
multiply_by_five = create_multiplier(5)

print("\nСохранение множителя:")
print(f"multiply_by_two(10) -> {multiply_by_two(10)!r}")
print(f"multiply_by_five(10) -> {multiply_by_five(10)!r}")
print(f"multiply_by_two(3) -> {multiply_by_two(3)!r}")


# Для чтения внешней переменной nonlocal не требуется.
# Для переприсваивания этой переменной используем nonlocal.
def create_counter(start=0):
    count = start

    def increase():
        nonlocal count
        count += 1
        return count

    return increase


counter = create_counter()

print("\nСохранение состояния между вызовами:")
print(f"Первый counter() -> {counter()!r}")
print(f"Второй counter() -> {counter()!r}")
print(f"Третий counter() -> {counter()!r}")

# count не создаётся заново при каждом вызове counter().
# Новое состояние создаётся при новом вызове create_counter().


# Счётчики, созданные разными вызовами фабрики,
# имеют отдельные переменные count.
first_counter = create_counter()
second_counter = create_counter(10)

print("\nНезависимые счётчики:")
print(f"first_counter() -> {first_counter()!r}")
print(f"first_counter() -> {first_counter()!r}")
print(f"second_counter() -> {second_counter()!r}")
print(f"first_counter() -> {first_counter()!r}")
print(f"second_counter() -> {second_counter()!r}")


# Для изменения самого списка nonlocal не нужен.
# Имя items не переприсваивается: меняется объект через append().
def create_collector():
    items = []

    def collect(item):
        items.append(item)
        return items.copy()

    return collect


collect = create_collector()

print("\nИзменяемый объект в замыкании:")
print(f"collect('Python') -> {collect('Python')!r}")
print(f"collect('SQL') -> {collect('SQL')!r}")
print(f"collect('Git') -> {collect('Git')!r}")


# Возвращаем копию списка, чтобы снаружи не получить
# прямой доступ к самому списку, хранящему состояние.
# Копия поверхностная: вложенные изменяемые объекты остаются общими.


# Две функции из одного вызова фабрики могут разделять состояние.
def create_counter_controls():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    def reset():
        nonlocal count
        count = 0

    return increase, reset


increase, reset = create_counter_controls()

print("\nОбщее состояние двух функций:")
print(f"increase() -> {increase()!r}")
print(f"increase() -> {increase()!r}")
print(f"reset() -> {reset()!r}")
print(f"increase() после reset() -> {increase()!r}")


# Замыкание сохраняет доступ к переменной,
# а не обязательно фиксирует её значение в момент создания функции.
def create_message_reader():
    message = "Before"

    def read_message():
        return message

    message = "After"
    return read_message


read_message = create_message_reader()

print("\nЧтение изменённой внешней переменной:")
print(f"read_message() -> {read_message()!r}")


# Это важно при создании функций в цикле.
# Все функции ниже используют одну переменную number.
def create_multipliers():
    functions = []

    for number in range(1, 4):
        def multiply(value):
            return value * number

        functions.append(multiply)

    return functions


multipliers = create_multipliers()

print("\nПозднее связывание в замыканиях:")
print(f"Множители в цикле: {list(range(1, 4))!r}")

for position, function in enumerate(multipliers, start=1):
    print(f"Функция {position}: function(10) -> {function(10)!r}")


# Все три вызова возвращают 30.
# На момент вызовов цикл завершён, number равен 3.


# Отдельный вызов фабрики создаёт отдельную переменную multiplier.
# Используем уже определённую create_multiplier().
def create_independent_multipliers():
    functions = []

    for number in range(1, 4):
        functions.append(create_multiplier(number))

    return functions


multipliers = create_independent_multipliers()

print("\nОтдельное замыкание для каждого множителя:")
print(f"Множители в цикле: {list(range(1, 4))!r}")

for position, function in enumerate(multipliers, start=1):
    print(f"Функция {position}: function(10) -> {function(10)!r}")


# Теперь результаты: 10, 20, 30.


# Другой способ сохранить текущее значение —
# использовать параметр со значением по умолчанию.
# Оно вычисляется при выполнении каждого def.
def create_multipliers_with_defaults():
    functions = []

    for number in range(1, 4):
        def multiply(value, multiplier=number):
            return value * multiplier

        functions.append(multiply)

    return functions


multipliers = create_multipliers_with_defaults()

print("\nФиксация значения через параметр по умолчанию:")
print(f"Множители в цикле: {list(range(1, 4))!r}")

for position, function in enumerate(multipliers, start=1):
    print(f"Функция {position}: function(10) -> {function(10)!r}")


# Здесь multiplier — локальный параметр.
# Для хранения множителя замыкание не используется.


# Внешняя функция не обязана возвращать замыкание.
# Например, она может сохранить его в переданном списке.
def register_greeting(functions, greeting):
    def greet(name):
        return f"{greeting}, {name}!"

    functions.append(greet)


greetings = []
register_greeting(greetings, "Welcome")

print("\nСохранение замыкания в коллекции:")
print(f"Количество сохранённых функций: {len(greetings)!r}")
print(f"greetings[0]('Roman') -> {greetings[0]('Roman')!r}")

# Главное:
# замыкание сохраняет доступ к переменным внешней функции;
# возвращение внутренней функции — частый, но не обязательный способ;
# nonlocal нужен для переприсваивания внешнего имени;
# изменение объекта само по себе не требует nonlocal;
# функции могут разделять состояние или иметь отдельное;
# при создании функций в цикле учитываем позднее связывание.
