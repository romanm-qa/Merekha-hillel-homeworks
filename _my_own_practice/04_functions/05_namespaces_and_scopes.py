# Пространство имён связывает имена с объектами.
# Область видимости определяет, где эти имена доступны.
# Глобальные имена находятся на уровне модуля — вне функций.
course_name = "Python"


def show_course():
    return course_name


print("Чтение глобальной переменной:")
print(f"Глобальное значение course_name: {course_name!r}")
print(f"show_course() -> {show_course()!r}")


# Параметры и переменные внутри функции являются локальными.
# Каждый вызов получает свои локальные значения.
def create_message(name):
    message = f"Hello, {name}!"
    return message


print("\nЛокальные переменные:")
print(f"create_message('Roman') -> {create_message('Roman')!r}")
print(f"create_message('Alex') -> {create_message('Alex')!r}")

# Локальное имя message не становится доступным снаружи.
try:
    print(message)
except NameError as error:
    print(f"Обращение к message снаружи -> {type(error).__name__}: {error}")

# Локальное присваивание не меняет одноимённую глобальную переменную.
language = "Python"


def show_local_language():
    language = "Java"
    return language


print("\nОдинаковые имена в разных областях:")
print(f"Глобальное значение до вызова: {language!r}")
print(f"show_local_language() -> {show_local_language()!r}")
print(f"Глобальное значение после вызова: {language!r}")

# Для обычного поиска имён внутри функций действует LEGB:
# Local — текущая функция.
# Enclosing — внешние функции, от ближайшей к более дальней.
# Global — текущий модуль.
# Built-in — встроенные имена Python.
scope_name = "Global"


def show_local_scope():
    scope_name = "Enclosing"

    def inner():
        scope_name = "Local"
        return scope_name

    return inner()


print("\nLEGB: найдено локальное имя:")
print(f"Глобальное значение scope_name: {scope_name!r}")
print(f"show_local_scope() -> {show_local_scope()!r}")


# Если локального имени нет, используется имя из внешней функции.
def show_enclosing_scope():
    scope_name = "Enclosing"

    def inner():
        return scope_name

    return inner()


print("\nLEGB: имя из внешней функции:")
print(f"Глобальное значение scope_name: {scope_name!r}")
print(f"show_enclosing_scope() -> {show_enclosing_scope()!r}")


# Если имени нет и во внешних функциях, проверяется модуль.
def show_global_scope():
    def inner():
        return scope_name

    return inner()


print("\nLEGB: глобальное имя:")
print(f"Глобальное значение scope_name: {scope_name!r}")
print(f"show_global_scope() -> {show_global_scope()!r}")


# Если имя не перекрыто, доступны встроенные объекты.
def get_length(text):
    return len(text)


text = "Python"

print("\nLEGB: встроенное имя:")
print(f"Исходная строка: {text!r}")
print(f"get_length(text) -> {get_length(text)!r}")


# Если имя нигде не найдено, возникает NameError.
def read_missing_name():
    return missing_value


print("\nНеизвестное имя:")

try:
    read_missing_name()
except NameError as error:
    print(f"read_missing_name() -> {type(error).__name__}: {error}")

# Присваивание внутри функции делает имя локальным,
# если оно не объявлено через global или nonlocal.
# Даже строка ДО присваивания обращается к локальному имени.
counter = 10


def increase_without_global():
    counter += 1
    return counter


print("\nЧтение локального имени до присваивания:")
print(f"Глобальное значение counter: {counter!r}")

try:
    increase_without_global()
except UnboundLocalError as error:
    print(
        f"increase_without_global() -> "
        f"{type(error).__name__}: {error}"
    )

print(f"Глобальное значение после вызова: {counter!r}")


# counter += 1 сначала требует прочитать counter.
# Локальное значение ещё не задано, поэтому возникает ошибка.
# Python не продолжает поиск в глобальной области.
# UnboundLocalError является подклассом NameError.


# global позволяет переприсвоить имя в области текущего модуля.
def increase_global_counter():
    global counter
    counter += 1
    return counter


print("\nИзменение глобальной переменной:")
print(f"Значение counter до вызова: {counter!r}")
print(f"increase_global_counter() -> {increase_global_counter()!r}")
print(f"Значение counter после вызова: {counter!r}")

# Для изменения самого объекта global не требуется.
# Здесь имя shared_numbers не переприсваивается.
shared_numbers = [10, 20]


def append_global_number(number):
    shared_numbers.append(number)


print("\nИзменение глобального списка без global:")
print(f"Исходный список: {shared_numbers!r}")

append_global_number(30)

print(f"Список после вызова: {shared_numbers!r}")


# nonlocal позволяет переприсвоить имя из внешней функции.
# Используется ближайшая внешняя функция, где это имя связано.
# Глобальная область для nonlocal не подходит.
def change_enclosing_message():
    message = "Outer"

    def inner():
        nonlocal message
        message = "Changed"

    inner()
    return message


print("\nИзменение имени внешней функции:")
print(f"change_enclosing_message() -> {change_enclosing_message()!r}")


# Без nonlocal присваивание создаёт отдельное локальное имя.
def keep_enclosing_message():
    message = "Outer"

    def inner():
        message = "Inner"
        return message

    inner_message = inner()
    return message, inner_message


print("\nПрисваивание без nonlocal:")
print(
    f"keep_enclosing_message() -> "
    f"{keep_enclosing_message()!r}"
)


# Для изменения объекта внешней функции nonlocal не требуется,
# если само имя не переприсваивается.
def change_enclosing_list():
    numbers = [10, 20]

    def inner():
        numbers.append(30)

    inner()
    return numbers


print("\nИзменение списка внешней функции:")
print(f"change_enclosing_list() -> {change_enclosing_list()!r}")

# if и обычный for не создают отдельную область видимости.
# Имена, присвоенные в их блоках, остаются в текущей области.
print("\nИмена после if и for:")

if True:
    status = "ready"

for last_number in [10, 20, 30]:
    pass

print(f"status после if: {status!r}")
print(f"last_number после for: {last_number!r}")

# Если блок не выполнялся, новое имя в нём не создастся.


# Глобальные имена читаются во время вызова функции.
# Поэтому функция увидит актуальное значение.
current_language = "Python"


def read_current_language():
    return current_language


print("\nЧтение актуального глобального значения:")
print(f"current_language: {current_language!r}")
print(f"read_current_language() -> {read_current_language()!r}")

current_language = "Java"

print(f"current_language после изменения: {current_language!r}")
print(f"read_current_language() -> {read_current_language()!r}")

# globals() возвращает словарь глобального пространства имён.
# Показываем только нужное имя, а не весь служебный вывод.
print("\nПросмотр глобального пространства имён:")
print(f"globals()['course_name'] -> {globals()['course_name']!r}")


# Внутри функции locals() позволяет посмотреть локальные имена.
def inspect_local_names(name):
    greeting = f"Hello, {name}!"
    return locals()


print("\nПросмотр локального пространства имён:")
print(f"inspect_local_names('Roman') -> {inspect_local_names('Roman')!r}")


# Здесь используем locals() только для просмотра.
# Не используем изменение этого словаря для присваивания переменных.


# Локальное имя может перекрыть встроенную функцию.
# После выхода из функции внешнее встроенное имя остаётся доступным.
def shadow_builtin():
    len = 10

    try:
        return len("Python")
    except TypeError as error:
        return f"{type(error).__name__}: {error}"


print("\nПерекрытие встроенного имени:")
print(f"shadow_builtin() -> {shadow_builtin()!r}")
print(f"len('Python') снаружи -> {len('Python')!r}")


# Вместо изменения глобального счётчика обычно удобнее
# явно принять текущее значение и вернуть новое.
def increase_counter(current_counter):
    return current_counter + 1


counter = 10

print("\nПередача значения через параметр:")
print(f"Исходное значение counter: {counter!r}")

counter = increase_counter(counter)

print(f"Значение после присваивания результата: {counter!r}")

# Главное:
# чтение внешнего имени обычно не требует global или nonlocal;
# присваивание имени и изменение объекта — разные операции;
# global относится к модулю, nonlocal — к внешним функциям;
# локальные имена одного вызова не заменяют имена другого вызова.
