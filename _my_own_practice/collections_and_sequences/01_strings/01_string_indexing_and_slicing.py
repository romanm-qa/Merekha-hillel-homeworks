# =====================================================
# СРЕЗЫ (SLICES)
# Синтаксис:
# строка[start:stop:step]
# =====================================================

some_str = "abcdefg."

# Индексы:
#
#   a   b   c   d   e   f   g   .
#   0   1   2   3   4   5   6   7

print(some_str)

print("-" * 30)

# Получить один символ по индексу
print(some_str[0])  # a
print(some_str[2])  # c
print(some_str[6])  # g

print("-" * 30)

# start включается
# stop НЕ включается
print(some_str[2:5])  # cde
print(some_str[:5])  # abcde
print(some_str[2:-2])  # cdef
print(some_str[3:])  # defg.

print("-" * 30)

# Копия строки
copy_str = some_str[:]
print(copy_str)

print("-" * 30)

# Каждый второй символ
print(some_str[::2])  # aceg

print("-" * 30)

# Получить символ по индексу можно
print(some_str[0])  # a

# Но изменить символ нельзя, потому что строки неизменяемые (immutable)
try:
    some_str[0] = "A"
except TypeError as error:
    print(f"Ошибка Python: {error}")
    print("Объяснение: строки (str) являются неизменяемым типом данных (immutable), поэтому изменить символ по индексу нельзя.")

print("-" * 30)

# Правильный способ "изменить" строку — создать новую
new_str = "A" + some_str[1:]

print(new_str)   # Abcdefg.
print(some_str)  # abcdefg.
