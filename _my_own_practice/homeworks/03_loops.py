# 7 8, 10, 11, 13, 19, 20, 26 — суммы, диапазоны, произведение, факториал, таблица умножения, последовательность Сиракуз

# ==========================================
# Практика. Сумма чисел с выбором чётности
# ==========================================
# Функция принимает два аргумента:
# stop — конец диапазона от 0 до stop, не включая stop;
# type_ — режим: "even" для чётных, "odd" для нечётных.
# Вернуть сумму чисел выбранной чётности.
# Для неизвестного режима вызвать ValueError.

def count_sum(stop, type_):
    total = 0

    if type_ == "even":
        for value in range(stop):
            if value % 2 == 0:
                total += value
    elif type_ == "odd":
        for value in range(stop):
            if value % 2 == 1:
                total += value
    else:
        raise ValueError('Режим должен быть "even" или "odd"')

    return total


print("=" * 50)
print("Практика. Сумма чисел с выбором чётности")
print("=" * 50)

# Позиционные аргументы
print(f"Диапазон: range(7), режим: 'even' → сумма: {count_sum(7, 'even')!r}")
print(f"Диапазон: range(7), режим: 'odd' → сумма: {count_sum(7, 'odd')!r}")

# Именованные аргументы
print(f"Диапазон: range(10), режим: 'even' → сумма: {count_sum(stop=10, type_='even')!r}")
print(f"Диапазон: range(10), режим: 'odd' → сумма: {count_sum(stop=10, type_='odd')!r}")
print()
