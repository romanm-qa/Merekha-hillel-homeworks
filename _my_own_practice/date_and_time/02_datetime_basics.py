from datetime import date, datetime, time

# ============================================================
# 1. DATE, TIME И DATETIME — ОСНОВНЫЕ КЛАССЫ
# ============================================================

# Модуль datetime содержит несколько классов для работы
# с разными представлениями даты и времени:
#
# date     — только дата: год, месяц и день;
# time     — только время: часы, минуты, секунды;
# datetime — дата и время вместе.

lesson_date = date(2026, 7, 28)
lesson_time = time(19, 15, 0)
lesson_datetime = datetime(2026, 7, 28, 19, 15, 0)

print("Только дата:")
print(lesson_date)

print("\nТолько время:")
print(lesson_time)

print("\nДата и время вместе:")
print(lesson_datetime)

# ============================================================
# 2. ПОЛУЧЕНИЕ ТЕКУЩЕЙ ДАТЫ И ВРЕМЕНИ
# ============================================================

# date.today() возвращает текущую локальную дату
# без информации о времени.
current_date = date.today()

# datetime.now() возвращает текущие локальные
# дату и время компьютера.
current_datetime = datetime.now()

print("\nТекущая дата:")
print(current_date)

print("\nТекущая дата и время:")
print(current_datetime)

# ============================================================
# 3. ПОЛУЧЕНИЕ ОТДЕЛЬНЫХ КОМПОНЕНТОВ DATETIME
# ============================================================

# У объекта datetime можно получить отдельные компоненты
# через его атрибуты: year, month, day и другие.

print("\nОтдельные компоненты текущей даты и времени:")
print(f"Год: {current_datetime.year}")
print(f"Месяц: {current_datetime.month}")
print(f"День: {current_datetime.day}")
print(f"Часы: {current_datetime.hour}")
print(f"Минуты: {current_datetime.minute}")
print(f"Секунды: {current_datetime.second}")
print(f"Микросекунды: {current_datetime.microsecond}")

# Методы date() и time() позволяют получить из datetime
# отдельный объект даты или времени.
date_part = current_datetime.date()
time_part = current_datetime.time()

print("\nДата, извлечённая из datetime:")
print(date_part)

print("\nВремя, извлечённое из datetime:")
print(time_part)

# ============================================================
# 4. REPLACE() — СОЗДАНИЕ ИЗМЕНЁННОЙ ДАТЫ ИЛИ ВРЕМЕНИ
# ============================================================

# Объекты date, time и datetime являются неизменяемыми.
# Метод replace() не меняет исходный объект, а создаёт новый
# с заменёнными компонентами.

original_datetime = datetime(2026, 7, 28, 19, 15)

changed_datetime = original_datetime.replace(
    day=30,
    hour=10,
    minute=45,
)

print("\nИсходные дата и время:")
print(original_datetime)

print("\nНовые дата и время после replace():")
print(changed_datetime)

# ============================================================
# 5. СРАВНЕНИЕ ДАТ И ВРЕМЕНИ
# ============================================================

# Объекты date и datetime можно сравнивать обычными операторами.
# Более поздняя дата считается большей.

first_datetime = datetime(2026, 7, 28, 10, 0)
second_datetime = datetime(2026, 7, 28, 18, 0)

print("\nРезультаты сравнения:")
print(f"Первое время раньше второго: {first_datetime < second_datetime}")
print(f"Первое время позже второго: {first_datetime > second_datetime}")
print(f"Значения равны: {first_datetime == second_datetime}")

# Сравнение удобно использовать для проверки,
# наступил ли дедлайн или произошло ли событие вовремя.

deadline = datetime(2026, 7, 28, 20, 0)
event_time = datetime(2026, 7, 28, 19, 45)

event_happened_on_time = event_time <= deadline

print("\nПроверка дедлайна:")
print(f"Событие произошло вовремя: {event_happened_on_time}")
