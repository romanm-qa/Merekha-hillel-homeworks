# Task 1. average_male_height()
# Словарь содержит данные про рост и пол людей.
# Написать функцию, которая возвращает средний рост мужчин.
people = {
    "person1": {"gender": "Male", "height": 175},
    "person2": {"gender": "Female", "height": 160},
    "person3": {"gender": "Male", "height": 180},
}

def average_male_height(people):
    male_height = 0
    male_count = 0

    for person in people.values():
        if person["gender"] == "Male":
            male_height += person["height"]
            male_count += 1

    return male_height / male_count

print(average_male_height(people))

# Task 2
# Есть список словарей с журналами. Нужно найти среднюю цену журналов, у которых тираж (volume) больше 10000.
magazines = [
    {"name": "Space", "volume": 20000, "price": 12.45},
    {"name": "SeaSide", "volume": 5000, "price": 10.45},
    {"name": "Fortune", "volume": 10000, "price": 17.99},
    {"name": "Vouge", "volume": 25000, "price": 7.68},
]
def average_price(magazines):
    total_price = 0
    magazines_count = 0

    for magazine in magazines:
        if magazine["volume"] > 10000:
            magazines_count += 1
            total_price += magazine["price"]

    return total_price / magazines_count

print(average_price(magazines))

# Задача 3:Написать функцию, которая возвращает кортеж, содержащий:
# 1. Количество пассажиров, у которых больше двух вещей.
# 2. Есть ли хотя бы один пассажир с одной вещью весом менее 25 кг.
# 3. Количество пассажиров, у которых число вещей больше среднего количества вещей среди всех пассажиров.
luggage = [
    {"number_of_items": 3, "total_weight": 30},
    {"number_of_items": 2, "total_weight": 20},
    {"number_of_items": 1, "total_weight": 15},
]
def luggage_statistics(luggage):
    more_than_two = 0
    has_light_single_bag = False
    total_items = 0
    above_average = 0

    # Считаем первые два пункта и сумму всех вещей
    for passenger in luggage:
        if passenger["number_of_items"] > 2:
            more_than_two += 1

        if passenger["number_of_items"] == 1 and passenger["total_weight"] < 25:
            has_light_single_bag = True

        total_items += passenger["number_of_items"]

    # Находим среднее количество вещей
    average_items = total_items / len(luggage)

    # Считаем пассажиров, у которых вещей больше среднего
    for passenger in luggage:
        if passenger["number_of_items"] > average_items:
            above_average += 1

    return more_than_two, has_light_single_bag, above_average

print(luggage_statistics(luggage))