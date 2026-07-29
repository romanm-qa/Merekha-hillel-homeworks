from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# ============================================================
# 1. NAIVE И AWARE DATETIME
# ============================================================

# Naive datetime не содержит информации о часовом поясе.
# Python знает дату и время, но не знает, к какой зоне они относятся.

naive_datetime = datetime(2026, 7, 28, 19, 15)

print("Naive datetime:")
print(naive_datetime)

print("\nЧасовой пояс naive datetime:")
print(naive_datetime.tzinfo)

# Aware datetime содержит информацию о часовом поясе.
# timezone.utc представляет всемирное координированное время UTC.

aware_datetime = datetime(
    2026,
    7,
    28,
    19,
    15,
    tzinfo=timezone.utc,
)

print("\nAware datetime:")
print(aware_datetime)

print("\nЧасовой пояс aware datetime:")
print(aware_datetime.tzinfo)

# ============================================================
# 2. ТЕКУЩЕЕ ВРЕМЯ В UTC
# ============================================================

# datetime.now(timezone.utc) возвращает текущий момент
# в часовом поясе UTC.

current_utc_datetime = datetime.now(timezone.utc)

print("\nТекущие дата и время в UTC:")
print(current_utc_datetime)

# ============================================================
# 3. ZONEINFO — ЧАСОВЫЕ ПОЯСА РЕАЛЬНЫХ РЕГИОНОВ
# ============================================================

# ZoneInfo создаёт часовой пояс по его системному названию.
# Он автоматически учитывает смещение от UTC
# и переходы между летним и зимним временем.

kyiv_timezone = ZoneInfo("Europe/Kyiv")
new_york_timezone = ZoneInfo("America/New_York")

event_in_utc = datetime(
    2026,
    7,
    28,
    16,
    15,
    tzinfo=timezone.utc,
)

event_in_kyiv = event_in_utc.astimezone(kyiv_timezone)
event_in_new_york = event_in_utc.astimezone(new_york_timezone)

print("\nОдин момент в разных часовых поясах:")

print(f"UTC:      {event_in_utc}")
print(f"Киев:     {event_in_kyiv}")
print(f"Нью-Йорк: {event_in_new_york}")

# ============================================================
# 4. ПЕРЕВОД ЛОКАЛЬНОГО ВРЕМЕНИ В UTC
# ============================================================

# Допустим, событие запланировано на 10:30 по Токио.
# Создаём отдельный объект часового пояса для этого примера.

tokyo_timezone = ZoneInfo("Asia/Tokyo")

meeting_in_tokyo = datetime(
    2026,
    8,
    15,
    10,
    30,
    tzinfo=tokyo_timezone,
)

# astimezone() переводит тот же момент из Токио в UTC.
meeting_in_utc = meeting_in_tokyo.astimezone(timezone.utc)

print("\nВремя встречи в Токио:")
print(meeting_in_tokyo)

print("\nТо же время встречи в UTC:")
print(meeting_in_utc)

# Несмотря на разное отображение времени,
# оба объекта обозначают один и тот же момент.
print("\nЭто один и тот же момент:")
print(meeting_in_tokyo == meeting_in_utc)

# isoformat() создаёт строку и сохраняет смещение часового пояса.
meeting_iso_string = meeting_in_utc.isoformat()

print("\nВремя для передачи через API:")
print(meeting_iso_string)
