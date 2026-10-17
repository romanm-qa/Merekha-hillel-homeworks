# При вызове параметр связывается с переданным объектом.
# Автоматическая копия объекта не создаётся.
# Важно различать изменение объекта и переприсваивание параметра.


# Числа неизменяемы.
# number += 1 связывает локальный параметр с другим числом.
# Переменная снаружи продолжает ссылаться на исходное число.
def increase_number(number):
    number += 1
    return number


number = 10

print("Неизменяемый аргумент:")
print(f"Исходное число: {number!r}")
print(f"increase_number(number) -> {increase_number(number)!r}")
print(f"Число после вызова: {number!r}")


# Список изменяем: append() меняет сам переданный объект.
# Изменения видны через переменную снаружи.
def append_number(numbers, number):
    numbers.append(number)


numbers = [10, 20]

print("\nИзменение переданного списка:")
print(f"Исходный список: {numbers!r}")

result = append_number(numbers, 30)

print(f"Список после вызова: {numbers!r}")
print(f"Результат функции: {result!r}")


# Изменение списка не требует return.
# Функция без явного return возвращает None.


# Присваивание нового списка параметру не меняет исходный список.
# Теперь локальный параметр numbers ссылается на другой объект.
def replace_numbers(numbers):
    numbers = [100, 200]
    return numbers


numbers = [10, 20]

print("\nПереприсваивание параметра:")
print(f"Исходный список: {numbers!r}")

result = replace_numbers(numbers)

print(f"Возвращённый список: {result!r}")
print(f"Исходный список после вызова: {numbers!r}")
print(f"result is numbers -> {result is numbers!r}")


# Для списка += расширяет существующий объект.
def extend_in_place(numbers):
    numbers += [30]
    return numbers


numbers = [10, 20]

print("\nОператор += со списком:")
print(f"Исходный список: {numbers!r}")

result = extend_in_place(numbers)

print(f"Список после вызова: {numbers!r}")
print(f"Возвращённый список: {result!r}")
print(f"result is numbers -> {result is numbers!r}")


# Выражение numbers + [30] создаёт новый список.
# Присваивание меняет только локальную связь параметра.
def extend_with_new_list(numbers):
    numbers = numbers + [30]
    return numbers


numbers = [10, 20]

print("\nОператор + и переприсваивание:")
print(f"Исходный список: {numbers!r}")

result = extend_with_new_list(numbers)

print(f"Возвращённый список: {result!r}")
print(f"Исходный список после вызова: {numbers!r}")
print(f"result is numbers -> {result is numbers!r}")


# Чтобы не менять исходный список, можно сначала скопировать его.
def append_to_copy(numbers, number):
    copied_numbers = numbers.copy()
    copied_numbers.append(number)
    return copied_numbers


numbers = [10, 20]

print("\nИзменение копии:")
print(f"Исходный список: {numbers!r}")

result = append_to_copy(numbers, 30)

print(f"Новый список: {result!r}")
print(f"Исходный список после вызова: {numbers!r}")
print(f"result is numbers -> {result is numbers!r}")


# copy() создаёт поверхностную копию.
# Внешние списки разные, но вложенные объекты остаются общими.
def change_nested_copy(rows):
    copied_rows = rows.copy()
    copied_rows[0].append(99)
    return copied_rows


rows = [[1, 2], [3, 4]]

print("\nПоверхностная копия вложенного списка:")
print(f"Исходный список: {rows!r}")

result = change_nested_copy(rows)

print(f"Возвращённый список: {result!r}")
print(f"Исходный список после вызова: {rows!r}")
print(f"result is rows -> {result is rows!r}")
print(f"result[0] is rows[0] -> {result[0] is rows[0]!r}")


# Словарь тоже можно изменить на месте.
def update_role(user, role):
    user["role"] = role


user = {"name": "Roman", "role": "student"}

print("\nИзменение переданного словаря:")
print(f"Исходный словарь: {user!r}")

update_role(user, "tester")

print(f"Словарь после вызова: {user!r}")


# Неизменяемый контейнер может содержать изменяемый объект.
# Кортеж не меняется, но список внутри него можно изменить.
def append_inside_tuple(data, number):
    data[0].append(number)


data = ([10, 20], "numbers")

print("\nИзменяемый объект внутри кортежа:")
print(f"Исходный кортеж: {data!r}")

append_inside_tuple(data, 30)

print(f"Кортеж после вызова: {data!r}")


# Значения по умолчанию вычисляются при выполнении def,
# а не заново при каждом вызове функции.
# Здесь один список используется всеми вызовами,
# в которых аргумент items не передан.
def add_item_shared(item, items=[]):
    items.append(item)
    return items


print("\nИзменяемое значение по умолчанию:")
print(f"Первый вызов add_item_shared(1) -> {add_item_shared(1)!r}")
print(f"Второй вызов add_item_shared(2) -> {add_item_shared(2)!r}")
print(f"Третий вызов add_item_shared(3) -> {add_item_shared(3)!r}")

# Если передать свой список, используется именно он.
# Список по умолчанию при этом не изменяется.
custom_items = [10]

print("\nЯвная передача списка:")
print(f"Исходный список: {custom_items!r}")
print(
    f"add_item_shared(20, custom_items) -> "
    f"{add_item_shared(20, custom_items)!r}"
)
print(f"Переданный список после вызова: {custom_items!r}")
print(f"add_item_shared(4) -> {add_item_shared(4)!r}")


# Если нужен отдельный список для каждого вызова без items,
# используем None и создаём список внутри функции.
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print("\nНовый список при каждом вызове без items:")
print(f"add_item(1) -> {add_item(1)!r}")
print(f"add_item(2) -> {add_item(2)!r}")
print(f"add_item(3) -> {add_item(3)!r}")

# Проверяем именно is None, а не if not items.
# Переданный пустой список нужно использовать, а не заменять.
items = []

print("\nПередача пустого списка:")
print(f"Исходный список: {items!r}")

result = add_item(10, items)

print(f"Список после вызова: {items!r}")
print(f"Возвращённый список: {result!r}")
print(f"result is items -> {result is items!r}")

# Правило вычисления значений по умолчанию относится
# не только к изменяемым объектам.
language = "Python"


def show_language(value=language):
    return value


language = "Java"

print("\nМомент вычисления значения по умолчанию:")
print(f"Текущее значение language: {language!r}")
print(f"show_language() -> {show_language()!r}")
print(f"show_language(language) -> {show_language(language)!r}")

# Главное:
# изменение объекта может быть видно снаружи;
# переприсваивание параметра не переназначает внешнюю переменную;
# функция не копирует аргументы автоматически;
# значения по умолчанию вычисляются один раз при выполнении def;
# для нового списка в каждом вызове удобно использовать None.
