# ==========================================
# LIST COMPREHENSION
# ==========================================
# List comprehension позволяет создать новый список
# в одну строку вместо использования цикла for.
# Он делает код короче и зачастую более читаемым.

print("=== Создание списка через цикл ===")

odd_numbers = []

for number in range(15):
    if number % 2 == 1:
        odd_numbers.append(number)

print(odd_numbers)

print("\n=== List comprehension ===")

odd_numbers = [number for number in range(15) if number % 2 == 1]

print(odd_numbers)

print("\n=== Только четные числа ===")

even_numbers = [number for number in range(10) if number % 2 == 0]

print(even_numbers)