# Множество изменяемо: add(value) добавляет элемент в существующее множество.
# Если элемент уже есть, множество не меняется.
numbers = {10, 20, 30}

print("Добавление элемента — add():")
print(f"Исходное множество: {numbers!r}")
numbers.add(40)
print(f"После numbers.add(40): {numbers!r}")
numbers.add(20)
print(f"После numbers.add(20): {numbers!r}")

# update(iterable) добавляет элементы из другой коллекции.
numbers = {10, 20, 30}
new_numbers = [30, 40, 50]

print("\nДобавление нескольких элементов — update():")
print(f"Исходное множество: {numbers!r}")
print(f"Добавляемый список: {new_numbers!r}")
numbers.update(new_numbers)
print(f"После numbers.update(new_numbers): {numbers!r}")

# remove(value) удаляет элемент. Если его нет, возникает KeyError.
numbers = {10, 20, 30}

print("\nУдаление элемента — remove():")
print(f"Исходное множество: {numbers!r}")
numbers.remove(20)
print(f"После numbers.remove(20): {numbers!r}")

# discard(value) удаляет элемент, если он есть.
# Если элемента нет, ошибки не возникает.
numbers = {10, 20, 30}

print("\nУдаление без ошибки — discard():")
print(f"Исходное множество: {numbers!r}")
numbers.discard(20)
print(f"После numbers.discard(20): {numbers!r}")
numbers.discard(99)
print(f"После numbers.discard(99): {numbers!r}")

# pop() удаляет и возвращает произвольный элемент.
numbers = {10, 20, 30}

print("\nУдаление произвольного элемента — pop():")
print(f"Исходное множество: {numbers!r}")
removed = numbers.pop()
print(f"Удалённый элемент: {removed!r}")
print(f"После numbers.pop(): {numbers!r}")

# clear() удаляет все элементы.
numbers = {10, 20, 30}

print("\nОчистка множества — clear():")
print(f"Исходное множество: {numbers!r}")
numbers.clear()
print(f"После numbers.clear(): {numbers!r}")
