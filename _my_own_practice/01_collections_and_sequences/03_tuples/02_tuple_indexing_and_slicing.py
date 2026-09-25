# Кортеж — последовательность: к его элементам можно обращаться по индексу.
fruits = ("apple", "banana", "orange", "kiwi")

print("Доступ по индексу:")
print(f"Исходный кортеж: {fruits!r}")
print(f"fruits[0] -> {fruits[0]!r}")
print(f"fruits[1] -> {fruits[1]!r}")
print(f"fruits[3] -> {fruits[3]!r}")

# Отрицательные индексы отсчитываются с конца: -1 — последний элемент.
print("\nОтрицательные индексы:")
print(f"Исходный кортеж: {fruits!r}")
print(f"fruits[-1] -> {fruits[-1]!r}")
print(f"fruits[-2] -> {fruits[-2]!r}")

# Срез [start:stop] включает start, но не включает stop.
numbers = (10, 20, 30, 40, 50, 60)

print("\nСрезы:")
print(f"Исходный кортеж: {numbers!r}")
print(f"numbers[1:4] -> {numbers[1:4]!r}")
print(f"numbers[:3] -> {numbers[:3]!r}")
print(f"numbers[2:] -> {numbers[2:]!r}")

# Третье значение в срезе — шаг: [start:stop:step].
print("\nСрезы с шагом:")
print(f"Исходный кортеж: {numbers!r}")
print(f"numbers[::2] -> {numbers[::2]!r}")
print(f"numbers[1::2] -> {numbers[1::2]!r}")

# Отрицательный шаг идёт справа налево.
print("\nСрезы с отрицательным шагом:")
print(f"Исходный кортеж: {numbers!r}")
print(f"numbers[::-1] -> {numbers[::-1]!r}")
print(f"numbers[4:1:-1] -> {numbers[4:1:-1]!r}")

# Чтобы добраться до числа во вложенном кортеже, нужны два индекса.
coordinates = ((8, 3), (2, 8), (3, 4))

print("\nВложенные кортежи:")
print(f"Исходный кортеж: {coordinates!r}")
print(f"coordinates[0] -> {coordinates[0]!r}")
print(f"coordinates[0][1] -> {coordinates[0][1]!r}")
