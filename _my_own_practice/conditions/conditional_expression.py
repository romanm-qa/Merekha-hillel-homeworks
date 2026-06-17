# Conditional Expression (тернарный оператор)
# Короткая запись if/else для простых условий

# Приклад 1. Перевірка віку
age = 20
status = "Дорослий" if age >= 18 else "Неповнолітній"

print(status)


# Приклад 2. Парне чи непарне число
number = 7
result = "Парне" if number % 2 == 0 else "Непарне"

print(result)

# Приклад 3. Максимальне число
a = 15
b = 20

max_number = a if a > b else b

print(max_number)

# Приклад 4. Перевірка наявності користувачів
users = []

message = "Є користувачі" if users else "Список порожній"

print(message)

# Приклад 5. Перевірка оцінки
score = 95

grade = "Зараховано" if score >= 60 else "Не зараховано"

print(grade)