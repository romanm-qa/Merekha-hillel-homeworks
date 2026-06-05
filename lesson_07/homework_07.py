# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити/доповнити."""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier

        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)

# task 2
""" Написати функцію, яка обчислює суму двох чисел. """
def sum_numbers(first_number, second_number):
    return first_number + second_number

print(sum_numbers(365, 500))

# task 3
""" Написати функцію, яка розрахує середнє арифметичне списку чисел. """
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers_list = list(range(1, 11))

print(calculate_average(numbers_list))

# task 4
""" Написати функцію, яка приймає рядок та повертає його у зворотному порядку. """
def reverse_string(text):
    return text[::-1]

print(reverse_string("Roman!"))

# task 5
""" Написати функцію, яка приймає список слів та повертає найдовше слово у списку. """
def find_longest_word(words):
    return max(words, key=len)

words_list = ["cat", "elephant", "dog"]

print(find_longest_word(words_list))

# task 6
""" Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка. """
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

""" Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним. """

# task 7 -> Calculate sum of even numbers in the list
def calculate_even_sum(numbers):
    even_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number

    return even_sum

numbers_list = list(range(10))

print(calculate_even_sum(numbers_list))

# task 8 -> Create a function that returns only string values from a list
def get_string_items(items):
    string_items = []

    for item in items:
        if type(item) == str:
            string_items.append(item)

    return string_items

items_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

print(get_string_items(items_list))

# task 9 -> Create a function that returns the number of words in the last sentence of a list
def get_last_sentence_word_count(sentences):
    last_sentence = sentences[-1]
    words = last_sentence.split()

    return len(words)

sentence = [
    "Hello world",
    "Python is awesome",
    "This is the last sentence"
]

print(get_last_sentence_word_count(sentence))

# task 10 -> # Filter and sort cars by search criteria
def get_matching_cars(car_data, search_criteria):
    filtered_cars = filter(
        lambda car: car[1][1] >= search_criteria[0]
                    and car[1][2] >= search_criteria[1]
                    and car[1][4] <= search_criteria[2],
        car_data.items()
    )

    result = sorted(filtered_cars, key=lambda car: car[1][4])[:5]

    return result

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

matching_cars = get_matching_cars(car_data, search_criteria)

for car_name, car_info in matching_cars:
    print(car_name, car_info)