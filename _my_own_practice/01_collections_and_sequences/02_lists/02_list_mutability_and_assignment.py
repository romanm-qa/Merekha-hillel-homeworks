# Список изменяемый: элемент можно заменить после создания списка.
fruits = ["apple", "banana", "orange"]

print("Изменение списка:")
print(f"Исходный список: {fruits!r}")
fruits[1] = "pear"
print(f"После fruits[1] = 'pear': {fruits!r}")

# del удаляет элемент по индексу или несколько элементов по срезу.
# После каждого удаления оставшиеся элементы сдвигаются.
numbers = [10, 20, 30, 40, 50]

print("\nУдаление элементов — del:")
print(f"Исходный список: {numbers!r}")
del numbers[2]
print(f"После del numbers[2]: {numbers!r}")
del numbers[-1]
print(f"После del numbers[-1]: {numbers!r}")
del numbers[1:3]
print(f"После del numbers[1:3]: {numbers!r}")

# Присваивание не копирует список: обе переменные указывают на один объект.
original_list = [1, 2, 3]
shared_list = original_list

print("\nПрисваивание списка — =:")
print(f"Исходный список: {original_list!r}")
print(f"shared_list is original_list -> {shared_list is original_list!r}")
shared_list.append(4)
print(f"После shared_list.append(4): {shared_list!r}")
print(f"Исходный список после изменения: {original_list!r}")

# copy() создаёт новый список. Изменение его состава не меняет исходный.
# Копия поверхностная: вложенные изменяемые элементы остаются общими.
original_list = [1, 2, 3]
copied_list = original_list.copy()

print("\nКопирование списка — copy():")
print(f"Исходный список: {original_list!r}")
print(f"original_list.copy() -> {copied_list!r}")
print(f"copied_list is original_list -> {copied_list is original_list!r}")
copied_list.append(4)
print(f"После copied_list.append(4): {copied_list!r}")
print(f"Исходный список после изменения копии: {original_list!r}")
