# L7: Fixtures в Pytest

## Цели урока

После этого урока вы сможете:

- объяснить назначение фикстур (fixtures) в Pytest;
- создавать собственные фикстуры;
- объяснить работу фикстур с `yield`;
- использовать параметр `scope`;
- выбирать подходящую область действия фикстуры;
- использовать общие фикстуры в нескольких тестовых файлах;
- автоматически запускать фикстуры с помощью `autouse`.

---

# Что такое фикстуры

**Fixture (фикстура)** — это специальная функция, которую Pytest выполняет для подготовки окружения или тестовых данных.

Обычно фикстура выполняется до запуска теста, а её результат передаётся внутрь тестовой функции.

Фикстуры можно использовать для:

- создания тестовых данных;
- подключения к базе данных;
- создания API-клиента;
- авторизации пользователя;
- открытия браузера;
- подготовки файлов;
- переключения системы в необходимое состояние;
- очистки созданных данных после теста.

Фикстуры можно повторно использовать в разных тестах. Благодаря этому не приходится дублировать одинаковый подготовительный код.

---

## Проблема без использования фикстур

Представим, что нескольким тестам необходимо подключение к базе данных.

Без фикстуры подключение пришлось бы создавать отдельно в каждом тесте:

```python
def test_create_user():
    connection = create_database_connection()
    ...


def test_delete_user():
    connection = create_database_connection()
    ...


def test_update_user():
    connection = create_database_connection()
    ...
```

Это приводит к:

- дублированию кода;
- усложнению поддержки;
- возможным различиям в подготовке тестов;
- лишним затратам времени и ресурсов.

Вместо этого можно создать одну фикстуру и использовать её во всех необходимых тестах.

---

# Создание простой фикстуры

Для объявления фикстуры используется декоратор:

```python
@pytest.fixture
```

или:

```python
@pytest.fixture()
```

Оба варианта допустимы.

Пример:

```python
import pytest


@pytest.fixture()
def ultimate_question_answer():
    return 42


def test_some_data(ultimate_question_answer):
    """Use fixture return value in a test."""
    assert ultimate_question_answer == 42
```

---

## Как Pytest находит фикстуру

Фикстура называется:

```python
ultimate_question_answer
```

Тест принимает аргумент с таким же именем:

```python
def test_some_data(ultimate_question_answer):
```

Pytest видит это имя и понимает, что перед запуском теста необходимо:

1. найти фикстуру `ultimate_question_answer`;
2. выполнить её;
3. получить значение из `return`;
4. передать это значение в тест.

Фактически происходит следующее:

```python
ultimate_question_answer = 42
```

После этого запускается проверка:

```python
assert ultimate_question_answer == 42
```

Самостоятельно вызывать фикстуру не нужно:

```python
# Так делать не нужно
ultimate_question_answer()
```

Pytest управляет вызовом фикстуры автоматически.

---

# Фикстура как предусловие

Фикстура может не возвращать значение, а просто выполнять необходимые действия перед тестом.

Например:

```python
import pytest


@pytest.fixture()
def prepare_test_environment():
    print("Prepare test environment")


def test_feature(prepare_test_environment):
    assert True
```

Перед запуском `test_feature` Pytest сначала выполнит:

```python
prepare_test_environment
```

Таким образом, фикстура может выступать в роли предусловия (**precondition**).

---

# Фикстуры с `yield`

Иногда необходимо выполнить действия не только до теста, но и после него.

Например:

- открыть и закрыть соединение с базой данных;
- создать и удалить пользователя;
- открыть и закрыть браузер;
- создать и удалить файл;
- авторизоваться и завершить сессию;
- добавить и удалить тестовые данные.

Для этого используются фикстуры с `yield`.

Пример:

```python
import pytest


@pytest.fixture()
def ultimate_question_answer():
    print("Set Up")

    yield 42

    print("Teardown")


def test_some_data(ultimate_question_answer):
    """Use fixture return value in a test."""
    assert ultimate_question_answer == 42
```

---

## Как работает `yield` в фикстуре

Код фикстуры делится на две части:

```python
@pytest.fixture()
def ultimate_question_answer():
    print("Set Up")      # Setup

    yield 42             # Передача значения тесту

    print("Teardown")    # Teardown
```

### Код до `yield`

```python
print("Set Up")
```

Это подготовительная часть — **setup**.

Она выполняется до запуска теста.

Здесь обычно:

- создают данные;
- открывают соединение;
- запускают браузер;
- выполняют авторизацию;
- подготавливают окружение.

### Значение после `yield`

```python
yield 42
```

Значение `42` передаётся в тест:

```python
def test_some_data(ultimate_question_answer):
```

Внутри теста:

```python
ultimate_question_answer == 42
```

### Код после `yield`

```python
print("Teardown")
```

Это завершающая часть — **teardown**.

Она выполняется после завершения теста.

Здесь обычно:

- удаляют тестовые данные;
- закрывают соединение;
- закрывают браузер;
- удаляют временные файлы;
- освобождают ресурсы.

---

## Порядок выполнения

Для следующего кода:

```python
@pytest.fixture()
def example_fixture():
    print("Set Up")
    yield 42
    print("Teardown")


def test_example(example_fixture):
    print("Test")
    assert example_fixture == 42
```

порядок выполнения будет таким:

```text
Set Up
Test
Teardown
```

Запуск с отображением `print()`:

```bash
pytest -v -s
```

Флаг `-s` отключает перехват стандартного вывода, поэтому сообщения `print()` отображаются в терминале.

Пример результата:

```text
example_test.py::test_example Set Up
Test
PASSED
Teardown
```

---

# `return` и `yield` в фикстурах

## Фикстура с `return`

```python
@pytest.fixture()
def user():
    return {"name": "Roman"}
```

Такая фикстура:

- подготавливает значение;
- передаёт его тесту;
- не содержит отдельного teardown.

Подходит, если после теста ничего очищать не нужно.

## Фикстура с `yield`

```python
@pytest.fixture()
def user():
    created_user = {"name": "Roman"}

    yield created_user

    delete_user(created_user)
```

Такая фикстура:

- создаёт данные до теста;
- передаёт данные тесту через `yield`;
- выполняет очистку после теста.

---

# Параметр `scope`

Фикстуры имеют необязательный параметр:

```python
scope
```

Он определяет, как часто Pytest будет создавать фикстуру и выполнять её teardown.

Доступные значения:

- `function`;
- `class`;
- `module`;
- `session`.

По умолчанию используется:

```python
scope="function"
```

Пример явного указания:

```python
@pytest.fixture(scope="function")
def example_fixture():
    yield 42
```

---

# `scope="function"`

```python
@pytest.fixture(scope="function")
def my_fixture():
    print("Hello")
    yield 42
    print("Bye")
```

`function` — область действия по умолчанию.

Фикстура запускается отдельно для каждой тестовой функции, которая её использует.

Пример:

```python
def test_one(my_fixture):
    assert my_fixture == 42


def test_two(my_fixture):
    assert my_fixture == 42


def test_three(my_fixture):
    assert my_fixture == 42
```

Фикстура выполнится три раза:

```text
Hello
test_one
Bye

Hello
test_two
Bye

Hello
test_three
Bye
```

Для каждого теста создаётся собственный экземпляр данных фикстуры.

Используйте `function`, когда:

- тесты должны быть полностью изолированы;
- каждому тесту нужны отдельные данные;
- после каждого теста требуется очистка;
- состояние не должно передаваться между тестами.

---

# `scope="class"`

```python
@pytest.fixture(scope="class")
def my_fixture():
    print("Hello")
    yield 42
    print("Bye")
```

Фикстура выполняется один раз для одного тестового класса, независимо от количества тестовых методов внутри него.

Пример:

```python
class TestClassOne:

    def test_one(self, my_fixture):
        assert my_fixture == 42

    def test_two(self, my_fixture):
        assert my_fixture == 42


class TestClassTwo:

    def test_three(self, my_fixture):
        assert my_fixture == 42
```

Порядок будет примерно таким:

```text
Hello
TestClassOne.test_one
TestClassOne.test_two
Bye

Hello
TestClassTwo.test_three
Bye
```

Для `TestClassOne` фикстура создаётся один раз и используется двумя тестами.

Для `TestClassTwo` создаётся новый экземпляр фикстуры.

Используйте `class`, когда:

- несколько тестов одного класса используют общий ресурс;
- подготовка ресурса занимает много времени;
- состояние допустимо разделять между тестами одного класса.

---

# `scope="module"`

```python
@pytest.fixture(scope="module")
def my_fixture():
    print("Hello")
    yield 42
    print("Bye")
```

В Pytest модуль обычно означает один Python-файл с тестами.

Фикстура запускается один раз для каждого тестового модуля, который её использует.

Пример структуры:

```text
tests/
├── test_users.py
└── test_products.py
```

Если фикстура используется в обоих файлах, она выполнится:

- один раз для `test_users.py`;
- один раз для `test_products.py`.

Количество функций и классов внутри файла не имеет значения.

Используйте `module`, когда:

- всем тестам одного файла нужен общий ресурс;
- ресурс дорого создавать перед каждым тестом;
- допустимо использовать один экземпляр ресурса внутри модуля.

---

# `scope="session"`

```python
@pytest.fixture(scope="session")
def my_fixture():
    print("Hello")
    yield 42
    print("Bye")
```

Фикстура запускается один раз за всю тестовую сессию.

Все тестовые функции, классы и модули используют один экземпляр результата фикстуры.

Порядок:

```text
Hello

Запускаются все тесты из всех модулей

Bye
```

Используйте `session`, когда:

- ресурс должен быть общим для всего запуска;
- его создание занимает много времени;
- нужно один раз открыть общее соединение;
- нужно один раз подготовить глобальное тестовое окружение.

Примеры:

- общая конфигурация тестового запуска;
- запуск тестового сервера;
- создание общего API-клиента;
- дорогое подключение к внешней системе;
- подготовка глобальных тестовых данных.

---

# Сравнение областей действия

| Scope | Частота выполнения | Когда выполняется teardown |
|---|---|---|
| `function` | Перед каждым тестом | После каждого теста |
| `class` | Один раз для тестового класса | После всех тестов класса |
| `module` | Один раз для тестового файла | После всех тестов файла |
| `session` | Один раз за весь запуск Pytest | После завершения всей сессии |

Чем шире `scope`, тем реже запускается фикстура:

```text
function → class → module → session
```

При выборе `scope` важно учитывать изоляцию тестов.

Широкий `scope` ускоряет тесты, но повышает риск того, что тесты будут влиять друг на друга через общее изменяемое состояние.

---

# Общие фикстуры в `conftest.py`

Фикстуру можно объявить непосредственно в тестовом файле:

```python
# test_users.py

import pytest


@pytest.fixture()
def user():
    return {"name": "Roman"}


def test_user_name(user):
    assert user["name"] == "Roman"
```

В этом случае она будет доступна только в соответствующем тестовом модуле.

Если фикстуру необходимо использовать в нескольких тестовых файлах, её следует вынести в:

```text
conftest.py
```

Пример структуры:

```text
project/
├── conftest.py
└── tests/
    ├── test_users.py
    └── test_products.py
```

## Файл `conftest.py`

```python
import pytest


@pytest.fixture()
def test_data():
    return {"status": "ok"}
```

## Файл `test_users.py`

```python
def test_users(test_data):
    assert test_data["status"] == "ok"
```

## Файл `test_products.py`

```python
def test_products(test_data):
    assert test_data["status"] == "ok"
```

Импортировать фикстуру из `conftest.py` не нужно:

```python
# Так делать не требуется
from conftest import test_data
```

Pytest автоматически находит файл `conftest.py` и доступные в нём фикстуры.

---

# Область доступности `conftest.py`

Фикстуры из `conftest.py` доступны:

- тестам в той же директории;
- тестам во вложенных директориях.

Пример:

```text
project/
├── conftest.py
└── tests/
    ├── test_api.py
    └── ui/
        └── test_login.py
```

Фикстуры из корневого `conftest.py` будут доступны и в `test_api.py`, и в `test_login.py`.

Также во вложенной директории можно создать дополнительный `conftest.py`:

```text
project/
├── conftest.py
└── tests/
    ├── test_api.py
    └── ui/
        ├── conftest.py
        └── test_login.py
```

Фикстуры из `tests/ui/conftest.py` будут доступны тестам внутри `tests/ui`, но не тестам, расположенным выше.

---

# Автоматические фикстуры: `autouse`

По умолчанию фикстура запускается только тогда, когда тест запрашивает её по имени:

```python
def test_example(my_fixture):
```

Иногда фикстура должна выполняться автоматически для всех подходящих тестов.

Для этого используется:

```python
autouse=True
```

Пример:

```python
import pytest


@pytest.fixture(autouse=True)
def prepare_environment():
    print("Prepare environment")
    yield
    print("Clean environment")
```

Теперь явно передавать фикстуру в тест не нужно:

```python
def test_one():
    assert True


def test_two():
    assert True
```

Фикстура автоматически выполнится для обоих тестов.

---

## `autouse` вместе со `scope`

```python
@pytest.fixture(scope="module", autouse=True)
def prepare_module():
    print("Prepare module")
    yield
    print("Clean module")
```

Такая фикстура:

- запускается автоматически;
- выполняется один раз для каждого тестового модуля;
- завершает teardown после выполнения всех тестов модуля.

Другие примеры:

```python
@pytest.fixture(scope="function", autouse=True)
```

Автоматически запускается для каждого теста.

```python
@pytest.fixture(scope="class", autouse=True)
```

Автоматически запускается один раз для каждого тестового класса.

```python
@pytest.fixture(scope="session", autouse=True)
```

Автоматически запускается один раз за всю тестовую сессию.

---

# Когда использовать `autouse`

`autouse=True` удобно использовать для действий, которые обязательны для всех тестов:

- очистка состояния перед каждым тестом;
- настройка логирования;
- установка переменных окружения;
- автоматическое начало и завершение транзакции;
- общая подготовка тестового окружения.

Однако `autouse` следует использовать осторожно.

Если фикстура запускается неявно, по коду теста может быть непонятно:

- откуда появились данные;
- что было выполнено перед тестом;
- почему изменилось окружение.

Если фикстура нужна только отдельным тестам, лучше указывать её явно:

```python
def test_example(my_fixture):
```

---

# Фикстуры как precondition и postcondition

Фикстура с `yield` может одновременно выполнять:

- **precondition** — предусловие;
- **postcondition** — постусловие.

Пример:

```python
import pytest


@pytest.fixture()
def created_user():
    user = create_user()  # Precondition

    yield user

    delete_user(user)     # Postcondition
```

Тест:

```python
def test_user_profile(created_user):
    assert created_user["name"] == "Roman"
```

Последовательность:

1. Создаётся пользователь.
2. Пользователь передаётся в тест.
3. Выполняется тест.
4. Пользователь удаляется.

---

# Главное о фикстурах

- Фикстура — функция для подготовки тестов и управления тестовым окружением.
- Фикстуры объявляются с помощью `@pytest.fixture`.
- Pytest передаёт результат фикстуры в тест по имени аргумента.
- `return` используется, когда необходима только подготовка данных.
- `yield` позволяет выполнить setup до теста и teardown после теста.
- Код до `yield` — предусловие.
- Код после `yield` — постусловие или очистка.
- `scope` определяет частоту выполнения фикстуры.
- По умолчанию используется `scope="function"`.
- `class` создаёт фикстуру один раз для тестового класса.
- `module` создаёт фикстуру один раз для тестового файла.
- `session` создаёт фикстуру один раз за весь запуск.
- Общие фикстуры размещаются в `conftest.py`.
- Импортировать фикстуры из `conftest.py` вручную не нужно.
- `autouse=True` автоматически запускает фикстуру для всех тестов соответствующей области действия.
- Чем шире `scope`, тем выше скорость, но тем ниже изоляция тестов.