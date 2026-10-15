# union() объединяет элементы обоих множеств без повторов.
left = {1, 2, 3}
right = {3, 4, 5}

print("Объединение — union() и |:")
print(f"Первое множество: {left!r}")
print(f"Второе множество: {right!r}")
print(f"left.union(right) -> {left.union(right)!r}")
print(f"left | right -> {left | right!r}")

# intersection() оставляет элементы, которые есть в обоих множествах.
print("\nПересечение — intersection() и &:")
print(f"Первое множество: {left!r}")
print(f"Второе множество: {right!r}")
print(f"left.intersection(right) -> {left.intersection(right)!r}")
print(f"left & right -> {left & right!r}")

# difference() оставляет элементы первого множества, которых нет во втором.
# Порядок множеств здесь влияет на результат.
print("\nРазность — difference() и -:")
print(f"Первое множество: {left!r}")
print(f"Второе множество: {right!r}")
print(f"left.difference(right) -> {left.difference(right)!r}")
print(f"left - right -> {left - right!r}")
print(f"right - left -> {right - left!r}")

# symmetric_difference() оставляет элементы, которые есть только в одном множестве.
print("\nСимметрическая разность — symmetric_difference() и ^:")
print(f"Первое множество: {left!r}")
print(f"Второе множество: {right!r}")
print(f"left.symmetric_difference(right) -> {left.symmetric_difference(right)!r}")
print(f"left ^ right -> {left ^ right!r}")

print("\nИсходные множества после операций:")
print(f"left -> {left!r}")
print(f"right -> {right!r}")
