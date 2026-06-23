"""
Пример использования try/except.
Пробуем сложить два значения как числа.
Если преобразование в float невозможно,
объединяем значения как строки.
"""
def concat_or_add(a, b):
    try:
        # Пытаемся преобразовать значения в числа и сложить
        return float(a) + float(b)

    except Exception:
        # Если преобразование не удалось,
        # объединяем значения как строки
        return str(a) + str(b)

print(concat_or_add(2.5, 2))        # 4.5
print(concat_or_add(2.5, "20"))     # 22.5
print(concat_or_add("2.5", "20"))   # 22.5
print(concat_or_add("2.5", "20a"))  # 2.520a


print(f"Строку можно переобразовать -> {float("20")}")  # 20.0