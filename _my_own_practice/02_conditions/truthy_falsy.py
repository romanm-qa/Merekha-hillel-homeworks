# Truthy и Falsy значення в Python

# Порожній список -> False
is_ready = []

if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet"

print(state_msg)

# Непорожній список -> True
is_ready = [1]

if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet"

print(state_msg)

# None -> False
user_name = None

if user_name:
    print("Ім'я вказано")
else:
    print("Ім'я не вказано")

# Рядок з текстом -> True
user_name = "Roman"

if user_name:
    print("Ім'я вказано")
else:
    print("Ім'я не вказано")

# Нуль -> False
number = 0

if number:
    print("Число не нуль")
else:
    print("Число дорівнює нулю")

# Будь-яке інше число -> True
number = 10

if number:
    print("Число не нуль")
else:
    print("Число дорівнює нулю")