# sort() сортирует сам список и возвращает None.
# По умолчанию числа располагаются по возрастанию.
numbers = [5, 2, 8, 1, 3]

print("Сортировка исходного списка — sort():")
print(f"Исходный список: {numbers!r}")
sort_result = numbers.sort()
print(f"После numbers.sort(): {numbers!r}")
print(f"Возвращаемое значение sort(): {sort_result!r}")

# reverse=True сортирует по убыванию; сам список тоже меняется.
descending_numbers = [5, 2, 8, 1, 3]

print("\nСортировка по убыванию — sort(reverse=True):")
print(f"Исходный список: {descending_numbers!r}")
descending_numbers.sort(reverse=True)
print(f"После descending_numbers.sort(reverse=True): {descending_numbers!r}")

# sorted() создаёт новый отсортированный список и не меняет исходный.
# Можно передать reverse=True для сортировки по убыванию.
original_numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(original_numbers)

print("\nСоздание отсортированного списка — sorted():")
print(f"Исходный список: {original_numbers!r}")
print(f"sorted(original_numbers) -> {sorted_numbers!r}")
print(f"Исходный список после sorted(): {original_numbers!r}")
print(f"sorted(original_numbers, reverse=True) -> {sorted(original_numbers, reverse=True)!r}")

# key задаёт правило сравнения элементов. Здесь строки сравниваются по длине.
words = ["banana", "kiwi", "apple"]

print("\nСортировка по правилу — key:")
print(f"Исходный список: {words!r}")
print(f"sorted(words, key=len) -> {sorted(words, key=len)!r}")
print(f"Исходный список после sorted(): {words!r}")

# reverse() меняет порядок элементов самого списка и возвращает None.
# Это разворот текущего порядка, а не сортировка по убыванию.
numbers_to_reverse = [10, 30, 20, 40]

print("\nРазворот исходного списка — reverse():")
print(f"Исходный список: {numbers_to_reverse!r}")
reverse_result = numbers_to_reverse.reverse()
print(f"После numbers_to_reverse.reverse(): {numbers_to_reverse!r}")
print(f"Возвращаемое значение reverse(): {reverse_result!r}")

# reversed() не меняет исходный список и возвращает итератор.
# list() собирает элементы итератора в новый список для вывода.
original_list = [10, 20, 30, 40]
reversed_list = list(reversed(original_list))

print("\nНовый список в обратном порядке — reversed():")
print(f"Исходный список: {original_list!r}")
print(f"list(reversed(original_list)) -> {reversed_list!r}")
print(f"Исходный список после reversed(): {original_list!r}")

# Срез [::-1] тоже создаёт новый список с обратным порядком элементов.
source_list = [10, 20, 30, 40]
sliced_list = source_list[::-1]

print("\nРазворот через срез [::-1]:")
print(f"Исходный список: {source_list!r}")
print(f"source_list[::-1] -> {sliced_list!r}")
print(f"Исходный список после среза: {source_list!r}")
