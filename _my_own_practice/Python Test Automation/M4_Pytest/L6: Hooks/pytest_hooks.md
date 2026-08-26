# L6: Hooks в Pytest

## Цели урока

После этого урока вы сможете:

- объяснить концепцию хуков (hooks) в Pytest;
- добавлять дополнительные параметры командной строки Pytest;
- изменять результаты сбора тестов и добавлять собственную логику отчётности;
- создавать динамические тесты, расширяя параметризацию;
- настраивать отчётность и уведомления о результатах запуска тестов;
- находить и изучать другие хуки в официальной документации Pytest.

---

# Что такое Pytest Hooks

**Hook (хук)** — это специальная функция, с помощью которой можно расширить или изменить стандартное поведение Pytest.

Хуки обычно описываются в файле `conftest.py`, а их названия начинаются с `pytest_`.

Примеры:

```python
def pytest_addoption(parser):
    ...
```

```python
def pytest_collection_finish(session):
    ...
```

```python
def pytest_generate_tests(metafunc):
    ...
```

```python
def pytest_sessionfinish(session, exitstatus):
    ...
```

Pytest автоматически находит такие функции и вызывает их в соответствующий момент жизненного цикла тестового запуска.

С помощью хуков можно:

- добавлять собственные параметры командной строки;
- влиять на сбор тестов;
- динамически параметризовать тесты;
- изменять или дополнять отчёты;
- выполнять действия после завершения всех тестов;
- отправлять уведомления;
- создавать плагины для Pytest.

По умолчанию Pytest предоставляет большое количество обычных хуков для изменения его поведения, а также специальные хуки для отладки.

---

## Жизненный цикл запуска Pytest

Упрощённо запуск Pytest можно представить так:

1. Pytest читает конфигурацию и аргументы командной строки.
2. Pytest находит файлы и функции с тестами.
3. Выполняется сбор тестов (test collection).
4. Собранные тесты запускаются.
5. Формируются результаты и отчёт.
6. Тестовая сессия завершается.

Разные хуки вызываются на разных этапах этого процесса.

Например:

| Хук | Когда вызывается |
|---|---|
| `pytest_addoption` | При настройке аргументов командной строки |
| `pytest_collection_finish` | После завершения сбора тестов |
| `pytest_generate_tests` | Во время сбора и подготовки тестовой функции |
| `pytest_sessionfinish` | После завершения всей тестовой сессии |

---

# Декоратор `@pytest.hookimpl`

Pytest предоставляет специальный декоратор:

```python
@pytest.hookimpl
```

Он позволяет управлять поведением и порядком выполнения хуков.

Например, можно указать, что конкретная реализация хука должна запускаться:

- раньше других реализаций;
- позже других реализаций;
- как обёртка вокруг остальных реализаций.

Пример:

```python
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_collection_finish(session):
    print("This hook should run before other implementations")
```

Часто используемые параметры:

| Параметр | Назначение |
|---|---|
| `tryfirst=True` | Попытаться выполнить реализацию хука первой |
| `trylast=True` | Попытаться выполнить реализацию хука последней |
| `hookwrapper=True` | Выполнить хук как обёртку вокруг других реализаций |

---

# Хук `pytest_addoption`

```python
pytest_addoption(parser, pluginmanager)
```

Хук `pytest_addoption` используется для добавления собственных параметров в командную строку Pytest.

Благодаря ему тесты можно запускать с дополнительными аргументами:

```bash
pytest --cmdopt=type2
```

## Пример структуры

```text
project/
├── conftest.py
└── test_sample.py
```

## Файл `test_sample.py`

```python
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")

    assert 0  # Намеренное падение, чтобы увидеть результат print()
```

Тест принимает фикстуру `cmdopt`.

В зависимости от её значения он выводит:

- `first`, если передано `type1`;
- `second`, если передано `type2`.

Проверка:

```python
assert 0
```

намеренно всегда падает. Она добавлена только для того, чтобы Pytest показал перехваченный вывод `print()` в отчёте об ошибке.

---

## Файл `conftest.py`

```python
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",
        action="store",
        default="type1",
        help="my option: type1 or type2",
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
```

Разберём этот код подробнее.

### Добавление нового параметра

```python
def pytest_addoption(parser):
```

Pytest автоматически вызывает этот хук и передаёт в него объект `parser`.

Объект `parser` позволяет зарегистрировать новые параметры командной строки.

```python
parser.addoption(
    "--cmdopt",
    action="store",
    default="type1",
    help="my option: type1 or type2",
)
```

Здесь создаётся дополнительный параметр:

```bash
--cmdopt
```

Его настройки:

| Аргумент | Значение |
|---|---|
| `"--cmdopt"` | Название параметра командной строки |
| `action="store"` | Сохранить переданное пользователем значение |
| `default="type1"` | Использовать `type1`, если параметр не был передан |
| `help="..."` | Описание параметра в справке Pytest |

---

## Получение значения параметра

```python
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
```

Встроенная фикстура `request` предоставляет информацию о текущем тестовом запуске.

Через неё можно получить конфигурацию Pytest:

```python
request.config
```

А затем прочитать значение аргумента командной строки:

```python
request.config.getoption("--cmdopt")
```

Полученное значение возвращается из фикстуры и передаётся в тест:

```python
def test_answer(cmdopt):
```

---

## Запуск без дополнительного параметра

```bash
pytest -q test_sample.py
```

Поскольку пользователь не передал `--cmdopt`, используется значение по умолчанию:

```python
default="type1"
```

Следовательно, тест выполняет:

```python
print("first")
```

В отчёте будет показано:

```text
Captured stdout call
first
```

---

## Запуск с дополнительным параметром

```bash
pytest -q --cmdopt=type2 test_sample.py
```

Теперь параметр имеет значение:

```python
cmdopt == "type2"
```

Поэтому тест выполняет:

```python
print("second")
```

В отчёте будет показано:

```text
Captured stdout call
second
```

Таким образом, один и тот же тест может менять своё поведение в зависимости от аргументов командной строки.

---

# Хук `pytest_collection_finish`

```python
pytest_collection_finish(session)
```

Хук `pytest_collection_finish` вызывается после того, как Pytest завершил сбор тестов.

Он позволяет:

- анализировать собранные тесты;
- изменять результаты этапа сбора;
- добавлять собственную логику отчётности;
- искать тесты с определёнными маркерами;
- выводить информацию о количестве и составе тестов.

Объект `session` содержит поле:

```python
session.items
```

В нём находится плоский список всех собранных тестов.

## Пример

```python
def pytest_collection_finish(session):
    print(f"Collected tests: {len(session.items)}")

    for item in session.items:
        print(item.nodeid)
```

Возможный вывод:

```text
Collected tests: 3
tests/test_login.py::test_valid_login
tests/test_login.py::test_invalid_password
tests/test_profile.py::test_update_profile
```

У каждого элемента можно проверить наличие маркера с помощью:

```python
item.get_closest_marker("marker_name")
```

Например:

```python
def pytest_collection_finish(session):
    smoke_tests = []

    for item in session.items:
        if item.get_closest_marker("smoke"):
            smoke_tests.append(item)

    print(f"Smoke tests collected: {len(smoke_tests)}")
```

Этот хук не запускает тесты. Он работает с тестами, которые Pytest уже обнаружил и добавил в коллекцию.

---

# Хук `pytest_generate_tests`

```python
pytest_generate_tests(metafunc)
```

Хук `pytest_generate_tests` позволяет динамически создавать несколько тест-кейсов для одной тестовой функции.

Он вызывается во время сбора тестов.

Через объект `metafunc` можно:

- узнать имя тестовой функции;
- посмотреть, какие фикстуры она запрашивает;
- получить конфигурацию Pytest;
- динамически вызвать параметризацию.

Главный метод:

```python
metafunc.parametrize()
```

По назначению он похож на декоратор:

```python
@pytest.mark.parametrize(...)
```

Разница заключается в том, что `pytest_generate_tests` позволяет формировать набор тестовых данных динамически.

---

## Пример структуры

```text
project/
├── conftest.py
└── test_strings.py
```

## Файл `test_strings.py`

```python
def test_valid_string(stringinput):
    assert stringinput.isalpha()
```

Метод:

```python
stringinput.isalpha()
```

возвращает `True`, если строка:

- не пустая;
- содержит только буквенные символы.

---

## Файл `conftest.py`

```python
def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize(
            "stringinput",
            metafunc.config.getoption("stringinput"),
        )
```

---

## Параметр с `action="append"`

```python
action="append"
```

означает, что аргумент можно передать несколько раз.

Например:

```bash
pytest \
  --stringinput="hello" \
  --stringinput="world" \
  test_strings.py
```

Все значения будут собраны в список:

```python
["hello", "world"]
```

Для сравнения:

| Значение `action` | Поведение |
|---|---|
| `"store"` | Сохраняет одно переданное значение |
| `"append"` | Добавляет каждое переданное значение в список |

---

## Проверка имени фикстуры

```python
if "stringinput" in metafunc.fixturenames:
```

`metafunc.fixturenames` содержит имена фикстур и аргументов, которые запрашивает текущая тестовая функция.

Наш тест принимает:

```python
def test_valid_string(stringinput):
```

Поэтому условие выполняется.

---

## Динамическая параметризация

```python
metafunc.parametrize(
    "stringinput",
    metafunc.config.getoption("stringinput"),
)
```

Здесь:

1. Pytest получает значения параметра `--stringinput`.
2. Каждое значение превращается в отдельный тест-кейс.
3. Значения по очереди передаются в аргумент `stringinput`.

Команда:

```bash
pytest -q \
  --stringinput="hello" \
  --stringinput="world" \
  test_strings.py
```

Результат:

```text
..                                                     [100%]
2 passed in 0.01s
```

Хотя в файле находится только одна тестовая функция, Pytest запустил два тест-кейса:

```python
test_valid_string("hello")
test_valid_string("world")
```

---

# Хук `pytest_sessionfinish`

```python
pytest_sessionfinish(session, exitstatus)
```

Хук `pytest_sessionfinish` вызывается после завершения всей тестовой сессии, непосредственно перед тем, как Pytest вернёт системе итоговый код завершения.

Он может использоваться для:

- генерации дополнительных отчётов;
- обновления статусов тестового запуска;
- отправки уведомлений;
- очистки ресурсов;
- сохранения итоговой статистики;
- выполнения действий в зависимости от успешности тестов.

Аргументы:

| Аргумент | Назначение |
|---|---|
| `session` | Информация о текущей тестовой сессии |
| `exitstatus` | Итоговый статус завершения Pytest |

## Простой пример

```python
def pytest_sessionfinish(session, exitstatus):
    print(f"Tests collected: {session.testscollected}")
    print(f"Exit status: {exitstatus}")
```

В `session` хранится информация о тестовой сессии, например количество собранных тестов.

`exitstatus` показывает, с каким результатом завершился запуск.

Некоторые стандартные коды завершения Pytest:

| Код | Значение |
|---:|---|
| `0` | Все тесты прошли |
| `1` | Один или несколько тестов упали |
| `2` | Выполнение было прервано пользователем |
| `3` | Внутренняя ошибка Pytest |
| `4` | Ошибка использования командной строки |
| `5` | Тесты не были найдены |

## Пример уведомления

```python
def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        print("All tests passed")
    else:
        print("Test run failed")
```

В реальном проекте вместо `print()` здесь можно:

- отправить сообщение в Slack;
- отправить email;
- обновить результат запуска в TestRail;
- записать данные в систему отчётности;
- сохранить статистику в файл или базу данных.

---

# Краткое сравнение рассмотренных хуков

| Хук | Назначение |
|---|---|
| `pytest_addoption` | Добавляет собственные аргументы командной строки |
| `pytest_collection_finish` | Работает с уже собранной коллекцией тестов |
| `pytest_generate_tests` | Динамически создаёт параметризованные тест-кейсы |
| `pytest_sessionfinish` | Выполняет действия после завершения всей тестовой сессии |

---

# Главное о Pytest Hooks

- Хук — это точка расширения стандартного поведения Pytest.
- Названия хуков начинаются с `pytest_`.
- Хуки обычно размещаются в `conftest.py` или в плагинах Pytest.
- Pytest самостоятельно вызывает хуки в соответствующие моменты.
- `pytest_addoption` добавляет параметры командной строки.
- Значения параметров можно получать через `request.config.getoption()`.
- `pytest_collection_finish` позволяет анализировать собранные тесты.
- `pytest_generate_tests` создаёт динамическую параметризацию.
- `pytest_sessionfinish` выполняется после завершения всех тестов.
- `@pytest.hookimpl` позволяет управлять порядком и способом выполнения реализаций хуков.

---

# Официальная документация

- [Writing hook functions](https://docs.pytest.org/en/7.1.x/how-to/writing_hook_functions.html)
- [Reference to all hooks](https://docs.pytest.org/en/7.1.x/reference/reference.html#hooks)