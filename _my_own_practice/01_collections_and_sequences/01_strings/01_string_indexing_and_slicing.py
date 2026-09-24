# Индексы и срезы строк
# Строка[start:stop:step]: start включается, stop не включается.

letters_and_dot = "abcdefg."

# Символы:     a   b   c   d   e   f   g   .
# Индексы:     0   1   2   3   4   5   6   7
# Отрицат.:   -8  -7  -6  -5  -4  -3  -2  -1

# Один символ по индексу
first_char = letters_and_dot[0]
third_char = letters_and_dot[2]
last_letter = letters_and_dot[6]
last_char = letters_and_dot[-1]

print("\nИндексы:")
print(f"Исходная строка: {letters_and_dot!r}")
print(f"letters_and_dot[0]  -> {first_char!r}")
print(f"letters_and_dot[2]  -> {third_char!r}")
print(f"letters_and_dot[6]  -> {last_letter!r}")
print(f"letters_and_dot[-1] -> {last_char!r}")

# Срезы: граница stop не входит в результат
middle = letters_and_dot[2:5]
first_five = letters_and_dot[:5]
without_edges = letters_and_dot[2:-2]
from_fourth = letters_and_dot[3:]
whole_string = letters_and_dot[:]  # Вся строка; новый объект не гарантирован

print("\nСрезы:")
print(f"Исходная строка: {letters_and_dot!r}")
print(f"letters_and_dot[2:5]  -> {middle!r}")
print(f"letters_and_dot[:5]   -> {first_five!r}")
print(f"letters_and_dot[2:-2] -> {without_edges!r}")
print(f"letters_and_dot[3:]   -> {from_fourth!r}")
print(f"letters_and_dot[:]    -> {whole_string!r}")

# Шаг и границы
every_second = letters_and_dot[::2]
reversed_string = letters_and_dot[::-1]
beyond_length = letters_and_dot[:100]  # Срез допускает выход за длину строки

print("\nШаг и границы:")
print(f"Исходная строка: {letters_and_dot!r}")
print(f"letters_and_dot[::2]  -> {every_second!r}")
print(f"letters_and_dot[::-1] -> {reversed_string!r}")
print(f"letters_and_dot[:100] -> {beyond_length!r}")

# Строку нельзя изменить по индексу
print("\nНеизменяемость:")
print(f"Исходная строка: {letters_and_dot!r}")

try:
    letters_and_dot[0] = "A"
except TypeError as error:
    print(f"letters_and_dot[0] = 'A' -> {type(error).__name__}: {error}")

# Чтобы получить другую строку, создаём её из частей исходной
changed_string = "A" + letters_and_dot[1:]
print(f"Новая строка: {changed_string!r}")
print(f"Исходная строка: {letters_and_dot!r}")
