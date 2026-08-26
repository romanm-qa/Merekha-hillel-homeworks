# L12: User Libraries

## Пользовательские библиотеки

Основные возможности Robot Framework предоставляются тестовыми библиотеками.

Robot Framework содержит встроенные библиотеки, но также позволяет:

- устанавливать сторонние библиотеки;
- создавать собственные библиотеки;
- реализовывать собственные keywords на Python;
- использовать Python-пакеты внутри Robot Framework-тестов.

Пользовательская библиотека может быть реализована:

- как Python-модуль;
- как Python-класс.

---

## Создание библиотеки

### Библиотека на основе модуля

Имя библиотеки совпадает с именем Python-файла.

Например, файл:

```text
Library.py
```

создаёт библиотеку с именем `Library`.

Модульные библиотеки:

- не могут принимать аргументы при импорте;
- всегда имеют глобальную область видимости (`GLOBAL`).

### Библиотека на основе класса

Имя библиотеки обычно совпадает с именем класса.

Если имя модуля совпадает с именем класса, Robot Framework позволяет не указывать имя класса отдельно.

Например, класс `ChildLib` внутри модуля `parent.ChildLib` можно импортировать так:

```robot
*** Settings ***
Library    parent.ChildLib
```

Если имя класса отличается от имени модуля, класс необходимо указывать явно.

Классовые библиотеки могут принимать аргументы. Они передаются через настройку `Library` и попадают в метод `__init__`.

```python
from example import Connection


class MyLibrary:

    def __init__(self, host, port=80):
        self._conn = Connection(host, int(port))

    def send_message(self, message):
        self._conn.send(message)
```

Импорт библиотеки с аргументами:

```robot
*** Settings ***
Library    MyLibrary    localhost    8080
```

Аргументы могут быть:

- обычными значениями;
- переменными Robot Framework;
- значениями, переданными через командную строку.

---

## Область видимости библиотеки

Поскольку библиотека является Python-объектом, её состояние может изменяться во время выполнения тестов.

Область видимости задаётся атрибутом:

```python
ROBOT_LIBRARY_SCOPE = "TEST"
```

Доступны три значения.

### `TEST`

Значение по умолчанию.

Для каждого тест-кейса создаётся новый экземпляр библиотеки.

```python
ROBOT_LIBRARY_SCOPE = "TEST"
```

Преимущество: тесты остаются независимыми друг от друга.

Все неизвестные Robot Framework значения области видимости также обрабатываются как `TEST`.

### `SUITE`

Новый экземпляр создаётся для каждого test suite.

```python
ROBOT_LIBRARY_SCOPE = "SUITE"
```

Каждый suite, включая suite более высокого уровня, получает собственный экземпляр библиотеки.

### `GLOBAL`

Один экземпляр создаётся на весь запуск тестов.

```python
ROBOT_LIBRARY_SCOPE = "GLOBAL"
```

Модульные библиотеки всегда имеют область видимости `GLOBAL`.

> Если одну библиотеку импортировать несколько раз с разными аргументами, для каждого импорта будет создан отдельный экземпляр.

---

## Версия библиотеки

Версия библиотеки может быть задана с помощью:

```python
ROBOT_LIBRARY_VERSION = "1.0"
```

или:

```python
__version__ = "1.0"
```

Robot Framework записывает версию:

- в `syslog`;
- в документацию, созданную через Libdoc.

---

## Формат документации

Формат документации библиотеки задаётся переменной:

```python
ROBOT_LIBRARY_DOC_FORMAT = "ROBOT"
```

Поддерживаемые значения:

- `ROBOT` — стандартный формат Robot Framework;
- `HTML`;
- `TEXT` — обычный текст;
- `reST` — reStructuredText.

Для использования `reST` необходимо установить пакет `docutils`.

```python
"""Library documentation written using reStructuredText."""

ROBOT_LIBRARY_DOC_FORMAT = "reST"


def keyword():
    """Keyword documentation."""
    pass
```

---

## Декоратор `@library`

Для настройки классовой библиотеки можно использовать декоратор `library` из пакета `robot.api.deco`.

```python
from robot.api.deco import library


@library
class MyLibrary:
    pass
```

Декоратор поддерживает параметры:

- `scope` — область видимости;
- `version` — версия библиотеки;
- `converter` — пользовательские преобразователи аргументов;
- `doc_format` — формат документации;
- `listener` — listener для получения событий выполнения;
- `auto_keywords` — автоматический поиск keywords.

Пример:

```python
from robot.api.deco import keyword, library


@library(scope="SUITE", version="1.0")
class MyLibrary:

    @keyword
    def send_message(self, message):
        print(message)
```

При использовании `@library` автоматическое обнаружение keywords по умолчанию отключается:

```python
ROBOT_AUTO_KEYWORDS = False
```

Поэтому каждый метод, который должен стать keyword, необходимо пометить декоратором:

```python
@keyword
```

Автоматическое обнаружение можно включить:

```python
@library(auto_keywords=True)
class MyLibrary:
    pass
```

Параметры декоратора имеют приоритет над атрибутами класса.

---

# Создание Keywords

При использовании статического API Robot Framework применяет introspection — анализирует функции и методы библиотеки и автоматически создаёт из них keywords.

По умолчанию функции и методы, начинающиеся с `_`, не становятся keywords.

```python
def public_keyword():
    pass


def _helper_function():
    pass
```

В этом примере только `public_keyword` будет доступен в Robot Framework.

---

## Управление доступными Keywords

Автоматическое создание keywords иногда приводит к тому, что Robot Framework добавляет:

- импортированные функции модуля;
- унаследованные методы класса;
- вспомогательные методы.

Чтобы этого избежать, можно отключить автоматическое обнаружение:

```python
ROBOT_AUTO_KEYWORDS = False
```

Затем нужные функции отмечаются декоратором `@keyword`.

```python
from robot.api.deco import keyword


ROBOT_AUTO_KEYWORDS = False


@keyword
def login(username, password):
    pass


def helper():
    pass
```

В модульной библиотеке также можно использовать переменную `__all__`:

```python
__all__ = ["login", "logout"]
```

Она определяет функции, которые должны быть доступны как keywords.

Для явного исключения функции используется декоратор `@not_keyword`.

```python
from robot.api.deco import not_keyword


@not_keyword
def helper_function():
    pass
```

---

## Имена Keywords

Robot Framework при поиске keyword игнорирует:

- регистр;
- пробелы;
- символы подчёркивания.

Метод:

```python
def hello_world():
    pass
```

можно вызвать разными способами:

```robot
Hello World
hello world
Hello_World
HELLO_WORLD
```

---

## Пользовательское имя Keyword

Другое имя можно указать через декоратор `@keyword`.

```python
from robot.api.deco import keyword


@keyword("Login via user panel")
def login(username, password):
    pass
```

Использование:

```robot
*** Test Cases ***
User Login
    Login via user panel    user@example.com    password
```

Внутренне метод называется `login`, но Robot Framework видит его как `Login via user panel`.

Функции и методы с явно заданным именем создают keywords, даже если их Python-имя начинается с `_`.

---

## Теги Keywords

К keyword можно добавить теги несколькими способами.

### Через декоратор

```python
from robot.api.deco import keyword


@keyword(tags=["tag1", "tag2"])
def login(username, password):
    pass
```

### Одновременно с пользовательским именем

```python
@keyword("Custom name", ["tag1", "tag2"])
def another_example():
    pass
```

### Через docstring

```python
def yet_another_keyword():
    """
    Tags: tag1, tag2
    """
```

---

# Преобразование аргументов

Если Robot Framework не получает информацию о типе аргумента, значение передаётся в Python как строка.

```python
def set_count(count):
    count = int(count)
```

Для ручного преобразования можно использовать:

- `int`;
- `float`;
- `str`;
- другие Python-классы.

---

## Преобразование Boolean

В Python любая непустая строка считается `True`.

```python
bool("False")  # True
```

Поэтому для строковых значений `False`, `NO` и `NONE` рекомендуется использовать:

```python
from robot.utils import is_truthy


def example(value):
    if is_truthy(value):
        pass
```

---

## Аннотации типов

Robot Framework использует аннотации типов для автоматического преобразования аргументов.

```python
def example_keyword(count: int, case_insensitive: bool = True):
    if case_insensitive:
        pass
```

При вызове keyword строковое значение для `count` будет преобразовано в `int`, а значение для `case_insensitive` — в `bool`.

---

## Типы через декоратор `@keyword`

Декоратор `@keyword` принимает параметр `types`.

Типы можно передать словарём:

```python
from robot.api.deco import keyword


@keyword(types={"second": float})
def example1(first, second, third):
    pass
```

Или списком:

```python
@keyword(types=[None, float])
def example2(first, second, third):
    pass
```

В списке типы соответствуют позиционным аргументам.

`None` означает, что для аргумента тип не задан.

Если используется параметр `types`, аннотации типов игнорируются.

Полностью отключить преобразование типов можно так:

```python
@keyword(types=None)
def example(value):
    pass
```

---

## Преобразование на основе значений по умолчанию

Если аргумент имеет значение по умолчанию, Robot Framework пытается преобразовать переданное значение к его типу.

```python
def example_keyword(count=-1, case_insensitive=True):
    pass
```

Robot Framework попробует преобразовать:

- `count` в `int`;
- `case_insensitive` в `bool`.

Такое преобразование является неявным. Если оно не получилось, Robot Framework может передать исходное значение.

Если одновременно указаны аннотация типа и значение по умолчанию, приоритет имеет аннотация.

---

## Несколько допустимых типов

Аргумент может поддерживать несколько типов.

Начиная с Python 3.10 можно использовать оператор `|`:

```python
def example(
    length: int | float,
    padding: int | str | None = None,
):
    pass
```

Robot Framework последовательно пытается применить указанные преобразования.

```robot
*** Test Cases ***
Conversion
    Example    10
    Example    1.5
    Example    ${10}
    Example    ${1.5}
```

Результат:

- строка `10` преобразуется в `int`;
- строка `1.5` преобразуется в `float`;
- готовый `int` принимается без преобразования;
- готовый `float` принимается без преобразования.

Если значение уже соответствует одному из типов, повторное преобразование не выполняется.

В параметре `types` декоратора также можно использовать кортеж типов.

---

## Пользовательские преобразователи

Если Robot Framework не поддерживает требуемое преобразование, можно создать custom converter.

Он настраивается через параметр `converter` декоратора `@library`.

Пользовательские преобразователи полезны для:

- собственных классов;
- специальных форматов данных;
- доменных объектов;
- нестандартных значений.

---

# Пользовательские декораторы

Собственные декораторы могут изменять:

- сигнатуру функции;
- имя функции;
- документацию;
- аннотации.

Из-за этого Robot Framework может неправильно определить аргументы keyword или создать некорректную Libdoc-документацию.

Чтобы сохранить метаданные функции, следует использовать `functools.wraps`.

```python
from functools import wraps


def custom_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

Также можно использовать специализированные библиотеки:

- `decorator`;
- `wrapt`.

---

# Embedded Arguments

Аргументы можно встраивать непосредственно в имя keyword.

```python
from robot.api.deco import keyword


@keyword(r"Add ${quantity:\d+} copies of ${item} to cart")
def add_copies_to_cart(quantity, item):
    pass
```

Использование:

```robot
*** Test Cases ***
Add Products
    Add 7 copies of coffee to cart
```

Здесь:

- `${quantity}` получает значение `7`;
- `${item}` получает значение `coffee`;
- `\d+` ограничивает `quantity` только цифрами.

Имена embedded arguments должны совпадать с именами аргументов Python-функции.

По умолчанию embedded arguments передаются как строки, но для них также можно использовать преобразование типов.

---

# Взаимодействие с Robot Framework

Пользовательские библиотеки могут:

- отправлять сообщения в лог;
- выводить сообщения в консоль;
- возвращать значения;
- завершать keywords с ошибкой;
- пропускать тесты;
- продолжать выполнение после ошибки;
- полностью останавливать выполнение тестов.

---

## Ошибки в Keywords

Любое необработанное исключение внутри keyword приводит к падению keyword.

```python
def verify_value(actual, expected):
    if actual != expected:
        raise AssertionError(
            f"Expected {expected}, but got {actual}"
        )
```

Для обычных исключений Robot Framework показывает:

- имя класса исключения;
- сообщение исключения.

Для стандартных проверок вроде `AssertionError` обычно отображается только сообщение.

Чтобы скрыть имя пользовательского исключения, можно добавить:

```python
ROBOT_SUPPRESS_NAME = True
```

> В учебном материале встречается написание `ROBOT_SUPRESS_NAME`, но правильное имя атрибута — `ROBOT_SUPPRESS_NAME`.

HTML-сообщение об ошибке должно начинаться с:

```text
*HTML*
```

Сообщения длиннее 40 строк сокращаются в отчёте, но полностью сохраняются в log-файле.

Traceback отображается в логах только при уровне логирования `DEBUG`.

---

## Специальные исключения Robot Framework

Исключения доступны в модуле:

```python
robot.api
```

### `Failure`

Сообщает о неуспешной проверке.

По поведению похож на `AssertionError`.

```python
from robot.api import Failure


def validate(value):
    if not value:
        raise Failure("Value is empty")
```

### `Error`

Сообщает об ошибке выполнения, например о неправильном использовании keyword.

На практике ведёт себя аналогично `Failure`.

### `ContinuableFailure`

Фиксирует ошибку, но позволяет продолжить выполнение теста.

Альтернативно пользовательское исключение может содержать:

```python
ROBOT_CONTINUE_ON_FAILURE = True
```

### `SkipExecution`

Помечает тест как пропущенный.

Альтернативный атрибут:

```python
ROBOT_SKIP_EXECUTION = True
```

### `FatalError`

Сообщает о критической ошибке и полностью останавливает выполнение.

Альтернативный атрибут:

```python
ROBOT_EXIT_ON_FAILURE = True
```

---

# Логирование

## Стандартный вывод

Всё, что keyword записывает в стандартный поток вывода, попадает в log-файл как одно сообщение уровня `INFO`.

```python
def keyword():
    print("Message")
```

Сообщения из стандартного потока ошибок также попадают в лог и дополнительно выводятся в консоль после завершения keyword.

---

## Уровни логирования

Уровень можно указать с помощью специального префикса:

```text
*TRACE*
*DEBUG*
*INFO*
*WARN*
*ERROR*
*HTML*
```

Пример:

```python
print("*WARN* Something happened")
```

Сообщения `WARN` и `ERROR`:

- автоматически выводятся в консоль;
- выделяются в отдельном разделе log-файла.

Уровень `HTML` позволяет интерпретировать HTML-разметку. В логе такое сообщение сохраняется с уровнем `INFO`.

При необходимости можно передать точный timestamp в миллисекундах от Unix epoch:

```text
*INFO:1308435758660* Message
```

---

## Немедленный вывод в консоль

Для немедленного вывода можно использовать `sys.__stdout__` или `sys.__stderr__`.

```python
import sys


def my_keyword(arg):
    sys.__stdout__.write(f"Got arg {arg}\n")
```

Такое сообщение не попадёт в log-файл.

---

## Robot Framework Logging API

Предпочтительный способ логирования — использовать `robot.api.logger`.

```python
from robot.api import logger


def my_keyword(arg):
    logger.debug(f"Got argument {arg}")
    logger.info("<i>HTML message</i>", html=True)
    logger.console("Hello, console!")
```

Основные методы:

```python
logger.debug("Debug message")
logger.info("Info message")
logger.warn("Warning message")
logger.error("Error message")
logger.console("Console message")
```

Вывод одновременно в лог и консоль:

```python
logger.info(
    f"Got arg {arg}",
    also_console=True,
)
```

Преимущества Robot Framework Logging API:

- точные timestamps;
- поддержка HTML;
- вывод в log-файл;
- вывод в консоль.

Недостаток: библиотека зависит от Robot Framework API.

Если Robot Framework не запущен, сообщения перенаправляются в стандартный Python-модуль `logging`.

---

## Стандартный модуль `logging`

Можно использовать обычный Python-модуль `logging`.

```python
import logging


logger = logging.getLogger(__name__)


def my_keyword(arg):
    logger.info("Got argument %s", arg)
```

Сообщения root logger передаются в log-файл Robot Framework.

Преимущества:

- библиотека не зависит напрямую от Robot Framework API;
- сообщения получают точные timestamps.

Недостаток:

- HTML-разметка не поддерживается.

Соответствие уровней Python и Robot Framework:

- `DEBUG` → `DEBUG`;
- `INFO` → `INFO`;
- `WARNING` → `WARN`;
- `ERROR` → `ERROR`;
- `CRITICAL` → `ERROR`.

Пользовательские уровни преобразуются к ближайшему меньшему стандартному уровню.

---

## Логирование во время инициализации

Библиотека может писать сообщения во время создания экземпляра.

Такие сообщения:

- не попадают в обычный log-файл;
- записываются в `syslog`;
- предупреждения и ошибки отображаются в разделе ошибок выполнения тестов.

---

# Возвращение значений

Keyword может вернуть любой Python-объект через `return`.

```python
from mymodule import MyObject


def return_string():
    return "Hello, world!"


def return_object(name):
    return MyObject(name)
```

Использование в Robot Framework:

```robot
*** Test Cases ***
Return Values
    ${message}=    Return String
    ${object}=     Return Object    Robot
```

Объекты можно передавать в keywords других библиотек.

---

## Возвращение нескольких значений

Python-функция может вернуть несколько объектов:

```python
def return_user():
    return "Roman", 29
```

Их можно сохранить:

### В несколько scalar variables

```robot
${name}    ${age}=    Return User
```

### В list variable

```robot
@{user}=    Return User
```

### В комбинацию переменных

Возвращаемое значение должно быть list-like объектом. В Python несколько значений по умолчанию возвращаются как tuple.

---

# Использование потоков

Если библиотека использует threads, взаимодействовать с Robot Framework следует только из главного потока.

Worker threads не должны напрямую:

- писать сообщения в Robot Framework log;
- возвращать значения Robot Framework;
- передавать исключения Robot Framework.

Рабочий поток должен передать результат, ошибку или сообщение главному потоку.

Если один keyword запускает фоновую задачу, другой keyword должен проверять её состояние.

---

# Внутренние модули Robot Framework

Внутренние API Robot Framework могут предоставлять информацию о:

- выполняемых тестах;
- настройках;
- автоматических переменных;
- активных библиотеках.

Однако внутренние API могут значительно изменяться между версиями, поэтому их использование не рекомендуется.

Наиболее безопасным внутренним API считается библиотека `BuiltIn`.

---

## Получение автоматической переменной

Пример получения `${OUTPUTDIR}`:

```python
import os.path

from robot.libraries.BuiltIn import BuiltIn


def do_something(argument):
    output = do_something_that_creates_a_lot_of_output(argument)

    output_dir = BuiltIn().replace_variables("${OUTPUTDIR}")
    path = os.path.join(output_dir, "results.txt")

    with open(path, "w") as file:
        file.write(output)

    print(
        '*HTML* Output written to '
        '<a href="results.txt">results.txt</a>'
    )
```

`BuiltIn().replace_variables()` заменяет Robot Framework-переменную её фактическим значением.

---

# Расширение существующих библиотек

Существующие встроенные и сторонние библиотеки можно расширять несколькими способами.

## Изменение исходного кода

Можно напрямую изменить исходный код библиотеки.

Преимущества:

- удобно при подготовке изменений для отправки разработчикам библиотеки;
- можно исправить или расширить исходную реализацию.

Недостатки:

- сложнее обновлять библиотеку;
- обновление может перезаписать изменения;
- модификации могут быть неочевидны другим пользователям.

---

## Наследование классовой библиотеки

Классовую библиотеку можно расширить через наследование.

```python
class ExtendedLibrary(OriginalLibrary):

    def new_keyword(self):
        pass
```

Преимущества:

- расширение явно отделено от оригинальной библиотеки;
- используется новое имя библиотеки;
- не нужно изменять исходный код.

Недостатки:

- оригинальную и расширенную библиотеки сложно использовать одновременно;
- их keywords могут пересекаться;
- состояния двух экземпляров не будут синхронизированы.

---

## Получение активного экземпляра библиотеки

Через `BuiltIn` можно получить активный экземпляр уже импортированной библиотеки:

```python
from robot.libraries.BuiltIn import BuiltIn


def title_should_start_with(expected):
    selenium_library = BuiltIn().get_library_instance(
        "SeleniumLibrary"
    )

    title = selenium_library.get_title()

    if not title.startswith(expected):
        raise AssertionError(
            f"Title '{title}' did not start with '{expected}'"
        )
```

Этот подход позволяет создать новый keyword, использующий состояние и методы уже активной библиотеки.

Преимущество: используется тот же экземпляр библиотеки, поэтому его состояние остаётся синхронизированным.

---

# Краткое сравнение библиотек

| Характеристика | Module-based | Class-based |
|---|---|---|
| Принимает аргументы | Нет | Да |
| Поддерживает `__init__` | Нет | Да |
| Область видимости | Всегда `GLOBAL` | `TEST`, `SUITE`, `GLOBAL` |
| Хранение состояния | Глобальное | Зависит от scope |
| Расширение наследованием | Нет | Да |
| Простота реализации | Проще | Более гибкая |

---

# Главное из урока

- Пользовательские библиотеки позволяют создавать Python-keywords для Robot Framework.
- Библиотека может быть реализована как модуль или класс.
- Только классовые библиотеки могут принимать аргументы при импорте.
- Область видимости задаётся через `ROBOT_LIBRARY_SCOPE`.
- Возможные scope: `TEST`, `SUITE` и `GLOBAL`.
- Модульные библиотеки всегда имеют scope `GLOBAL`.
- `@library` используется для настройки классовой библиотеки.
- При использовании `@library` автоматическое обнаружение keywords по умолчанию отключено.
- `@keyword` создаёт keyword, задаёт ему имя, теги и типы аргументов.
- `@not_keyword` явно исключает функцию из списка keywords.
- Robot Framework игнорирует регистр, пробелы и подчёркивания в именах keywords.
- Аргументы можно преобразовывать вручную, через аннотации, значения по умолчанию или параметр `types`.
- Embedded arguments позволяют включать значения непосредственно в имя keyword.
- Любое необработанное исключение приводит к падению keyword.
- Robot Framework предоставляет специальные исключения для failure, skip, продолжения и остановки выполнения.
- Для логирования можно использовать `print`, `robot.api.logger` или стандартный модуль `logging`.
- Keywords могут возвращать строки, коллекции и любые другие Python-объекты.
- Внутренние API Robot Framework могут изменяться, поэтому безопаснее использовать `BuiltIn`.
- Существующие библиотеки можно расширять изменением кода, наследованием или получением активного экземпляра через `BuiltIn`.