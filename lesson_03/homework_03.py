# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)

# Задачі 04 -10:
# Переведіть задачі з книги "Математика, 5 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в п'ятому класі

# task 04
"""Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(total_area)

# task 05
"""Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі."""
total_products = 375291
first_and_second_warehouses = 250449
second_and_third_warehouses = 222950

first_warehouse = total_products - second_and_third_warehouses
third_warehouse = total_products - first_and_second_warehouses
second_warehouse = total_products - (first_warehouse + third_warehouse)
print(first_warehouse)
print(third_warehouse)
print(second_warehouse)

# task 06
"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера."""
monthly_payment = 1179
years_count = 1.5
months_in_year = 12

months_count = years_count * months_in_year
computer_price = int(monthly_payment * months_count)
print(computer_price)

# task 07
"""Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(8019 % 8)
print(9907 % 9)
print(2789 % 5)
print(7248 % 6)
print(7128 % 5)
print(19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza_quantity = 4
large_pizza_price = 274
large_pizza_price_with_quantity = large_pizza_quantity * large_pizza_price

medium_pizza_quantity = 2
medium_pizza_price = 218
medium_pizza_price_with_quantity = medium_pizza_quantity * medium_pizza_price

juice_quantity = 4
juice_price = 35
juice_price_with_quantity = juice_quantity * juice_price

cake_quantity = 1
cake_price = 350
cake_price_with_quantity = cake_quantity * cake_price

water_quantity = 3
water_price = 21
water_price_with_quantity = water_quantity * water_price

total_order_price = (
    large_pizza_price_with_quantity
    + medium_pizza_price_with_quantity
    + juice_price_with_quantity
    + cake_price_with_quantity
    + water_price_with_quantity
)
print(total_order_price)

# task 09
"""Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?"""
total_photos = 232
album_per_page = 8
total_pages = total_photos // album_per_page
print(total_pages)

# task 10
"""Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?"""
distance_km = 1600
fuel_per_100_km = 9
fuel_tank_capacity = 48

total_fuel_needed = int(distance_km / 100) * fuel_per_100_km
# if we assume the car starts with a full tank
minimum_refuels = int(total_fuel_needed / fuel_tank_capacity) - 1
print(total_fuel_needed)
print(minimum_refuels)