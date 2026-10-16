# Условное выражение выбирает одно из двух значений.
# Запись: значение_если_истина if условие else значение_если_ложь.
# Сначала проверяется условие, затем вычисляется только выбранная ветка.
age = 20

print("Условное выражение — проверка возраста:")
print(f"Исходный возраст: {age!r}")
status = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"
print(f"Полученный статус: {status!r}")

# Тот же результат можно получить обычной конструкцией if/else.
age = 20

print("\nТа же проверка через if/else:")
print(f"Исходный возраст: {age!r}")
if age >= 18:
    status = "Совершеннолетний"
else:
    status = "Несовершеннолетний"
print(f"Полученный статус: {status!r}")

# Условие number % 2 == 0 проверяет чётность числа.
number = 7

print("\nПроверка чётности:")
print(f"Исходное число: {number!r}")
result = "Чётное" if number % 2 == 0 else "Нечётное"
print(f"Результат проверки: {result!r}")

# Ветками могут быть переменные, а не только строки.
first_number = 15
second_number = 20

print("\nВыбор большего числа:")
print(f"Первое число: {first_number!r}")
print(f"Второе число: {second_number!r}")
max_number = first_number if first_number > second_number else second_number
print(f"Большее число: {max_number!r}")

# Пустой список считается ложным, непустой — истинным.
users = []

print("\nПроверка пустого списка:")
print(f"Исходный список пользователей: {users!r}")
message = "Есть пользователи" if users else "Список пуст"
print(f"Сообщение: {message!r}")

users = ["Roman", "Anna"]

print("\nПроверка непустого списка:")
print(f"Исходный список пользователей: {users!r}")
message = "Есть пользователи" if users else "Список пуст"
print(f"Сообщение: {message!r}")

# Условное выражение удобно для простого выбора значения.
# Для сложной логики используем обычную конструкцию if/elif/else.
score = 95
passing_score = 60

print("\nПроверка проходного балла:")
print(f"Исходные баллы: {score!r}")
print(f"Проходной балл: {passing_score!r}")
grade = "Зачтено" if score >= passing_score else "Не зачтено"
print(f"Результат: {grade!r}")
