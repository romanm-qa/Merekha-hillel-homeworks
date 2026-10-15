# Множество хранит только уникальные элементы.
# Порядок элементов не гарантирован.
numbers = {10, 20, 30, 20, 10}

print("Создание множества:")
print(f"Исходное множество: {numbers!r}")
print(f"len(numbers) -> {len(numbers)!r}")

# sorted() возвращает отсортированный список.
# Исходное множество не меняется.
numbers = {30, 10, 20}

print("\nСортировка элементов — sorted():")
print(f"Исходное множество: {numbers!r}")
print(f"sorted(numbers) -> {sorted(numbers)!r}")
print(f"sorted(numbers, reverse=True) -> {sorted(numbers, reverse=True)!r}")
print(f"Множество после сортировки: {numbers!r}")

# set() создаёт множество из итерируемого объекта и убирает повторы.
fruits = ["apple", "banana", "apple", "orange"]

print("\nСоздание множества из списка — set():")
print(f"Исходный список: {fruits!r}")
print(f"set(fruits) -> {set(fruits)!r}")

# Пустое множество создаётся через set().
# Пустые фигурные скобки {} создают словарь.
empty_set = set()
empty_braces = {}

print("\nПустое множество:")
print(f"Исходное множество: {empty_set!r}")
print(f"type(empty_set) -> {type(empty_set)!r}")
print(f"{{}} -> {empty_braces!r}")
print(f"type(empty_braces) -> {type(empty_braces)!r}")
