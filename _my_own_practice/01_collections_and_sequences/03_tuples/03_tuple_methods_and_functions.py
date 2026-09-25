# count() возвращает количество вхождений значения.
numbers = (10, 20, 10, 30, 10, 40)

print("Метод count():")
print(f"Исходный кортеж: {numbers!r}")
print(f"numbers.count(10) -> {numbers.count(10)!r}")
print(f"numbers.count(50) -> {numbers.count(50)!r}")

# index() возвращает индекс первого найденного значения.
# Если значения нет, возникает ValueError.
print("\nМетод index():")
print(f"Исходный кортеж: {numbers!r}")
print(f"numbers.index(10) -> {numbers.index(10)!r}")
print(f"numbers.index(30) -> {numbers.index(30)!r}")

# Поиск можно ограничить индексами start и stop; stop не включается.
print("\nПоиск в части кортежа:")
print(f"Исходный кортеж: {numbers!r}")
print(f"numbers.index(10, 1) -> {numbers.index(10, 1)!r}")
print(f"numbers.index(10, 3, 5) -> {numbers.index(10, 3, 5)!r}")

# Встроенные функции вызываются отдельно, а не через точку после кортежа.
values = (4, 8, 2, 6)

print("\nВстроенные функции:")
print(f"Исходный кортеж: {values!r}")
print(f"len(values) -> {len(values)!r}")
print(f"min(values) -> {min(values)!r}")
print(f"max(values) -> {max(values)!r}")
print(f"sum(values) -> {sum(values)!r}")

# sorted() возвращает новый список, исходный кортеж остаётся прежним.
print("\nСортировка:")
print(f"Исходный кортеж: {values!r}")
print(f"sorted(values) -> {sorted(values)!r}")
print(f"Кортеж после sorted(): {values!r}")
