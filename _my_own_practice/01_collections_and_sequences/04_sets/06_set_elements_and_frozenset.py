# Числа, строки и кортежи из хешируемых значений могут быть элементами set.
items = {10, "apple", (1, 2)}

print("Элементы множества:")
print(f"Исходное множество: {items!r}")
print(f"(1, 2) in items -> {(1, 2) in items!r}")

# Список нельзя добавить в множество: он изменяем и не хешируется.
items = {10, 20}

print("\nПопытка добавить список:")
print(f"Исходное множество: {items!r}")
try:
    items.add([1, 2])
except TypeError as error:
    print(f"items.add([1, 2]) -> {type(error).__name__}: {error}")

# frozenset — неизменяемое множество.
numbers = frozenset({1, 2, 3})

print("\nНеизменяемое множество — frozenset:")
print(f"Исходный frozenset: {numbers!r}")
print(f"2 in numbers -> {2 in numbers!r}")

# frozenset можно вложить в обычное множество.
groups = {frozenset({1, 2}), frozenset({3, 4})}

print("\nfrozenset как элемент set:")
print(f"Исходное множество: {groups!r}")
print(f"frozenset({{1, 2}}) in groups -> {frozenset({1, 2}) in groups!r}")
