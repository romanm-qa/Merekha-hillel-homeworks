# Методы изменения списка работают с самим списком и возвращают None.
# append() добавляет переданный объект в конец как один элемент.
numbers = [1, 3, 5]

print("Добавление одного элемента — append():")
print(f"Исходный список: {numbers!r}")
numbers.append(range(5))
print(f"После numbers.append(range(5)): {numbers!r}")
print(f"Последний элемент: {numbers[-1]!r}")

# extend() добавляет в конец элементы итерируемого объекта по отдельности.
numbers = [1, 3, 5]

print("\nДобавление нескольких элементов — extend():")
print(f"Исходный список: {numbers!r}")
numbers.extend(range(5))
print(f"После numbers.extend(range(5)): {numbers!r}")

# Список в append() становится одним вложенным элементом.
# extend() добавляет содержимое переданного списка по отдельности.
append_numbers = [1, 2]
extend_numbers = [1, 2]

print("\nСравнение append() и extend():")
print(f"Исходные списки: {append_numbers!r}")
append_numbers.append([3, 4])
extend_numbers.extend([3, 4])
print(f"append_numbers.append([3, 4]) -> {append_numbers!r}")
print(f"extend_numbers.extend([3, 4]) -> {extend_numbers!r}")

# insert(index, value) вставляет значение перед указанным индексом.
# Элементы справа сдвигаются на одну позицию.
numbers = [1, 3, 5]

print("\nВставка по индексу — insert():")
print(f"Исходный список: {numbers!r}")
numbers.insert(1, 8)
print(f"После numbers.insert(1, 8): {numbers!r}")

# remove(value) удаляет первое вхождение значения, а не элемент по индексу.
# Если значения нет в списке, возникнет ValueError.
numbers = [1, 8, 3, 5, 3]

print("\nУдаление по значению — remove():")
print(f"Исходный список: {numbers!r}")
numbers.remove(3)
print(f"После numbers.remove(3): {numbers!r}")

# pop() удаляет последний элемент и возвращает его.
numbers = [10, 20, 30, 40]

print("\nУдаление с возвратом значения — pop():")
print(f"Исходный список: {numbers!r}")
deleted_item = numbers.pop()
print(f"numbers.pop() -> {deleted_item!r}")
print(f"Список после pop(): {numbers!r}")

# pop(index) удаляет и возвращает элемент по индексу.
# Несуществующий индекс вызывает IndexError; pop() у пустого списка — тоже.
numbers = [10, 20, 30, 40]

print("\nУдаление по индексу — pop(index):")
print(f"Исходный список: {numbers!r}")
deleted_item = numbers.pop(1)
print(f"numbers.pop(1) -> {deleted_item!r}")
print(f"Список после pop(1): {numbers!r}")

# clear() удаляет все элементы самого списка.
numbers = [10, 20, 30, 40]

print("\nОчистка списка — clear():")
print(f"Исходный список: {numbers!r}")
numbers.clear()
print(f"После numbers.clear(): {numbers!r}")
