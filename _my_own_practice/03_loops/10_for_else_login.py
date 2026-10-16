# Пользователь может попробовать войти 3 раза.
# Если логин и пароль верные — выходим из цикла.
# Если все попытки закончились — блокируем доступ.
LOGIN = "admin"
PASSWORD = "qwerty"

attempts = 3

for _ in range(attempts):
    username = input("Username: ")
    password = input("Password: ")

    if username == LOGIN and password == PASSWORD:
        print("Login successful!")
        break
    else:
        print("Invalid username or password.")
else:
    print("Too many failed attempts.")
    print("Access denied.")

# range(attempts) создаёт 3 итерации.
# Если пользователь успешно вошёл, выполняется break.
# Из-за break блок else уже НЕ выполнится.
# Если все попытки закончились и break ни разу не сработал, выполняется else.