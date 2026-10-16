# Сложный пример с for, continue, in и вложенным циклом.
# Задача:
# 1. Убрать точки из строки.
# 2. Убрать повторяющиеся символы.
# 3. Посчитать сумму оставшихся цифр.

some_string = "1.545.12.8"

result_str = ""

for char in some_string:
    # Пропускаем точки и символы, которые уже есть в result_str
    if char == "." or char in result_str:
        continue

    result_str += char

else:
    total = 0

    for elem in result_str:
        total += int(elem)

print("result_str =", result_str)
print("total =", total)