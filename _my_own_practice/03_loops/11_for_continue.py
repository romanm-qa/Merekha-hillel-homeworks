# continue пропускает текущую итерацию и сразу переходит к следующей.
text = "hello world"

for char in text:
    # Не выводим букву "o"
    if char == "o":
        continue

    print(char)

users = ["Roman", "", "Alex", "", "Kate"]

for user in users:
    # Пропускаем пустые записи
    if user == "":
        continue

    print(user)