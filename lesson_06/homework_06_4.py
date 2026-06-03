# Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі
# Якщо список не надано:
# list_value = list(range(10))

list_value = list(range(10))
even_sum = 0

for value in list_value:
    if value % 2 == 0:
        even_sum += value

print(f"Sum of even numbers: {even_sum}")