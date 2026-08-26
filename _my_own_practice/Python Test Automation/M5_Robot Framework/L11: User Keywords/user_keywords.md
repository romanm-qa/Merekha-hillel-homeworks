# L11: User Keywords

## User Keywords

**User Keywords** — это пользовательские ключевые слова, которые создаются непосредственно в Robot Framework (`.robot`) файлах.

Они отличаются от **Library Keywords**:

* **User Keywords** определяются пользователем в `.robot` файлах.
* **Library Keywords** предоставляются подключёнными библиотеками.

User Keywords позволяют объединять несколько низкоуровневых действий в одно переиспользуемое действие.

Например, вместо повторения:

```robot
Open Browser    http://host/login.html
Title Should Be    Login Page
```

можно создать собственный keyword:

```robot
*** Keywords ***
Open Login Page
    Open Browser    http://host/login.html
    Title Should Be    Login Page
```

А затем использовать его в тестах:

```robot
*** Test Cases ***
Login Page Test
    Open Login Page
```

---

## Где определяются User Keywords

User Keywords создаются в секции:

```robot
*** Keywords ***
```

Они могут находиться в:

* test suite файле;
* test suite initialization файле;
* resource-файле.

Keyword из resource-файла становится доступен другим файлам, которые импортируют этот resource.

Keywords, определённые непосредственно в test suite, доступны только внутри этого suite.

---

## User Keyword Syntax

Базовый синтаксис:

```robot
*** Keywords ***
Open Login Page
    Open Browser    http://host/login.html
    Title Should Be    Login Page
```

Keyword также может принимать аргументы:

```robot
*** Keywords ***
Title Should Start With
    [Arguments]    ${expected}
    ${title} =    Get Title
    Should Start With    ${title}    ${expected}
```

Здесь:

* `Title Should Start With` — имя keyword;
* `[Arguments]` — настройка аргументов;
* `${expected}` — входной аргумент;
* `${title}` — переменная, получившая результат `Get Title`.

---

# Keyword Settings

Для User Keywords доступны специальные настройки.

Основные:

* `[Documentation]` — документация keyword;
* `[Tags]` — теги;
* `[Arguments]` — аргументы;
* `[Return]` — возвращаемое значение (устаревающий подход);
* `[Teardown]` — действия после выполнения keyword;
* `[Timeout]` — максимальное время выполнения.

Пример:

```robot
*** Keywords ***
Example Keyword
    [Documentation]    Example documentation
    [Tags]    smoke    login
    [Arguments]    ${username}
    Log    ${username}
```

---

# Keyword Documentation

Документация задаётся через:

```robot
[Documentation]
```

Пример:

```robot
*** Keywords ***
Login User
    [Documentation]    Logs user into the application
    Log    Logging in
```

Первая логическая строка документации отображается в test logs.

Полную документацию можно использовать при генерации документации через **Libdoc**.

---

## Deprecated Keywords

Keyword можно пометить устаревшим с помощью `DEPRECATED` в начале документации.

Например:

```robot
*** Keywords ***
Old Login
    [Documentation]    DEPRECATED Use New Login instead.
    Log    Old login
```

При использовании такого keyword Robot Framework выдаст warning.

---

# Keyword Tags

User Keywords могут иметь теги.

Например:

```robot
*** Keywords ***
Settings Tags Using Separate Setting
    [Tags]    my    fine    tags
    No Operation
```

Теги также можно указать в документации:

```robot
*** Keywords ***
Settings Tags Using Documentation
    [Documentation]    I have documentation.
    ...                Tags: my, fine, tags
    No Operation
```

Теги отображаются:

* в logs;
* в документации Libdoc;
* могут использоваться для поиска keywords.

Командные опции:

```text
--removekeywords
--flattenkeywords
```

также могут работать с тегами.

> Имена тегов, начинающиеся с `robot-` и `robot:`, зарезервированы Robot Framework.

---

# Keyword Arguments

Аргументы User Keyword задаются через:

```robot
[Arguments]
```

Robot Framework поддерживает несколько типов аргументов:

1. Positional Arguments
2. Default Values
3. Variable Number of Arguments
4. Free Named Arguments
5. Named-Only Arguments

---

# Positional Arguments

Самый простой вариант — позиционные аргументы.

Один аргумент:

```robot
*** Keywords ***
One Argument
    [Arguments]    ${arg_name}
    Log    Got argument ${arg_name}
```

Использование:

```robot
One Argument    Hello
```

В результате:

```text
${arg_name} = Hello
```

---

## Несколько позиционных аргументов

```robot
*** Keywords ***
Multiple Arguments
    [Arguments]    ${arg1}    ${arg2}    ${arg3}
    Log    1st argument: ${arg1}
    Log    2nd argument: ${arg2}
    Log    3rd argument: ${arg3}
```

Вызов:

```robot
Multiple Arguments    one    two    three
```

Соответствие происходит по позиции:

```text
one   → ${arg1}
two   → ${arg2}
three → ${arg3}
```

Рекомендуется использовать понятные имена аргументов в lowercase.

---

# Default Values

Аргументы могут иметь значения по умолчанию.

Синтаксис:

```robot
${argument}=default value
```

Например:

```robot
*** Keywords ***
One Argument With Default Value
    [Arguments]    ${arg}=default value
    Log    Got argument ${arg}
```

Keyword можно вызвать вообще без аргумента:

```robot
One Argument With Default Value
```

Тогда:

```text
${arg} = default value
```

Либо передать своё значение:

```robot
One Argument With Default Value    custom
```

Тогда:

```text
${arg} = custom
```

---

## Несколько аргументов со значениями по умолчанию

```robot
*** Keywords ***
Two Arguments With Defaults
    [Arguments]    ${arg1}=default 1    ${arg2}=${VARIABLE}
    Log    1st argument ${arg1}
    Log    2nd argument ${arg2}
```

Keyword принимает от `0` до `2` аргументов.

---

## Required + Optional Argument

Можно комбинировать обязательные и необязательные аргументы:

```robot
*** Keywords ***
One Required And One With Default
    [Arguments]    ${required}    ${optional}=default
    Log    Required: ${required}
    Log    Optional: ${optional}
```

Вызов:

```robot
One Required And One With Default    hello
```

Результат:

```text
${required} = hello
${optional} = default
```

Или:

```robot
One Required And One With Default    hello    world
```

Результат:

```text
${required} = hello
${optional} = world
```

Обязательные positional arguments должны находиться **до аргументов со значениями по умолчанию**.

---

## Default Value Based on Earlier Argument

Значение по умолчанию может зависеть от ранее объявленного аргумента:

```robot
*** Keywords ***
Default Based On Earlier Argument
    [Arguments]    ${a}    ${b}=${a}    ${c}=${a} and ${b}
    Should Be Equal    ${a}    ${b}
    Should Be Equal    ${c}    ${a} and ${b}
```

---

# Variable Number of Arguments

Robot Framework позволяет создавать keywords, принимающие произвольное количество аргументов.

Используется list variable:

```robot
@{varargs}
```

Это аналог идеи Python:

```python
*args
```

---

## Любое количество аргументов

```robot
*** Keywords ***
Any Number Of Arguments
    [Arguments]    @{varargs}
    Log Many    @{varargs}
```

Можно вызвать:

```robot
Any Number Of Arguments
```

или:

```robot
Any Number Of Arguments    one
```

или:

```robot
Any Number Of Arguments    one    two    three
```

Все переданные значения попадут в:

```robot
@{varargs}
```

---

## Один обязательный + любое количество дополнительных

```robot
*** Keywords ***
One Or More Arguments
    [Arguments]    ${required}    @{rest}
    Log Many    ${required}    @{rest}
```

Первое значение попадёт в:

```robot
${required}
```

Все остальные:

```robot
@{rest}
```

---

## Required + Default + Varargs

Все варианты можно комбинировать:

```robot
*** Keywords ***
Required, Default, Varargs
    [Arguments]    ${req}    ${opt}=42    @{others}
    Log    Required: ${req}
    Log    Optional: ${opt}
    Log    Others:
    FOR    ${item}    IN    @{others}
        Log    ${item}
    END
```

Порядок:

```text
required → default → varargs
```

Например:

```robot
Required, Default, Varargs    A    100    B    C
```

получим:

```text
${req} = A
${opt} = 100
@{others} = [B, C]
```

---

# Free Named Arguments

Robot Framework поддерживает произвольные **именованные аргументы**.

Используется dictionary variable:

```robot
&{named}
```

Это похоже на Python:

```python
**kwargs
```

Пример:

```robot
*** Keywords ***
Free Named Only
    [Arguments]    &{named}
    Log Many    &{named}
```

Keyword может принимать произвольные аргументы вида:

```text
name=value
```

---

## Positional + Free Named

```robot
*** Keywords ***
Positional And Free Named
    [Arguments]    ${required}    &{extra}
    Log Many    ${required}    &{extra}
```

Первый аргумент:

```robot
${required}
```

остальные именованные аргументы:

```robot
&{extra}
```

---

## Varargs + Free Named

Можно комбинировать `@{args}` и `&{config}`:

```robot
*** Keywords ***
Run Program
    [Arguments]    @{args}    &{config}
    Run Process    program.py    @{args}    &{config}
```

Здесь:

```text
@{args}   → дополнительные positional arguments
&{config} → дополнительные named arguments
```

`&{...}` должен находиться последним среди аргументов keyword.

---

# Named-Only Arguments

**Named-only arguments** похожи на Python keyword-only arguments.

Они должны передаваться по имени.

При наличии `@{varargs}` аргументы после него становятся named-only:

```robot
*** Keywords ***
With Varargs
    [Arguments]    @{varargs}    ${named}
    Log Many    @{varargs}    ${named}
```

`${named}` необходимо передавать как named argument.

---

## Named-Only без Varargs

Если `@{varargs}` не нужны, используется:

```robot
@{}
```

Например:

```robot
*** Keywords ***
Without Varargs
    [Arguments]    @{}    ${first}    ${second}
    Log Many    ${first}    ${second}
```

`@{}` служит разделителем: аргументы после него являются named-only.

---

## Positional + Named-Only

```robot
*** Keywords ***
With Positional
    [Arguments]    ${positional}    @{}    ${named}
    Log Many    ${positional}    ${named}
```

Здесь:

```text
${positional} → positional
${named}      → named-only
```

---

## Named-Only + Free Named

Можно комбинировать:

```robot
*** Keywords ***
With Free Named
    [Arguments]    @{varargs}    ${named only}    &{free named}
    Log Many    @{varargs}    ${named only}    &{free named}
```

---

## Default Values для Named-Only

Named-only arguments также могут иметь default values:

```robot
*** Keywords ***
With And Without Defaults
    [Arguments]    @{}    ${opt}=default    ${req}    ${opt2}=default 2
    Log Many    ${opt}    ${req}    ${opt2}
```

В отличие от обычных positional arguments, порядок named-only аргументов с default и без default не имеет значения.

---

## Краткое сравнение с Python

| Robot Framework | Python           | Назначение                           |
| --------------- | ---------------- | ------------------------------------ |
| `${arg}`        | обычный параметр | Один аргумент                        |
| `${arg}=value`  | `arg=value`      | Default value                        |
| `@{args}`       | `*args`          | Произвольные positional arguments    |
| `&{kwargs}`     | `**kwargs`       | Произвольные named arguments         |
| `@{}`           | `*`              | Разделитель для named-only arguments |

Таким образом, система аргументов User Keywords во многом похожа на механизм аргументов функций Python.

# L11: User Keywords — Part 2

# Embedding Arguments Into Keyword Names

Robot Framework позволяет помещать аргументы **прямо в имя User Keyword**.

Это позволяет создавать keywords, которые выглядят почти как обычные предложения.

Например:

```robot
*** Keywords ***
Select ${animal} from list
    Open Page    Pet Selection
    Select Item From List    animal_list    ${animal}
```

Использование:

```robot
*** Test Cases ***
Example
    Select dog from list
```

Robot Framework определит:

```text
${animal} = dog
```

Главное преимущество такого подхода — высокая читаемость тестов.

---

## Ограничения Embedded Arguments

Keywords с embedded arguments:

* работают только для User Keywords;
* не могут одновременно использовать обычные `[Arguments]`;
* не поддерживают default values;
* не поддерживают variable number of arguments.

Также пробелы и `_` в таких именах **не игнорируются**, в отличие от обычного сопоставления keyword names.

Регистр при этом не учитывается.

---

# Несколько Embedded Arguments

В имя keyword можно встроить несколько аргументов:

```robot
*** Keywords ***
Show "${breed}" "${name}" in console
    Log    ${name} is a ${breed}
```

Использование:

```robot
*** Test Cases ***
Example
    Show "Great Dane" "Daisy" in console
```

Получим:

```text
${breed} = Great Dane
${name} = Daisy
```

Кавычки помогают Robot Framework определить границы значений.

---

# Matching Embedded Arguments

Robot Framework использует **regular expressions** для поиска значений embedded arguments.

По умолчанию используется шаблон, способный сопоставить практически любую строку.

Из-за этого иногда возникают неоднозначности.

Например:

```robot
*** Keywords ***
I execute "${cmd}"
    Run Process    ${cmd}    shell=True

I execute "${cmd}" with "${opts}"
    Run Process    ${cmd}    ${opts}    shell=True
```

Использование:

```robot
*** Test Cases ***
Example
    I execute "ls"
    I execute "ls" with "-lh"
```

Robot Framework должен определить, какой именно keyword соответствует вызову.

---

# Custom Regular Expressions

Для embedded arguments можно задавать собственные regexp.

Синтаксис:

```robot
${argument:regexp}
```

Например:

```robot
*** Keywords ***
I execute "${cmd:[^"]+}"
    Run Process    ${cmd}    shell=True
```

Здесь:

```text
[^"]+
```

означает:

> один или более символов, кроме `"`

Это делает сопоставление более точным.

---

## Ограничение значения числами

Можно разрешить только цифры:

```robot
${num:\d+}
```

Пример:

```robot
*** Keywords ***
I type ${num1:\d+} ${operator:[+-]} ${num2:\d+}
    Calculate    ${num1}    ${operator}    ${num2}
```

Теперь допустимы вызовы:

```robot
I type 1 + 2
I type 53 - 11
```

Где:

```text
${num1}     → число
${operator} → + или -
${num2}     → число
```

---

# Embedded Arguments с датой

Можно задать строгий формат даты:

```robot
*** Keywords ***
Today is ${date:\d{4}-\d{2}-\d{2}}
    Log    ${date}
```

Соответствует формату:

```text
YYYY-MM-DD
```

Например:

```robot
Today is 2011-06-27
```

---

## Variables и Embedded Arguments

Robot Framework также автоматически сопоставляет embedded argument, если при вызове используется variable.

Например:

```robot
*** Variables ***
${DATE}    2011-06-27

*** Test Cases ***
Example
    Today is ${DATE}
```

При этом есть важный нюанс:

> Если используется variable, её фактическое значение может не соответствовать regexp, указанному в embedded argument.

---

# Return Values

User Keywords могут возвращать значения.

Начиная с Robot Framework 5.0 рекомендуемый способ — оператор:

```robot
RETURN
```

Старые способы:

```text
[Return]
Return From Keyword
Return From Keyword If
```

считаются deprecated.

---

# Возврат одного значения

```robot
*** Keywords ***
Return One Value
    [Arguments]    ${arg}
    ${value} =    Convert To Upper Case    ${arg}
    RETURN    ${value}
```

Использование:

```robot
${result} =    Return One Value    hello
```

Получим:

```text
${result} = HELLO
```

После `RETURN` выполнение keyword прекращается.

Например:

```robot
*** Keywords ***
Return One Value
    [Arguments]    ${arg}
    ${value} =    Convert To Upper Case    ${arg}
    RETURN    ${value}
    Fail    Not executed
```

Строка:

```robot
Fail    Not executed
```

никогда не выполнится.

---

# Возврат нескольких значений

Можно вернуть сразу несколько значений:

```robot
*** Keywords ***
Return Three Values
    RETURN    a    b    c
```

Результат можно сохранить:

```robot
${a}    ${b}    ${c} =    Return Three Values
```

---

# Conditional RETURN

`RETURN` можно использовать внутри условий.

```robot
*** Keywords ***
Conditional Return
    [Arguments]    ${arg}
    Log    Before

    IF    ${arg} == 1
        Log    Returning!
        RETURN
    END

    Log    After
```

Если:

```text
${arg} == 1
```

выполнение остановится на:

```robot
RETURN
```

и:

```robot
Log    After
```

не выполнится.

---

# RETURN внутри FOR

`RETURN` можно использовать внутри циклов.

Например, поиск индекса:

```robot
*** Keywords ***
Find Index
    [Arguments]    ${test}    ${items}

    FOR    ${index}    ${item}    IN ENUMERATE    @{items}
        IF    $item == $test    RETURN    ${index}
    END

    RETURN    ${-1}
```

Логика:

```text
проходим элементы
        ↓
нашли нужный
        ↓
RETURN index
```

Если элемент не найден:

```robot
RETURN    ${-1}
```

---

# Keyword Teardown

User Keyword может иметь собственный **teardown**.

Для этого используется:

```robot
[Teardown]
```

Teardown выполняется **после основной части keyword**.

Пример:

```robot
*** Keywords ***
With Teardown
    Do Something
    [Teardown]    Log    keyword teardown
```

Последовательность:

```text
Do Something
      ↓
keyword заканчивается
      ↓
Log    keyword teardown
```

---

## Teardown выполняется даже при ошибке

Важная особенность:

> Keyword teardown вызывается даже тогда, когда основная часть keyword завершилась с ошибкой.

Например:

```robot
*** Keywords ***
Example
    Some Failing Keyword
    [Teardown]    Cleanup
```

Даже если:

```robot
Some Failing Keyword
```

упадёт, Robot Framework всё равно попытается выполнить:

```robot
Cleanup
```

Это делает teardown удобным для:

* закрытия браузера;
* удаления созданных данных;
* освобождения ресурсов;
* возврата системы в исходное состояние.

---

## Ошибки внутри Teardown

Если одна из операций teardown завершилась ошибкой, Robot Framework всё равно старается продолжить остальные teardown-действия.

При этом сам тест будет считаться failed.

---

# Teardown через Variable

Имя teardown keyword можно хранить в переменной:

```robot
*** Keywords ***
Using Variables
    [Documentation]    Teardown given as variable
    Do Something
    [Teardown]    ${TEARDOWN}
```

Например:

```robot
*** Variables ***
${TEARDOWN}    Close Browser
```

Тогда фактически будет выполнен:

```robot
Close Browser
```

---

# User Keyword: полный пример

Пример, объединяющий несколько возможностей:

```robot
*** Keywords ***
Login User
    [Documentation]    Logs user into application
    [Tags]    login
    [Arguments]    ${username}    ${password}=secret

    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Click Button    Login

    RETURN    ${username}

    [Teardown]    Log    Login keyword finished
```

Здесь используются:

* `[Documentation]`;
* `[Tags]`;
* `[Arguments]`;
* positional argument;
* default value;
* `RETURN`;
* `[Teardown]`.

---

# User Keywords — Общая схема

```text
*** Keywords ***
        │
        ├── Keyword Name
        │
        ├── [Documentation]
        ├── [Tags]
        ├── [Arguments]
        ├── [Timeout]
        │
        ├── Keyword Steps
        │
        ├── RETURN
        │
        └── [Teardown]
```

---

# Что важно запомнить

**User Keyword** — переиспользуемая последовательность действий, созданная непосредственно в Robot Framework.

Основные возможности:

* создаются в `*** Keywords ***`;
* могут принимать positional arguments;
* поддерживают default values;
* `@{args}` используется для произвольного количества positional arguments;
* `&{kwargs}` — для произвольных named arguments;
* поддерживаются named-only arguments;
* аргументы можно встраивать прямо в имя keyword;
* для embedded arguments можно использовать regexp;
* значения рекомендуется возвращать через `RETURN`;
* `[Teardown]` выполняет cleanup после keyword;
* teardown запускается даже при ошибке основной части keyword.

## Аналогии с Python

```text
Robot Framework          Python

${arg}                    arg
${arg}=default            arg=default
@{args}                   *args
&{kwargs}                 **kwargs
@{}                       *
RETURN                    return
```

Эти аналогии особенно полезны, потому что механизм аргументов User Keywords во многом повторяет привычную модель функций Python.
