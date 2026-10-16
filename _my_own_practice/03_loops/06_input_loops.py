# input() возвращает строку.
# Цикл повторяет запрос, пока пользователь не введёт stop.
print("Повторение ввода до команды stop:")

text = input("Введи текст (stop — выход): ")

while text != "stop":
    print(f"Введённый текст: {text!r}")
    text = input("Введи текст (stop — выход): ")

print("Ввод текста завершён")

# while True повторяет запрос до выхода через break.
# int() преобразует строку в целое число.
# Если преобразование невозможно, возникает ValueError.
print("\nВвод целых чисел до нуля:")

while True:
    raw_number = input("Введи целое число (0 — выход): ")

    try:
        number = int(raw_number)
    except ValueError as error:
        print(f"Введённая строка: {raw_number!r}")
        print(f"int(raw_number) -> {type(error).__name__}: {error}")
        continue

    if number == 0:
        print("Введён 0 — завершаем цикл")
        break

    print(f"Полученное число: {number!r}")

print("Ввод чисел завершён")

# Меню работает, пока пользователь не выберет выход.
# strip() убирает пробельные символы по краям строки.
# После приветствия цикл продолжает показывать меню.
name = ""

print("\nМеню:")
print(f"Начальное значение name: {name!r}")

while True:
    print("\n1. Ввести имя")
    print("2. Поздороваться")
    print("3. Выйти")

    choice = input("Выбери пункт: ").strip()

    if choice == "1":
        name = input("Введи имя: ").strip()
        print(f"Сохранённое имя: {name!r}")

    elif choice == "2":
        if name:
            print(f"Привет, {name}!")
        else:
            print("Сначала введи имя")

    elif choice == "3":
        print("Выход из меню")
        break

    else:
        print(f"Неизвестный пункт: {choice!r}")

print("Работа меню завершена")

# for ограничивает количество попыток входа.
# Успешный вход вызывает break, поэтому else пропускается.
# Если все попытки исчерпаны, выполняется else у цикла.
# Логин и пароль ниже — учебные данные для проверки примера.
EXPECTED_LOGIN = "admin"
EXPECTED_PASSWORD = "qwerty"
MAX_ATTEMPTS = 3

print("\nВход с ограничением попыток:")
print(f"Максимальное количество попыток: {MAX_ATTEMPTS!r}")

for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"\nПопытка {attempt} из {MAX_ATTEMPTS}")

    username = input("Введи логин: ")
    password = input("Введи пароль: ")

    if username == EXPECTED_LOGIN and password == EXPECTED_PASSWORD:
        print("Вход выполнен")
        break

    print("Неверный логин или пароль")
else:
    print("Попытки закончились. Доступ запрещён")

print("Проверка входа завершена")
