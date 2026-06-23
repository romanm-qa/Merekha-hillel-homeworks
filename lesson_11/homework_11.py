# Есть список строк:
# ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
# Нужно:
# 1. Для каждой строки посчитать сумму чисел.
# 2. Если в строке есть нечисловые символы — поймать ошибку.
# 3. В случае ошибки вывести: "Не можу це зробити!"
#
# Ожидаемый вывод:
# 10
# 60
# Не можу це зробити!

numbers_strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def calculate_sum(numbers_string):
    numbers_list = numbers_string.split(",")

    total = 0

    for number in numbers_list:
        total += int(number)

    return total

for item in numbers_strings:
    try:
        print(calculate_sum(item))
    except ValueError:
        print("Не можу це зробити!")