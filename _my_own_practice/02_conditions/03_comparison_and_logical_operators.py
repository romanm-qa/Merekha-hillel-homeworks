# Сравнения чисел возвращают True или False.
# = присваивает значение, == проверяет равенство.
first_number = 10
second_number = 20

print("Операторы сравнения:")
print(f"Первое число: {first_number!r}")
print(f"Второе число: {second_number!r}")
print(f"first_number == second_number -> {first_number == second_number!r}")
print(f"first_number != second_number -> {first_number != second_number!r}")
print(f"first_number < second_number -> {first_number < second_number!r}")
print(f"first_number > second_number -> {first_number > second_number!r}")
print(f"first_number <= second_number -> {first_number <= second_number!r}")
print(f"first_number >= second_number -> {first_number >= second_number!r}")

# <= и >= включают равенство.
age = 18

print("\nПроверка границы:")
print(f"Исходный возраст: {age!r}")
print(f"age > 18 -> {age > 18!r}")
print(f"age >= 18 -> {age >= 18!r}")

# Цепочка сравнений проверяет сразу обе границы.
number = 7

print("\nЦепочка сравнений:")
print(f"Исходное число: {number!r}")
print(f"0 <= number < 10 -> {0 <= number < 10!r}")
print(f"number >= 0 and number < 10 -> {number >= 0 and number < 10!r}")

# and — для истинного результата должны выполняться оба условия.
age = 20
has_ticket = True

print("\nОба условия — and:")
print(f"Исходный возраст: {age!r}")
print(f"Есть билет: {has_ticket!r}")
if age >= 18 and has_ticket:
    print("Вход разрешён")
else:
    print("Возраст не подходит или билета нет")

# or — достаточно хотя бы одного истинного условия.
is_admin = False
is_owner = True

print("\nХотя бы одно условие — or:")
print(f"Администратор: {is_admin!r}")
print(f"Владелец: {is_owner!r}")
if is_admin or is_owner:
    print("Редактирование разрешено")
else:
    print("Редактирование запрещено")

# not меняет истинность на противоположную и всегда возвращает bool.
is_blocked = False

print("\nОтрицание — not:")
print(f"Пользователь заблокирован: {is_blocked!r}")
print(f"not is_blocked -> {not is_blocked!r}")
if not is_blocked:
    print("Пользователь не заблокирован")

# Сравнения выполняются раньше not, затем and, затем or.
# Скобки позволяют явно задать нужную группировку.
is_admin = True
is_owner = False
is_blocked = True

print("\nПриоритет операторов и скобки:")
print(f"Администратор: {is_admin!r}")
print(f"Владелец: {is_owner!r}")
print(f"Заблокирован: {is_blocked!r}")
result = is_admin or is_owner and not is_blocked
print(f"is_admin or is_owner and not is_blocked -> {result!r}")
result = (is_admin or is_owner) and not is_blocked
print(f"(is_admin or is_owner) and not is_blocked -> {result!r}")

# Короткое замыкание and: если слева falsy, справа не вычисляется.
# Проверка защищает от деления на ноль.
divisor = 0

print("\nКороткое замыкание — and:")
print(f"Исходный делитель: {divisor!r}")
result = divisor != 0 and 10 / divisor > 2
print(f"divisor != 0 and 10 / divisor > 2 -> {result!r}")

# Короткое замыкание or: если слева truthy, справа не вычисляется.
divisor = 0

print("\nКороткое замыкание — or:")
print(f"Исходный делитель: {divisor!r}")
result = divisor == 0 or 10 / divisor > 2
print(f"divisor == 0 or 10 / divisor > 2 -> {result!r}")

# and и or возвращают один из операндов, не обязательно bool.
# a and b: возвращает a, если a falsy; иначе возвращает b.
# a or b: возвращает a, если a truthy; иначе возвращает b.
first_name = ""
fallback_name = "Guest"

print("\nВозвращаемые значения and и or:")
print(f"Исходное имя: {first_name!r}")
print(f"Запасное имя: {fallback_name!r}")
print(f"first_name or fallback_name -> {first_name or fallback_name!r}")
print(f"first_name and fallback_name -> {first_name and fallback_name!r}")

first_name = "Roman"

print(f"\nИсходное имя: {first_name!r}")
print(f"Запасное имя: {fallback_name!r}")
print(f"first_name or fallback_name -> {first_name or fallback_name!r}")
print(f"first_name and fallback_name -> {first_name and fallback_name!r}")

# or заменяет любое falsy-значение, включая допустимый ноль.
# Если нужно заменить только None, проверяем его явно.
score = 0

print("\nЗначение по умолчанию и ноль:")
print(f"Исходные баллы: {score!r}")
print(f"score or 100 -> {score or 100!r}")
result = score if score is not None else 100
print(f"score if score is not None else 100 -> {result!r}")

# choice == 1 or 2 означает (choice == 1) or 2.
# Если сравнение ложно, результат — число 2, которое считается истинным.
choice = 3
