# Пространства имён и области видимости в Python

## 1. Что такое пространство имён

**Пространство имён (namespace)** — это структура, в которой Python хранит соответствие между именами и объектами.

Упрощённо его можно представить как словарь:

```python
{
    "name": "Roman",
    "age": 29,
    "print": <built-in function print>
}
```

Когда Python встречает имя переменной или функции, он ищет объект, связанный с этим именем.

```python
user_name = "Roman"

print(user_name)
```

Здесь:

- `user_name` — имя;
- `"Roman"` — объект, на который ссылается имя;
- связь между ними хранится в пространстве имён.

---

## 2. Зачем нужны пространства имён

Пространства имён позволяют использовать одинаковые имена в разных частях программы.

```python
name = "Global Roman"


def show_name():
    name = "Local Roman"
    print(name)


show_name()
print(name)
```

Результат:

```text
Local Roman
Global Roman
```

Переменные имеют одинаковое имя `name`, но находятся в разных пространствах имён и поэтому не конфликтуют.

---

## 3. Виды пространств имён

В Python существуют следующие основные пространства имён:

- **Built-in** — встроенное пространство имён;
- **Global** — глобальное пространство имён;
- **Enclosing** — пространство внешней функции;
- **Local** — локальное пространство функции.

Они образуют правило поиска имён **LEGB**:

```text
Local → Enclosing → Global → Built-in
```

---

## 4. Built-in namespace

**Built-in namespace** содержит встроенные объекты Python.

Например:

- `print()`;
- `len()`;
- `sum()`;
- `max()`;
- `min()`;
- `range()`;
- `str`;
- `int`;
- `list`;
- `dict`.

```python
numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
```

Результат:

```text
3
60
```

Эти функции доступны без импорта, потому что находятся во встроенном пространстве имён.

### Не стоит переопределять встроенные имена

```python
list = [1, 2, 3]
```

После этого имя `list` больше не ссылается на встроенный тип:

```python
numbers = list((4, 5, 6))
```

Программа завершится ошибкой, потому что теперь `list` — обычный список, а не встроенная функция.

Лучше использовать другое имя:

```python
numbers_list = [1, 2, 3]
```

---

## 5. Global namespace

**Глобальное пространство имён** создаётся при запуске Python-файла.

В нём находятся переменные, функции и классы, объявленные на верхнем уровне файла.

```python
course_name = "Python"


def show_course():
    print(course_name)


show_course()
```

Переменная `course_name` является глобальной, потому что создана вне функции.

Функция может читать глобальную переменную.

Результат:

```text
Python
```

---

## 6. Local namespace

**Локальное пространство имён** создаётся при вызове функции.

В нём находятся:

- параметры функции;
- переменные, созданные внутри функции.

```python
def greet(user_name):
    message = f"Hello, {user_name}!"
    print(message)


greet("Roman")
```

Здесь `user_name` и `message` существуют только внутри функции `greet()`.

```python
def create_message():
    message = "Hello!"


create_message()
print(message)
```

Результат:

```text
NameError: name 'message' is not defined
```

После завершения функции её локальное пространство имён обычно уничтожается.

---

## 7. Локальная и глобальная переменные с одинаковым именем

```python
language = "Python"


def show_language():
    language = "Java"
    print(language)


show_language()
print(language)
```

Результат:

```text
Java
Python
```

Внутри функции Python находит локальную переменную `language`.

Глобальная переменная при этом не изменяется.

---

## 8. Enclosing namespace

**Enclosing namespace** появляется, когда одна функция находится внутри другой.

```python
def outer_function():
    message = "Message from outer function"

    def inner_function():
        print(message)

    inner_function()


outer_function()
```

Переменная `message`:

- не локальная для `inner_function()`;
- находится во внешней функции `outer_function()`;
- относится к области **Enclosing**.

Результат:

```text
Message from outer function
```

---

## 9. Область видимости

**Область видимости (scope)** — это часть программы, в которой определённое имя доступно.

Важно различать:

- **namespace** — где хранятся имена;
- **scope** — откуда к этим именам можно обратиться.

```python
global_number = 10


def calculate():
    local_number = 20
    print(global_number)
    print(local_number)


calculate()
```

Внутри функции доступны обе переменные:

```text
10
20
```

Но снаружи локальная переменная недоступна:

```python
print(local_number)
```

Результат:

```text
NameError: name 'local_number' is not defined
```

---

## 10. Правило LEGB

Python ищет имена в определённом порядке:

```text
L — Local
E — Enclosing
G — Global
B — Built-in
```

То есть поиск выполняется так:

1. внутри текущей функции;
2. во внешней функции;
3. в глобальной области файла;
4. среди встроенных объектов Python.

---

## 11. Пример работы правила LEGB

```python
name = "Global"


def outer_function():
    name = "Enclosing"

    def inner_function():
        name = "Local"
        print(name)

    inner_function()


outer_function()
```

Результат:

```text
Local
```

Python находит имя в локальной области и прекращает поиск.

Если удалить локальную переменную:

```python
name = "Global"


def outer_function():
    name = "Enclosing"

    def inner_function():
        print(name)

    inner_function()


outer_function()
```

Результат:

```text
Enclosing
```

Если удалить переменную из внешней функции:

```python
name = "Global"


def outer_function():
    def inner_function():
        print(name)

    inner_function()


outer_function()
```

Результат:

```text
Global
```

Если имя не найдено ни в одной области, Python проверяет встроенное пространство имён.

```python
def show_length():
    print(len("Python"))


show_length()
```

Результат:

```text
6
```

---

## 12. Функция globals()

Функция `globals()` возвращает словарь глобального пространства имён.

```python
course_name = "Python"

print(globals())
```

В полученном словаре можно найти созданную переменную:

```python
print(globals()["course_name"])
```

Результат:

```text
Python
```

Через `globals()` можно добавить новое глобальное имя:

```python
globals()["student_name"] = "Roman"

print(student_name)
```

Результат:

```text
Roman
```

Но изменять глобальные переменные таким способом обычно не рекомендуется: код становится сложнее понимать и поддерживать.

---

## 13. Функция locals()

Функция `locals()` возвращает словарь текущего локального пространства имён.

```python
def show_local_namespace():
    user_name = "Roman"
    user_age = 29

    print(locals())


show_local_namespace()
```

Пример результата:

```text
{'user_name': 'Roman', 'user_age': 29}
```

Вне функции `locals()` показывает текущую таблицу локальных имён. На уровне модуля локальное и глобальное пространства фактически совпадают.

---

## 14. Сравнение globals() и locals()

```python
global_variable = "Global value"


def inspect_namespaces():
    local_variable = "Local value"

    print("Global:", "global_variable" in globals())
    print("Local:", "local_variable" in locals())


inspect_namespaces()
```

Результат:

```text
Global: True
Local: True
```

`globals()` используется для просмотра глобального пространства имён, а `locals()` — текущего локального пространства.

---

## 15. Изменение глобальной переменной внутри функции

Функция может читать глобальную переменную:

```python
counter = 10


def show_counter():
    print(counter)


show_counter()
```

Но попытка изменить её без дополнительного указания создаёт проблему:

```python
counter = 10


def increase_counter():
    counter += 1


increase_counter()
```

Результат:

```text
UnboundLocalError
```

Поскольку внутри функции есть присваивание, Python считает `counter` локальной переменной.

Но значение этой локальной переменной пытаются прочитать до того, как оно было присвоено.

---

## 16. Ключевое слово global

Ключевое слово `global` сообщает Python, что внутри функции нужно использовать глобальную переменную.

```python
counter = 10


def increase_counter():
    global counter
    counter += 1


increase_counter()
print(counter)
```

Результат:

```text
11
```

Теперь функция изменяет глобальную переменную, а не создаёт локальную.

### Создание глобальной переменной внутри функции

```python
def create_global_variable():
    global message
    message = "Hello from function"


create_global_variable()
print(message)
```

Результат:

```text
Hello from function
```

Так делать можно, но обычно это ухудшает читаемость программы.

---

## 17. Ключевое слово nonlocal

Ключевое слово `nonlocal` используется во вложенных функциях.

Оно позволяет изменить переменную из области внешней функции.

```python
def outer_function():
    counter = 0

    def inner_function():
        nonlocal counter
        counter += 1

    inner_function()
    print(counter)


outer_function()
```

Результат:

```text
1
```

Без `nonlocal` внутри `inner_function()` была бы создана новая локальная переменная.

```python
def outer_function():
    message = "Outer"

    def inner_function():
        message = "Inner"
        print("Внутри:", message)

    inner_function()
    print("Снаружи:", message)


outer_function()
```

Результат:

```text
Внутри: Inner
Снаружи: Outer
```

С использованием `nonlocal`:

```python
def outer_function():
    message = "Outer"

    def inner_function():
        nonlocal message
        message = "Changed by inner function"

    inner_function()
    print(message)


outer_function()
```

Результат:

```text
Changed by inner function
```

---

## 18. Разница между global и nonlocal

| Ключевое слово | Какую переменную изменяет |
|---|---|
| `global` | Переменную из глобальной области файла |
| `nonlocal` | Переменную из ближайшей внешней функции |

Пример:

```python
value = "Global"


def outer_function():
    value = "Enclosing"

    def change_values():
        global value
        value = "Changed global"

    change_values()
    print("Enclosing:", value)


outer_function()
print("Global:", value)
```

Результат:

```text
Enclosing: Enclosing
Global: Changed global
```

Здесь `global value` относится именно к глобальной переменной, а не к переменной внешней функции.

---

## 19. Пространства имён и хеш-таблицы

Внутренне пространства имён Python реализованы с помощью структур, похожих на словари.

Словарь работает как **хеш-таблица**:

```python
student = {
    "name": "Roman",
    "age": 29
}
```

Python получает ключ, вычисляет его хеш и находит связанное значение.

Аналогично пространство имён связывает имена с объектами:

```text
"student" → объект словаря
"print" → встроенная функция
"course_name" → строка
```

Именно поэтому функции `globals()` и `locals()` возвращают словари.

---

## 20. Побочные эффекты при изменении внешних переменных

Изменение глобальной переменной внутри функции называется **побочным эффектом**.

```python
total = 0


def add_number(number):
    global total
    total += number


add_number(10)
add_number(20)

print(total)
```

Результат:

```text
30
```

Функция не только выполняет вычисление, но и изменяет состояние программы снаружи.

Такой код сложнее:

- тестировать;
- отлаживать;
- переиспользовать;
- понимать.

Чаще лучше вернуть новое значение:

```python
def add_number(current_total, number):
    return current_total + number


total = 0
total = add_number(total, 10)
total = add_number(total, 20)

print(total)
```

Результат:

```text
30
```

Теперь функция получает данные через параметры и возвращает результат явно.

---

## 21. Краткий итог

- **Пространство имён** хранит связь между именами и объектами.
- **Область видимости** определяет, где имя доступно.
- Python ищет имена по правилу **LEGB**.
- `Local` — текущая функция.
- `Enclosing` — внешняя функция.
- `Global` — текущий модуль или файл.
- `Built-in` — встроенные объекты Python.
- `globals()` возвращает глобальное пространство имён.
- `locals()` возвращает текущее локальное пространство имён.
- `global` позволяет изменить глобальную переменную.
- `nonlocal` позволяет изменить переменную внешней функции.
- Частое изменение внешнего состояния создаёт побочные эффекты и усложняет программу.

# Замыкания и декораторы в Python

## 1. Функции как объекты

В Python функция является объектом.

Это означает, что функцию можно:

- сохранить в переменную;
- передать в другую функцию;
- вернуть из другой функции;
- сохранить в коллекции.

```python
def greet():
    return "Hello!"


greeting_function = greet

print(greeting_function())
```

Результат:

```text
Hello!
```

Важно: мы записали функцию в переменную без круглых скобок:

```python
greeting_function = greet
```

Здесь передаётся сама функция.

Если поставить круглые скобки:

```python
greeting_message = greet()
```

В переменную будет записан результат вызова функции.

---

## 2. Передача функции в другую функцию

Функцию можно передать в другую функцию как обычный аргумент.

```python
def greet(name):
    return f"Hello, {name}!"


def execute_function(function, value):
    return function(value)


result = execute_function(greet, "Roman")

print(result)
```

Результат:

```text
Hello, Roman!
```

В функцию `execute_function()` передаётся:

- функция `greet`;
- значение `"Roman"`.

Внутри `execute_function()` переданная функция вызывается:

```python
function(value)
```

---

## 3. Вложенные функции

Внутри одной функции можно объявить другую функцию.

```python
def outer_function():
    def inner_function():
        print("Внутренняя функция")

    inner_function()


outer_function()
```

Результат:

```text
Внутренняя функция
```

Функция `inner_function()` доступна только внутри `outer_function()`.

Попытка вызвать её снаружи приведёт к ошибке:

```python
inner_function()
```

Результат:

```text
NameError: name 'inner_function' is not defined
```

---

# Замыкания

## 4. Что такое замыкание

**Замыкание (closure)** — это внутренняя функция, которая запоминает переменные из области внешней функции даже после завершения её работы.

Для создания замыкания обычно нужны три условия:

1. Одна функция находится внутри другой функции.
2. Внутренняя функция использует переменную внешней функции.
3. Внешняя функция возвращает внутреннюю функцию.

```python
def outer_function():
    message = "Hello from closure!"

    def inner_function():
        print(message)

    return inner_function


closure_function = outer_function()
closure_function()
```

Результат:

```text
Hello from closure!
```

Функция `outer_function()` уже завершила работу, но `inner_function()` продолжает помнить значение переменной `message`.

---

## 5. Как работает замыкание

Рассмотрим код по шагам:

```python
def create_greeting():
    greeting = "Hello"

    def greet(name):
        return f"{greeting}, {name}!"

    return greet
```

Вызываем внешнюю функцию:

```python
greeting_function = create_greeting()
```

Функция `create_greeting()` возвращает функцию `greet`, но не вызывает её.

Теперь переменная `greeting_function` хранит ссылку на внутреннюю функцию.

```python
print(greeting_function("Roman"))
```

Результат:

```text
Hello, Roman!
```

Внутренняя функция помнит значение `greeting`, находившееся во внешней области видимости.

---

## 6. Замыкание с параметром внешней функции

Переменная, которую запоминает замыкание, может быть параметром внешней функции.

```python
def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply


multiply_by_two = create_multiplier(2)
multiply_by_five = create_multiplier(5)

print(multiply_by_two(10))
print(multiply_by_five(10))
```

Результат:

```text
20
50
```

Каждое замыкание хранит собственное значение `multiplier`:

```text
multiply_by_two  → multiplier = 2
multiply_by_five → multiplier = 5
```

---

## 7. Сохранение состояния между вызовами

Замыкание может сохранять и изменять состояние между вызовами.

Для изменения переменной внешней функции используется `nonlocal`.

```python
def create_counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase


counter = create_counter()

print(counter())
print(counter())
print(counter())
```

Результат:

```text
1
2
3
```

Переменная `count` не создаётся заново при каждом вызове `counter()`.

Она сохраняется внутри замыкания.

---

## 8. Независимые замыкания

Каждый вызов внешней функции создаёт новое независимое замыкание.

```python
def create_counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase


first_counter = create_counter()
second_counter = create_counter()

print(first_counter())
print(first_counter())
print(second_counter())
print(first_counter())
print(second_counter())
```

Результат:

```text
1
2
1
3
2
```

У каждого счётчика собственная переменная `count`.

---

## 9. Практический пример замыкания

Создадим функцию для вычисления цены со скидкой.

```python
def create_discount(discount_percent):
    def calculate_price(price):
        discount = price * discount_percent / 100
        return price - discount

    return calculate_price


calculate_student_price = create_discount(10)
calculate_vip_price = create_discount(25)

print(calculate_student_price(1000))
print(calculate_vip_price(1000))
```

Результат:

```text
900.0
750.0
```

Вместо повторной передачи размера скидки мы создаём отдельную функцию с уже сохранённым значением.

---

# Декораторы

## 10. Что такое декоратор

**Декоратор** — это функция, которая принимает другую функцию, добавляет к ней новое поведение и возвращает новую функцию.

При этом код исходной функции изменять не нужно.

Декоратор можно представить так:

```text
Исходная функция
        ↓
     Декоратор
        ↓
Функция с дополнительным поведением
```

---

## 11. Простейший декоратор

```python
def decorator(function):
    def wrapper():
        print("Действие перед вызовом функции")

        function()

        print("Действие после вызова функции")

    return wrapper
```

Создадим функцию:

```python
def greet():
    print("Hello!")
```

Применим декоратор вручную:

```python
greet = decorator(greet)

greet()
```

Результат:

```text
Действие перед вызовом функции
Hello!
Действие после вызова функции
```

---

## 12. Как работает wrapper

Внутри декоратора обычно создаётся вложенная функция с именем `wrapper`.

```python
def decorator(function):
    def wrapper():
        print("Before")

        function()

        print("After")

    return wrapper
```

`wrapper()` выполняет три действия:

1. Запускает код перед исходной функцией.
2. Вызывает исходную функцию.
3. Запускает код после исходной функции.

После декорирования имя исходной функции начинает ссылаться на `wrapper`:

```python
greet = decorator(greet)
```

---

## 13. Синтаксис @decorator

Вместо ручной записи:

```python
greet = decorator(greet)
```

можно использовать специальный синтаксис `@`.

```python
def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper


@decorator
def greet():
    print("Hello!")


greet()
```

Результат:

```text
Before
Hello!
After
```

Запись:

```python
@decorator
def greet():
    ...
```

эквивалентна записи:

```python
def greet():
    ...


greet = decorator(greet)
```

---

## 14. Декоратор с возвращаемым значением

Если исходная функция возвращает значение, `wrapper()` тоже должен его вернуть.

```python
def decorator(function):
    def wrapper():
        print("Функция начала работу")

        result = function()

        print("Функция завершила работу")

        return result

    return wrapper


@decorator
def get_message():
    return "Hello, Roman!"


message = get_message()

print(message)
```

Результат:

```text
Функция начала работу
Функция завершила работу
Hello, Roman!
```

Если не написать:

```python
return result
```

декорированная функция вернёт `None`.

---

## 15. Декоратор для функции с аргументами

Если исходная функция принимает аргументы, `wrapper()` тоже должен их принимать.

```python
def decorator(function):
    def wrapper(name):
        print("Вызов функции")

        result = function(name)

        return result

    return wrapper


@decorator
def greet(name):
    return f"Hello, {name}!"


print(greet("Roman"))
```

Результат:

```text
Вызов функции
Hello, Roman!
```

Но такой декоратор подойдёт только функциям с одним параметром.

---

## 16. Универсальный декоратор с *args и **kwargs

Чтобы декоратор мог работать с разными функциями, используются `*args` и `**kwargs`.

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        print("Функция вызвана")

        result = function(*args, **kwargs)

        return result

    return wrapper
```

Применим его к функции с позиционными аргументами:

```python
@decorator
def add(first_number, second_number):
    return first_number + second_number


print(add(10, 20))
```

Результат:

```text
Функция вызвана
30
```

Применим тот же декоратор к функции с именованными аргументами:

```python
@decorator
def introduce(name, age):
    return f"My name is {name}. I am {age} years old."


print(introduce(name="Roman", age=29))
```

Результат:

```text
Функция вызвана
My name is Roman. I am 29 years old.
```

`*args` собирает позиционные аргументы, а `**kwargs` — именованные.

---

## 17. Декоратор для проверки аргументов

Декоратор может проверять данные до запуска функции.

```python
def validate_positive_numbers(function):
    def wrapper(*args, **kwargs):
        for number in args:
            if number < 0:
                raise ValueError("Числа должны быть положительными")

        return function(*args, **kwargs)

    return wrapper


@validate_positive_numbers
def add(first_number, second_number):
    return first_number + second_number


print(add(10, 20))
```

Результат:

```text
30
```

При передаче отрицательного числа:

```python
print(add(-10, 20))
```

Результат:

```text
ValueError: Числа должны быть положительными
```

---

## 18. Декоратор для измерения времени выполнения

Декораторы часто используются для измерения времени работы функций.

```python
import time


def measure_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Время выполнения: {execution_time:.5f} секунд")

        return result

    return wrapper


@measure_time
def calculate_sum():
    return sum(range(1_000_000))


print(calculate_sum())
```

Декоратор добавляет измерение времени, не изменяя код `calculate_sum()`.

---

## 19. Декоратор для подсчёта вызовов

Состояние можно хранить внутри замыкания декоратора.

```python
def count_calls(function):
    calls_count = 0

    def wrapper(*args, **kwargs):
        nonlocal calls_count
        calls_count += 1

        print(f"Количество вызовов: {calls_count}")

        return function(*args, **kwargs)

    return wrapper


@count_calls
def greet(name):
    return f"Hello, {name}!"


print(greet("Roman"))
print(greet("Alex"))
print(greet("Max"))
```

Результат:

```text
Количество вызовов: 1
Hello, Roman!
Количество вызовов: 2
Hello, Alex!
Количество вызовов: 3
Hello, Max!
```

Переменная `calls_count` сохраняется между вызовами благодаря замыканию.

---

## 20. Несколько декораторов

К одной функции можно применить несколько декораторов.

```python
def first_decorator(function):
    def wrapper(*args, **kwargs):
        print("Первый декоратор: начало")

        result = function(*args, **kwargs)

        print("Первый декоратор: конец")

        return result

    return wrapper


def second_decorator(function):
    def wrapper(*args, **kwargs):
        print("Второй декоратор: начало")

        result = function(*args, **kwargs)

        print("Второй декоратор: конец")

        return result

    return wrapper


@first_decorator
@second_decorator
def greet():
    print("Hello!")


greet()
```

Результат:

```text
Первый декоратор: начало
Второй декоратор: начало
Hello!
Второй декоратор: конец
Первый декоратор: конец
```

Декораторы применяются снизу вверх:

```python
greet = first_decorator(second_decorator(greet))
```

Но выполняются начиная с внешнего декоратора.

---

## 21. Декоратор с параметрами

Иногда параметры нужно передать самому декоратору.

Для этого используется ещё один уровень вложенности.

```python
def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator
```

Применение:

```python
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Roman")
```

Результат:

```text
Hello, Roman!
Hello, Roman!
Hello, Roman!
```

Здесь:

- `repeat(3)` получает параметры декоратора;
- `decorator(function)` получает исходную функцию;
- `wrapper(*args, **kwargs)` получает аргументы исходной функции.

---

## 22. Сохранение информации об исходной функции

После декорирования имя функции и её документация могут быть потеряны.

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@decorator
def greet():
    """Возвращает приветствие."""
    return "Hello!"


print(greet.__name__)
```

Результат:

```text
wrapper
```

Теперь Python считает, что функция называется `wrapper`.

Для сохранения информации используется `functools.wraps`.

```python
from functools import wraps


def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@decorator
def greet():
    """Возвращает приветствие."""
    return "Hello!"


print(greet.__name__)
print(greet.__doc__)
```

Результат:

```text
greet
Возвращает приветствие.
```

Поэтому в настоящих декораторах желательно использовать:

```python
@wraps(function)
```

---

## 23. Полный шаблон универсального декоратора

```python
from functools import wraps


def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Действия перед вызовом функции

        result = function(*args, **kwargs)

        # Действия после вызова функции

        return result

    return wrapper
```

Этот шаблон:

- принимает любую функцию;
- поддерживает позиционные аргументы;
- поддерживает именованные аргументы;
- сохраняет возвращаемое значение;
- сохраняет имя и документацию исходной функции.

---

## 24. Связь замыканий и декораторов

Декораторы работают благодаря нескольким возможностям Python:

1. Функции являются объектами.
2. Функции можно передавать как аргументы.
3. Функции можно возвращать из других функций.
4. Внутренние функции создают замыкания.
5. Замыкание сохраняет ссылку на исходную функцию.

```python
def decorator(function):
    def wrapper():
        function()

    return wrapper
```

Функция `wrapper()` запоминает переданную `function`, даже после завершения работы `decorator()`.

Поэтому декоратор является практическим применением замыкания.

---

## 25. Где применяются декораторы

Декораторы используются для добавления повторяющегося поведения:

- логирования;
- проверки аргументов;
- проверки доступа;
- авторизации;
- измерения времени выполнения;
- подсчёта вызовов;
- обработки исключений;
- кэширования результатов;
- повторного запуска функций;
- тестирования.

Пример логирования:

```python
from functools import wraps


def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Запущена функция: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Функция {function.__name__} завершена")

        return result

    return wrapper


@log_call
def multiply(first_number, second_number):
    return first_number * second_number


print(multiply(5, 4))
```

Результат:

```text
Запущена функция: multiply
Функция multiply завершена
20
```

---

## 26. Краткий итог

### Замыкание

Замыкание — это внутренняя функция, которая:

- использует переменные внешней функции;
- возвращается из внешней функции;
- сохраняет доступ к внешним переменным;
- может хранить состояние между вызовами.

### Декоратор

Декоратор — это функция, которая:

- принимает другую функцию;
- добавляет к ней новое поведение;
- возвращает функцию-обёртку;
- позволяет не изменять исходный код функции.

### Основная структура декоратора

```python
from functools import wraps


def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper
```

### Применение

```python
@decorator
def target_function():
    pass
```

Эквивалентная запись:

```python
target_function = decorator(target_function)
```