# Strings (`str`)

## Что такое строка

**Строка (`str`)** — это неизменяемая упорядоченная последовательность символов Unicode.

```python
empty = ""
letter = "A"
text = "Hello"

print(type(text))  # <class 'str'>
print(len(empty))  # 0
```

Строка может быть пустой. В Python нет отдельного типа `char`: один символ — это строка длиной `1`.

Строки:

- упорядочены;
- поддерживают индексацию, срезы и перебор;
- могут содержать повторяющиеся символы;
- являются неизменяемыми (`immutable`).

---

## Создание строк

Одинарные и двойные кавычки равнозначны:

```python
first = 'Hello'
second = "Python"
message = "I'm learning Python"
quote = 'He said: "Hello"'
```

Тройные кавычки используют для многострочного текста:

```python
message = """Первая строка
Вторая строка"""
```

Функция `str()` создаёт строковое представление объекта:

```python
age_as_text = str(30)
print(age_as_text)        # 30 (без кавычек при выводе, но это строка)
print(type(age_as_text))  # <class 'str'>
```

`input()` всегда возвращает строку:

```python
age = input("Введите возраст: ")
print(type(age))  # <class 'str'>
```

---

## Escape-последовательности и raw strings

| Запись | Значение |
| --- | --- |
| `\n` | перенос строки |
| `\t` | табуляция |
| `\\` | обратная косая черта |
| `\"` | двойная кавычка |
| `\'` | одинарная кавычка |

```python
print("Hello\nWorld")
print("Name:\tRoman")
print("C:\\Users\\Roman")
```

В raw string обратные косые черты обычно воспринимаются буквально:

```python
path = r"C:\Users\Roman\tests"
regex = r"\d+"
```

Такие строки часто используют для регулярных выражений и Windows-путей.

---

## Длина и индексация

`len()` возвращает количество символов. Положительные индексы считаются слева от `0`, отрицательные — справа от `-1`.

```text
символ:    P   y   t   h   o   n
индекс:    0   1   2   3   4   5
отриц.:   -6  -5  -4  -3  -2  -1
```

```python
text = "Python"

print(len(text))  # 6
print(text[0])    # P
print(text[-1])   # n
```

Несуществующий индекс вызывает `IndexError`:

```python
print(text[10])  # IndexError: string index out of range
```

---

## Срезы

```python
string[start:stop:step]
```

- `start` включается;
- `stop` не включается;
- стандартный `step` равен `1`.

```python
text = "Python"

print(text[1:4])   # yth
print(text[:3])    # Pyt
print(text[3:])    # hon
print(text[::2])   # Pto
print(text[::-1])  # nohtyP
print(text[:])     # Python
```

`text[:]` возвращает всю строку; отдельный объект при этом не гарантирован.

В отличие от индекса, граница среза может выходить за длину строки:

```python
print("Python"[:100])  # Python
```

Шаг `0` вызывает `ValueError`.

---

## Неизменяемость строк

Изменить символ по индексу нельзя:

```python
text = "Hello"
text[0] = "Y"  # TypeError
```

Строковые методы не изменяют исходную строку, а возвращают результат:

```python
text = "Hello"
new_text = text.replace("H", "Y")

print(text)      # Hello
print(new_text)  # Yello
```

Чтобы сохранить результат, его нужно присвоить переменной:

```python
text = text.upper()
```

---

## Перебор строки

```python
for letter in "QA":
    print(letter)

for index, letter in enumerate("QA"):
    print(index, letter)
```

`enumerate()` используют, когда вместе с символом нужен его индекс.

---

## Проверка наличия и поиск

`in` и `not in` возвращают `bool`:

```python
url = "https://example.com/login"

print("login" in url)      # True
print("admin" not in url)  # True
```

Проверка чувствительна к регистру.

### `find()`, `rfind()`, `index()`

`find()` возвращает индекс первого вхождения, `rfind()` — последнего. Если подстроки нет, они возвращают `-1`.

`index()` работает похоже на `find()`, но при отсутствии подстроки вызывает `ValueError`.

```python
text = "test passed, test finished"

print(text.find("test"))   # 0
print(text.rfind("test"))  # 13
print(text.find("error"))  # -1
print("Python".index("t"))  # 2
```

### `count()`, `startswith()`, `endswith()`

```python
print("banana".count("a"))  # 3

filename = "report.pdf"
print(filename.startswith("report"))       # True
print(filename.endswith(".pdf"))           # True
print(filename.endswith((".pdf", ".txt"))) # True
```

`count()` считает неперекрывающиеся вхождения.

---

## Изменение регистра

```python
text = "pYtHoN testing"

print(text.lower())       # python testing
print(text.upper())       # PYTHON TESTING
print(text.capitalize())  # Python testing
print(text.title())       # Python Testing
print(text.swapcase())    # PyThOn TESTING
```

Для сравнения Unicode-текста без учёта регистра подходит `casefold()`:

```python
actual = "Straße"
expected = "STRASSE"

print(actual.casefold() == expected.casefold())  # True
```

`casefold()` выполняет более агрессивное преобразование регистра, чем `lower()`.

---

## Замена и очистка

### `replace()`

```python
text = "one one one"

print(text.replace("one", "two"))     # two two two
print(text.replace("one", "two", 1))  # two one one
```

Третий аргумент ограничивает количество замен.

### `strip()`, `lstrip()`, `rstrip()`

Без аргументов удаляют пробельные символы по краям, включая пробелы, `\n` и `\t`:

```python
text = " \t Hello \n"

print(text.strip())
print(text.lstrip())
print(text.rstrip())
```

Аргумент `strip()` — это набор удаляемых символов, а не точная подстрока:

```python
print("www.example.com".strip("w.com"))  # example
```

Для удаления точного префикса или суффикса используют:

```python
print("test_user".removeprefix("test_"))   # user
print("report.json".removesuffix(".json")) # report
```

---

## Разделение и объединение

### `split()`

Разбивает строку и возвращает список строк:

```python
text = "Python,Java,Go"

print(text.split(","))     # ['Python', 'Java', 'Go']
print(text.split(",", 1))  # ['Python', 'Java,Go']
```

Без аргумента `split()` делит по группам пробельных символов:

```python
print(" Python   QA\nAutomation ".split())
# ['Python', 'QA', 'Automation']
print("a  b".split(" "))  # ['a', '', 'b'] — точный разделитель сохраняет пустой элемент
```

### `join()`

Объединяет строки из итерируемого объекта. Метод вызывается у разделителя:

```python
languages = ["Python", "Java", "Go"]
print(", ".join(languages))  # Python, Java, Go
```

Все элементы должны быть строками:

```python
numbers = [1, 2, 3]
result = "-".join(map(str, numbers))
print(result)  # 1-2-3
```

---

## Методы проверки

| Метод | Что проверяет |
| --- | --- |
| `isalpha()` | только буквы |
| `isdigit()` | только цифры |
| `isalnum()` | только буквы и цифры |
| `isspace()` | только пробельные символы |
| `islower()` | регистровые символы в нижнем регистре |
| `isupper()` | регистровые символы в верхнем регистре |

```python
print("Python".isalpha())    # True
print("123".isdigit())      # True
print("Python3".isalnum())  # True
print(" \t\n".isspace())    # True
```

Для пустой строки эти четыре метода возвращают `False`.

Проверки относятся ко **всей** строке: `"Python QA".isalnum()` даёт `False` из-за пробела, а `"Hello World".isspace()` — из-за букв.

`isdigit()` не проверяет запись числа со знаком или десятичной точкой:

```python
print("-123".isdigit())  # False
print("12.5".isdigit())  # False
print("²".isdigit())     # True
```

Даже `True` не гарантирует, что `int()` примет строку: `int("²")` вызовет `ValueError`.

---

## Форматирование строк

### Конкатенация

Оператор `+` объединяет строки:

```python
name = "Roman"
message = "Hello, " + name
```

Для объединения большого количества строк обычно используют `join()`.

### `str.format()`

```python
message = "Name: {}, score: {:.2f}".format("Roman", 95.5)
print(message)  # Name: Roman, score: 95.50
```

### F-строки

В современном Python чаще используют f-строки:

```python
name = "Roman"
score = 95.5

print(f"Name: {name}, score: {score:.2f}")
print(f"Rounded: {42:05d}")  # Rounded: 00042
print(f"Percent: {0.875:.1%}")  # Percent: 87.5%
```

В фигурных скобках допустимы выражения:

```python
passed = 8
failed = 2

print(f"Total: {passed + failed}")  # Total: 10
```

`!r` внутри f-строки показывает представление значения (`repr()`), что помогает увидеть кавычки и скрытые символы:

```python
text = " hello\n"
print(f"{text!r}")  # ' hello\n'
```

---

## Сравнение строк

`==` сравнивает значения, а `is` — идентичность объектов. Содержимое строк сравнивают через `==`:

```python
actual = "passed"
expected = "passed"

print(actual == expected)  # True
```

`<` и `>` сравнивают строки лексикографически по кодовым точкам Unicode и чувствительны к регистру:

```python
print("apple" < "banana")  # True
print("Z" < "a")           # True
```

---

## Примеры для автотестов

Ниже фрагменты отдельных тестов: `current_url`, `actual_text`, `actual_status` и `filename` предполагаются уже полученными в тесте.

```python
assert current_url.endswith("/garage")
assert actual_text.strip() == "Car added"
assert actual_status.casefold() == "success".casefold()

status_code, message = "200 OK".split(maxsplit=1)

assert filename.endswith((".png", ".jpg", ".jpeg"))
```

---

## Краткие выводы

- `str` — упорядоченная неизменяемая последовательность Unicode-символов.
- Индекс возвращает символ и может вызвать `IndexError`; срез возвращает строку и допускает выход границы за длину.
- Строковые методы не изменяют исходную строку.
- `in` проверяет наличие, `find()` возвращает индекс или `-1`, а `index()` может вызвать `ValueError`.
- `split()` превращает строку в список, а `join()` объединяет строки.
- `strip()` очищает края строки, но не символы внутри.
- Для современного форматирования обычно используют f-строки.
- Значения строк сравнивают через `==`, а не через `is`.
