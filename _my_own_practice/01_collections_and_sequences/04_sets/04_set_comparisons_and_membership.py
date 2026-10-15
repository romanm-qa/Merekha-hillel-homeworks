# in и not in проверяют наличие отдельного элемента.
numbers = {10, 20, 30}

print("Проверка элемента — in и not in:")
print(f"Исходное множество: {numbers!r}")
print(f"20 in numbers -> {20 in numbers!r}")
print(f"40 in numbers -> {40 in numbers!r}")
print(f"40 not in numbers -> {40 not in numbers!r}")

# Множества равны, если содержат одинаковые элементы.
# Порядок записи и повторы на равенство не влияют.
first = {1, 2, 3}
second = {3, 2, 1, 1}

print("\nРавенство множеств — ==:")
print(f"Первое множество: {first!r}")
print(f"Второе множество: {second!r}")
print(f"first == second -> {first == second!r}")

# Подмножество: все элементы small входят в large.
small = {1, 2}
large = {1, 2, 3}

print("\nПодмножество — issubset() и <=:")
print(f"Меньшее множество: {small!r}")
print(f"Большее множество: {large!r}")
print(f"small.issubset(large) -> {small.issubset(large)!r}")
print(f"small <= large -> {small <= large!r}")
print(f"large <= small -> {large <= small!r}")

# Надмножество: large содержит все элементы small.
print("\nНадмножество — issuperset() и >=:")
print(f"Большее множество: {large!r}")
print(f"Меньшее множество: {small!r}")
print(f"large.issuperset(small) -> {large.issuperset(small)!r}")
print(f"large >= small -> {large >= small!r}")

# Строгие сравнения < и > требуют, чтобы множества различались.
print("\nСтрогое подмножество и надмножество:")
print(f"Меньшее множество: {small!r}")
print(f"Большее множество: {large!r}")
print(f"small < large -> {small < large!r}")
print(f"large > small -> {large > small!r}")
print(f"small < small -> {small < small!r}")

# isdisjoint() проверяет, что у множеств нет общих элементов.
evens = {2, 4, 6}
odds = {1, 3, 5}

print("\nОтсутствие общих элементов — isdisjoint():")
print(f"Первое множество: {evens!r}")
print(f"Второе множество: {odds!r}")
print(f"evens.isdisjoint(odds) -> {evens.isdisjoint(odds)!r}")
