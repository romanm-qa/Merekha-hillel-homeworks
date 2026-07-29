from datetime import datetime, timedelta

# ============================================================
# 1. TIMEDELTA — ВРЕМЕННОЙ ИНТЕРВАЛ
# ============================================================

# datetime представляет конкретный момент:
# например, 28 июля 2026 года в 19:15.
#
# timedelta представляет продолжительность:
# например, 5 дней, 3 часа и 30 минут.

time_interval = timedelta(
    days=5,
    hours=3,
    minutes=30,
)

print("Временной интервал:")
print(time_interval)

print("\nТип значения:")
print(type(time_interval))

# ============================================================
# 2. ДОБАВЛЕНИЕ И ВЫЧИТАНИЕ TIMEDELTA
# ============================================================

# timedelta можно добавлять к datetime или вычитать из него.
# Результатом будет новый объект datetime.

start_datetime = datetime(2026, 7, 28, 19, 15)

future_datetime = start_datetime + time_interval
past_datetime = start_datetime - time_interval

print("\nИсходная дата и время:")
print(start_datetime)

print("\nПосле добавления временного интервала:")
print(future_datetime)

print("\nПосле вычитания временного интервала:")
print(past_datetime)

# ============================================================
# 3. РАЗНИЦА МЕЖДУ ДВУМЯ DATETIME
# ============================================================

# Если вычесть один datetime из другого,
# результатом будет объект timedelta.

heartbeat_sent_at = datetime(2026, 7, 28, 19, 15, 0)
heartbeat_received_at = datetime(2026, 7, 28, 19, 15, 8)

heartbeat_delay = heartbeat_received_at - heartbeat_sent_at

print("\nВремя отправки heartbeat:")
print(heartbeat_sent_at)

print("\nВремя получения heartbeat:")
print(heartbeat_received_at)

print("\nЗадержка heartbeat:")
print(heartbeat_delay)

print("\nТип полученной разницы:")
print(type(heartbeat_delay))

# ============================================================
# 4. DAYS, SECONDS И TOTAL_SECONDS()
# ============================================================

# У timedelta есть отдельные атрибуты days и seconds.
#
# days — количество полных дней;
# seconds — оставшиеся секунды без учёта полных дней;
# total_seconds() — весь интервал в секундах.

long_interval = timedelta(
    days=2,
    hours=3,
    minutes=10,
)

print("\nПродолжительный интервал:")
print(long_interval)

print(f"Полных дней: {long_interval.days}")
print(f"Оставшихся секунд: {long_interval.seconds}")
print(f"Всего секунд: {long_interval.total_seconds()}")

# ============================================================
# 5. ПРОВЕРКА ДОПУСТИМОГО ВРЕМЕННОГО ИНТЕРВАЛА
# ============================================================

# Представим, что heartbeat должен приходить
# не позднее чем через 10 секунд после отправки.

maximum_delay = timedelta(seconds=10)

heartbeat_arrived_on_time = heartbeat_delay <= maximum_delay

print("\nПроверка heartbeat:")
print(f"Фактическая задержка: {heartbeat_delay.total_seconds()} секунд")
print(f"Допустимая задержка: {maximum_delay.total_seconds()} секунд")
print(f"Heartbeat получен вовремя: {heartbeat_arrived_on_time}")
