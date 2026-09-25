# index(value) возвращает индекс первого совпадения.
# Если значения нет в списке, возникает ValueError.
fruits = ["apple", "banana", "orange", "banana"]

print("Поиск позиции — index():")
print(f"Исходный список: {fruits!r}")
print(f"fruits.index('banana') -> {fruits.index('banana')!r}")
print(f"fruits.index('orange') -> {fruits.index('orange')!r}")

# index(value, start, stop) ищет только в указанной части списка.
# start включается, stop не включается. Возвращается индекс в исходном списке.
print("\nПоиск с ограничением — index(value, start, stop):")
print(f"Исходный список: {fruits!r}")
print(f"fruits.index('banana', 2) -> {fruits.index('banana', 2)!r}")
print(f"fruits.index('orange', 1, 3) -> {fruits.index('orange', 1, 3)!r}")

# count(value) возвращает число совпадений; если их нет, возвращает 0.
numbers = [10, 20, 30, 20, 40, 20]

print("\nПодсчёт совпадений — count():")
print(f"Исходный список: {numbers!r}")
print(f"numbers.count(20) -> {numbers.count(20)!r}")
print(f"numbers.count(10) -> {numbers.count(10)!r}")
print(f"numbers.count(50) -> {numbers.count(50)!r}")

# in проверяет наличие значения и возвращает True или False.
# Для проверки отсутствия значения используется not in.
fruits = ["apple", "banana", "orange"]

print("\nПроверка наличия — in и not in:")
print(f"Исходный список: {fruits!r}")
print(f"'banana' in fruits -> {'banana' in fruits!r}")
print(f"'kiwi' in fruits -> {'kiwi' in fruits!r}")
print(f"'kiwi' not in fruits -> {'kiwi' not in fruits!r}")

# Встроенные функции вызываются отдельно, а не через точку после списка.
numbers = [10, 20, 30, 20, 40, 20]

print("\nВстроенные функции:")
print(f"Исходный список: {numbers!r}")
print(f"len(numbers) -> {len(numbers)!r}")
print(f"min(numbers) -> {min(numbers)!r}")
print(f"max(numbers) -> {max(numbers)!r}")
print(f"sum(numbers) -> {sum(numbers)!r}")
