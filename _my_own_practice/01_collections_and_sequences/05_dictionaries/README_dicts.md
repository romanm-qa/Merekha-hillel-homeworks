# Словари в Python — dict

Словарь хранит пары **ключ: значение**. По ключу можно получить связанное с ним значение.

```python
student = {"name": "Roman", "age": 25, "city": "Kyiv"}
print(f"Исходный словарь: {student!r}")
print(f"student['name'] -> {student['name']!r}")  # 'Roman'
```

## Файлы темы

| Файл | Содержание |
| --- | --- |
| [01_dict_creation_and_basics.py](01_dict_creation_and_basics.py) | Создание, уникальность ключей, изменяемость, порядок и равенство |
| [02_dict_access_and_membership.py](02_dict_access_and_membership.py) | Доступ через `[]` и `get()`, проверка наличия |
| [03_dict_modification_methods.py](03_dict_modification_methods.py) | Добавление, обновление и удаление пар |
| [04_dict_iteration_and_views.py](04_dict_iteration_and_views.py) | Перебор, представления, преобразование в списки |
| [05_dict_copying_and_merging.py](05_dict_copying_and_merging.py) | Присваивание, копирование и объединение |
| [06_dict_comprehensions.py](06_dict_comprehensions.py) | Создание и преобразование словарей через comprehension |
| [07_dict_keys_and_nested_data.py](07_dict_keys_and_nested_data.py) | Хешируемые ключи и вложенные коллекции |

## 1. Основные свойства

- `dict` — изменяемый тип: можно добавлять и удалять пары, заменять значения.
- Ключи уникальны и должны быть хешируемыми.
- Значения могут быть любого типа и могут повторяться.
- Словарь сохраняет порядок добавления ключей.
- Доступ выполняется по ключу. Индексов и срезов у словаря нет.
- При обычном переборе словаря получаем ключи.
- Сам словарь не хешируется: он не может быть ключом другого словаря или элементом множества.

`len(student)` возвращает количество пар. Пустой словарь — `{}`; пустое множество создаётся через `set()`.

## 2. Создание словаря

```python
empty = {}
empty = dict()

student = {"name": "Roman", "age": 25}
student = dict(name="Roman", age=25)

pairs = [("name", "Roman"), ("age", 25)]
student = dict(pairs)

keys = ["name", "age"]
values = ["Roman", 25]
student = dict(zip(keys, values))
```

Имена аргументов в `dict(name="Roman")` становятся строковыми ключами. При создании из пар каждый элемент источника должен содержать ровно два элемента: ключ и значение.

Обычный `zip()` останавливается на самом коротком источнике. Если ключей три, а значений два, получится только две пары.

### Повторяющиеся ключи и значения

При повторе ключа остаётся последнее значение:

```python
pairs = [("name", "Roman"), ("age", 25), ("name", "Alex")]
print(dict(pairs))  # {'name': 'Alex', 'age': 25}
```

Одинаковые значения у разных ключей сохраняются:

```python
scores = {"Roman": 90, "Anna": 90, "Alex": 80}
print(len(scores))  # 3
```

### Порядок и равенство

Замена значения не перемещает ключ. Новый ключ добавляется в конец. Если удалить ключ и добавить его заново, он окажется в конце.

При сравнении через `==` порядок не учитывается: сравниваются пары ключ–значение.

```python
first = {"name": "Roman", "age": 25}
second = {"age": 25, "name": "Roman"}
print(first == second)  # True
```

## 3. Доступ и проверка наличия

| Запись | Ключ есть | Ключа нет | Меняет словарь |
| --- | --- | --- | --- |
| `data[key]` | Возвращает значение | `KeyError` | Нет |
| `data.get(key)` | Возвращает значение | Возвращает `None` | Нет |
| `data.get(key, default)` | Возвращает значение | Возвращает `default` | Нет |
| `key in data` | `True` | `False` | Нет |

Число в квадратных скобках тоже является ключом:

```python
items = {5: "apple", 0: "banana"}
print(items[0])  # 'banana' — значение ключа 0
```

### Что проверяет in

```python
student = {"name": "Roman", "age": 25}
print(f"Исходный словарь: {student!r}")
print(f"'name' in student -> {'name' in student!r}")  # True
print(f"'Roman' in student -> {'Roman' in student!r}")  # False
print(f"'Roman' in student.values() -> {'Roman' in student.values()!r}")  # True
print(f"('name', 'Roman') in student.items() -> {('name', 'Roman') in student.items()!r}")  # True
```

### Отсутствующий ключ и None

`get()` использует значение по умолчанию только при отсутствии ключа. Существующее значение `None` он не заменяет.

```python
student = {"name": "Roman", "city": None}
print(student.get("city", "Unknown"))     # None
print(student.get("country", "Unknown"))  # 'Unknown'
print("city" in student)                   # True
print("country" in student)                # False
```

Если нужно различить отсутствующий ключ и ключ со значением `None`, проверяй наличие через `in`.

## 4. Добавление, изменение и удаление

### Добавление и замена через []

```python
student = {"name": "Roman", "age": 25}
student["city"] = "Kyiv"  # Добавление новой пары
student["age"] = 26       # Замена значения
```

### Таблица методов и операций

| Метод или операция | Что делает | Что возвращает | Если ключа нет |
| --- | --- | --- | --- |
| `data[key] = value` | Добавляет пару или заменяет значение | Присваивание не возвращает результат | Добавляет пару |
| `data.update(other)` | Добавляет и обновляет пары | `None` | Добавляет пару |
| `data.setdefault(key, default)` | Добавляет пару только при отсутствии ключа | Существующее или добавленное значение | Добавляет `default` |
| `data.pop(key)` | Удаляет пару по ключу | Удалённое значение | `KeyError` |
| `data.pop(key, default)` | Удаляет пару, если ключ есть | Удалённое значение или `default` | Возвращает `default` |
| `data.popitem()` | Удаляет последнюю добавленную пару | Кортеж `(ключ, значение)` | Для пустого словаря — `KeyError` |
| `del data[key]` | Удаляет пару по ключу | Инструкция не возвращает результат | `KeyError` |
| `data.clear()` | Удаляет все пары | `None` | Оставляет пустой словарь |

`del` — инструкция Python, а не метод словаря.

### update()

Принимает другой словарь, итерируемый объект с парами или именованные аргументы. При совпадении ключей использует новые значения.

```python
student = {"name": "Roman", "age": 25}
student.update({"age": 26, "city": "Kyiv"})
student.update([("age", 27)])
student.update(city="Lviv")
```

Не записывай `student = student.update(...)`: метод возвращает `None`.

### get() и setdefault()

Оба возвращают значение существующего ключа. Если ключа нет, `get()` только возвращает default, а `setdefault()` ещё добавляет пару.

```python
student = {"name": "Roman"}
print(student.get("city", "Kyiv"))         # 'Kyiv'
print(student)                            # {'name': 'Roman'}
print(student.setdefault("city", "Kyiv"))  # 'Kyiv'
print(student)                            # {'name': 'Roman', 'city': 'Kyiv'}
```

Без второго аргумента `setdefault()` использует `None`. Если ключ уже есть, его значение сохраняется, включая `None`.

## 5. Перебор и представления

| Запись | Что получаем при переборе |
| --- | --- |
| `for key in data` | Ключи |
| `for key in data.keys()` | Ключи |
| `for value in data.values()` | Значения |
| `for key, value in data.items()` | Ключ и значение каждой пары |

```python
student = {"name": "Roman", "age": 25}
print(f"Исходный словарь: {student!r}")
for key, value in student.items():
    print(f"Ключ: {key!r}, значение: {value!r}")
```

`items()` при переборе выдаёт кортежи `(ключ, значение)`. В цикле выше каждая пара распаковывается в две переменные.

### keys(), values() и items()

Эти методы возвращают **представления** словаря: `dict_keys`, `dict_values`, `dict_items`.

Представление связано с исходным словарём и отражает его изменения. Доступ по индексу не поддерживается. Для индексов можно создать список.

```python
student = {"name": "Roman", "age": 25}
keys_view = student.keys()
keys_list = list(student)
student["city"] = "Kyiv"

print(keys_view)     # dict_keys(['name', 'age', 'city'])
print(keys_list)     # ['name', 'age']
print(keys_list[0])  # 'name'
```

### Преобразование в списки

Для `student = {"name": "Roman", "age": 25}`:

| Выражение | Результат |
| --- | --- |
| `list(student)` | `['name', 'age']` |
| `list(student.keys())` | `['name', 'age']` |
| `list(student.values())` | `['Roman', 25]` |
| `list(student.items())` | `[('name', 'Roman'), ('age', 25)]` |

### Изменение при переборе

Заменять значения существующих ключей можно:

```python
scores = {"Roman": 80, "Anna": 90, "Alex": 70}
for name in scores:
    scores[name] += 5
```

Не добавляй и не удаляй ключи при прямом переборе словаря или его представлений: это может вызвать `RuntimeError` или нарушить перебор. Для удаления используй отдельный список ключей:

```python
scores = {"Roman": 80, "Anna": 90, "Alex": 70}
for name in list(scores):
    if scores[name] < 80:
        del scores[name]
```

## 6. Присваивание и копирование

| Запись | Новый внешний словарь | Вложенные изменяемые коллекции |
| --- | --- | --- |
| `alias = data` | Нет | Общие, поскольку словарь один |
| `copied = data.copy()` | Да | Остаются общими |
| `copied = dict(data)` | Да | Остаются общими |
| `copied = deepcopy(data)` | Да | Вложенные обычные коллекции копируются рекурсивно |

`==` сравнивает содержимое, `is` проверяет, один ли это объект.

### Поверхностная копия

```python
student = {"name": "Roman", "courses": ["Python", "SQL"]}
copied = student.copy()

print(copied == student)  # True
print(copied is student)  # False
print(copied["courses"] is student["courses"])  # True

copied["courses"].append("Git")  # Общий список изменится у обоих
copied["name"] = "Alex"         # Значение заменится только в copied
```

Замена вложенного списка через `copied['courses'] = ['Docker']` затронет только копию. Это присваивание нового значения ключу, а не изменение общего списка.

### Глубокая копия

```python
from copy import deepcopy

student = {"name": "Roman", "courses": ["Python", "SQL"]}
copied = deepcopy(student)
copied["courses"].append("Git")

print(student["courses"])  # ['Python', 'SQL']
print(copied["courses"])   # ['Python', 'SQL', 'Git']
```

## 7. Объединение словарей

| Запись | Создаёт новый словарь | Меняет левый словарь |
| --- | --- | --- |
| `left \| right` | Да | Нет |
| `{**left, **right}` | Да | Нет |
| `left \|= right` | Нет | Да |
| `left.update(right)` | Нет | Да |

При совпадении ключей побеждает значение справа или указанное позже. Объединение не выполняет глубокое копирование вложенных объектов.

```python
left = {"name": "Roman", "age": 25}
right = {"age": 26, "city": "Kyiv"}
merged = left | right
print(merged)  # {'name': 'Roman', 'age': 26, 'city': 'Kyiv'}
```

`left | right` и `right | left` могут содержать разные значения совпадающих ключей. Обновлённый ключ сохраняет свою позицию; новые ключи добавляются в конец.

## 8. Dict comprehension

Общая запись:

```python
result = {key_expression: value_expression for item in source}
```

Создаёт новый словарь. Ключ и значение можно вычислять из элемента источника.

```python
numbers = [1, 2, 3, 4]
squares = {number: number ** 2 for number in numbers}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16}
```

Эквивалентный цикл:

```python
numbers = [1, 2, 3, 4]
squares = {}
for number in numbers:
    squares[number] = number ** 2
```

### Фильтрация и выбор значения

`if` после `for` отбирает элементы. `if/else` перед `for` выбирает значение для каждого элемента.

```python
scores = {"Roman": 80, "Anna": 90, "Alex": 70}

passed = {name: score for name, score in scores.items() if score >= 80}
# {'Roman': 80, 'Anna': 90}

statuses = {
    name: "Passed" if score >= 80 else "Failed"
    for name, score in scores.items()
}
# {'Roman': 'Passed', 'Anna': 'Passed', 'Alex': 'Failed'}
```

### Преобразование ключей и значений

```python
scores = {"Roman": 80, "Anna": 90}
increased = {name: score + 5 for name, score in scores.items()}
lowercase = {name.lower(): score for name, score in scores.items()}

names = ["Roman", "Anna"]
points = [80, 90]
student_scores = {name: score for name, score in zip(names, points)}
```

### Обмен ключей и значений

Новые ключи должны быть хешируемыми. Повторяющиеся новые ключи приводят к потере пар: сохраняется последнее значение.

```python
scores = {"Roman": 90, "Anna": 90, "Alex": 80}
students_by_score = {score: name for name, score in scores.items()}
print(students_by_score)  # {90: 'Anna', 80: 'Alex'}
```

## 9. Какие объекты могут быть ключами

Хешируемость позволяет использовать объект как ключ словаря или элемент множества. Она не означает, что объект можно перебрать.

| Тип ключа | Можно использовать | Условие или пример |
| --- | --- | --- |
| `str` | Да | `'name'` |
| `int`, `float`, `bool` | Да | `100`, `2.5`, `True` |
| `tuple` | Если все элементы хешируемые | `(1, 2)` можно; `(1, [2, 3])` нельзя |
| `frozenset` | Да | `frozenset({1, 2})` |
| `list` | Нет | `TypeError` |
| `set` | Нет | `TypeError` |
| `dict` | Нет | `TypeError` |

### Равные числовые ключи

`1`, `1.0` и `True` равны и имеют одинаковый хеш, поэтому относятся к одной записи:

```python
data = {1: "integer"}
data[1.0] = "float"
data[True] = "boolean"
print(data)       # {1: 'boolean'}
print(len(data))  # 1
```

## 10. Вложенные данные

Значением может быть список, другой словарь или любая другая коллекция.

```python
student = {
    "name": "Roman",
    "courses": ["Python", "SQL"],
    "address": {"city": "Kyiv", "country": "Ukraine"},
}

print(student["courses"][0])       # 'Python'
print(student["address"]["city"])  # 'Kyiv'
student["courses"].append("Git")
student["address"]["city"] = "Lviv"
```

В `student['courses'][0]` сначала получаем список по ключу, затем элемент списка по индексу. В `student['address']['city']` оба обращения выполняются по ключам.

### get() для вложенных данных

`get()` проверяет только словарь, на котором вызван.

```python
student = {"name": "Roman"}
address = student.get("address", {})
city = address.get("city", "Unknown")
```

Если `address` существует со значением `None`, default `{}` не используется. Когда тип вложенного значения неизвестен, его можно проверить:

```python
student = {"name": "Roman", "address": None}
address = student.get("address")
if isinstance(address, dict):
    city = address.get("city", "Unknown")
else:
    city = "Unknown"
```

### Список словарей

```python
students = [
    {"name": "Roman", "score": 80},
    {"name": "Anna", "score": 90},
]
print(f"Исходный список: {students!r}")
for student in students:
    print(f"Имя: {student['name']!r}, баллы: {student['score']!r}")
```

## 11. Что важно запомнить

- `{}` создаёт словарь, `set()` — пустое множество.
- `data[key]` ищет по ключу; отсутствующий ключ вызывает `KeyError`.
- `get()` не добавляет ключ; `setdefault()` добавляет отсутствующий ключ.
- `in` для словаря проверяет ключи.
- `keys()`, `values()`, `items()` возвращают динамические представления.
- `pop()` возвращает значение; `popitem()` — пару `(ключ, значение)`.
- `update()` и `clear()` меняют словарь и возвращают `None`.
- Присваивание не копирует словарь; поверхностная копия сохраняет общие вложенные объекты.
- При объединении совпадающий ключ получает значение справа.
- Ключ должен быть хешируемым; значение может быть любого типа.
