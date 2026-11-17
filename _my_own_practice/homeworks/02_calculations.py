# 3, 6, 15, 18 — перевод температуры, деление и остаток, банковский вклад, расстояние между точками

# ==========================================
# Задача 3. Перевод температуры
# ==========================================
# Функция принимает:
# temperature — значение температуры;
# scale — исходную шкалу: "C" или "F".
#
# Если scale == "C", перевести Цельсии в Фаренгейты.
# Если scale == "F", перевести Фаренгейты в Цельсии.
# Вернуть полученную температуру.
#
# Формулы:
# F = C * 9 / 5 + 32
# C = (F - 32) * 5 / 9

def convert_temperature(temperature, scale):
    if scale == "C":
        return temperature * 9 / 5 + 32
    elif scale == "F":
        return (temperature - 32) * 5 / 9
    else:
        raise ValueError('Шкала должна быть "C" или "F"')


print("=" * 50)
print("Задача 3. Перевод температуры")
print("=" * 50)

print(f"Температура: 0 °C → °F: {convert_temperature(0, 'C')!r}")
print(f"Температура: 100 °C → °F: {convert_temperature(100, 'C')!r}")
print(f"Температура: 32 °F → °C: {convert_temperature(32, 'F')!r}")
print(f"Температура: 212 °F → °C: {convert_temperature(212, 'F')!r}")
print()


# ==========================================
# Практика. Перевод расстояния
# ==========================================
# Функция принимает:
# distance — значение расстояния;
# unit — исходную единицу: "km" или "mi".
#
# Если unit == "km", перевести километры в мили.
# Если unit == "mi", перевести мили в километры.
# Вернуть полученное расстояние.
#
# Использовать соотношение: 1 миля = 1.609344 км.

def convert_distance(distance, unit):
    if unit == "mi":
        return distance * 1.609344
    elif unit == "km":
        return distance / 1.609344
    else:
        raise ValueError('Единица должна быть "km" или "mi"')


print("=" * 50)
print("Практика. Перевод расстояния")
print("=" * 50)

print(f"Расстояние: 10 km → mi: {convert_distance(10, 'km')!r}")
print(f"Расстояние: 5 mi → km: {convert_distance(5, 'mi')!r}")
print(f"Расстояние: 0 km → mi: {convert_distance(0, 'km')!r}")
print(f"Расстояние: 1 mi → km: {convert_distance(1, 'mi')!r}")
print()
