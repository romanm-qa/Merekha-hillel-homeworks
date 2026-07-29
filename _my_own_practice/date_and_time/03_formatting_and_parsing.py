from datetime import datetime

# ============================================================
# 1. STRFTIME() — ПРЕОБРАЗОВАНИЕ DATETIME В СТРОКУ
# ============================================================

# strftime() создаёт строку из объекта date, time или datetime
# по указанному шаблону.
#
# Название можно запомнить так:
# strftime = string format time
#
# datetime object → strftime() → string

event_datetime = datetime(2026, 7, 28, 19, 15, 30)

formatted_datetime = event_datetime.strftime("%d.%m.%Y %H:%M:%S")

print("Исходный объект datetime:")
print(event_datetime)

print("\nДата и время в виде строки:")
print(formatted_datetime)

print("\nТипы значений:")
print(f"Тип event_datetime: {type(event_datetime)}")
print(f"Тип formatted_datetime: {type(formatted_datetime)}")

# Основные обозначения формата:
#
# %Y — год из четырёх цифр: 2026
# %m — номер месяца: 07
# %d — день месяца: 28
# %H — часы в 24-часовом формате: 19
# %M — минуты: 15
# %S — секунды: 30

# ============================================================
# 2. STRPTIME() — ПРЕОБРАЗОВАНИЕ СТРОКИ В DATETIME
# ============================================================

# strptime() преобразует строку в объект datetime
# согласно указанному шаблону.
#
# Название можно запомнить так:
# strptime = string parse time
#
# string → strptime() → datetime object

datetime_string = "28.07.2026 19:15:30"
datetime_format = "%d.%m.%Y %H:%M:%S"

parsed_datetime = datetime.strptime(
    datetime_string,
    datetime_format,
)

print("\nИсходная строка:")
print(datetime_string)

print("\nОбъект datetime, созданный из строки:")
print(parsed_datetime)

print("\nТипы значений после преобразования:")
print(f"Тип datetime_string: {type(datetime_string)}")
print(f"Тип parsed_datetime: {type(parsed_datetime)}")

# ============================================================
# 3. VALUEERROR — ОБРАБОТКА НЕПРАВИЛЬНОГО ФОРМАТА
# ============================================================

# Если строка не соответствует шаблону или содержит невозможную дату,
# strptime() выбрасывает исключение ValueError.

invalid_datetime_string = "28/07/2026 19:15:30"
expected_format = "%d.%m.%Y %H:%M:%S"

try:
    parsed_invalid_datetime = datetime.strptime(
        invalid_datetime_string,
        expected_format,
    )
    print(parsed_invalid_datetime)

except ValueError as error:
    print("\nНе удалось преобразовать строку в datetime:")
    print(error)

# ============================================================
# 4. ISOFORMAT() И FROMISOFORMAT() — ISO 8601
# ============================================================

# ISO 8601 — распространённый стандарт записи даты и времени.
# Такой формат часто используется в API, JSON и базах данных.
#
# datetime → isoformat() → строка
# строка → fromisoformat() → datetime

api_datetime = datetime(2026, 7, 28, 19, 15, 30)

iso_datetime_string = api_datetime.isoformat()

print("\nДата и время в ISO-формате:")
print(iso_datetime_string)
print(f"Тип значения: {type(iso_datetime_string)}")

restored_datetime = datetime.fromisoformat(iso_datetime_string)

print("\nОбъект datetime, восстановленный из ISO-строки:")
print(restored_datetime)
print(f"Тип значения: {type(restored_datetime)}")
