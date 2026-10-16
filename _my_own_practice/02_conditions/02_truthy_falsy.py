# В условии объект проверяется на истинность.
# Truthy — считается истинным, falsy — считается ложным.
# bool() позволяет явно увидеть результат такой проверки.
print("Ложные значения — falsy:")
print(f"bool(False) -> {bool(False)!r}")
print(f"bool(None) -> {bool(None)!r}")
print(f"bool(0) -> {bool(0)!r}")
print(f"bool(0.0) -> {bool(0.0)!r}")
print(f"bool('') -> {bool('')!r}")
print(f"bool([]) -> {bool([])!r}")
print(f"bool(()) -> {bool(())!r}")
print(f"bool({{}}) -> {bool({})!r}")
print(f"bool(set()) -> {bool(set())!r}")
print(f"bool(frozenset()) -> {bool(frozenset())!r}")

# Непустые строки и коллекции, а также ненулевые числа — truthy.
print("\nИстинные значения — truthy:")
print(f"bool(True) -> {bool(True)!r}")
print(f"bool(10) -> {bool(10)!r}")
print(f"bool(-5) -> {bool(-5)!r}")
print(f"bool('Roman') -> {bool('Roman')!r}")
print(f"bool([1]) -> {bool([1])!r}")

# if users проверяет истинность списка: пустой список считается ложным.
users = []

print("\nПустой список в условии:")
print(f"Исходный список пользователей: {users!r}")
if users:
    print("Есть пользователи")
else:
    print("Список пользователей пуст")

users = ["Roman", "Anna"]

print("\nНепустой список в условии:")
print(f"Исходный список пользователей: {users!r}")
if users:
    print("Есть пользователи")
else:
    print("Список пользователей пуст")

# not меняет результат проверки истинности на противоположный.
user_name = ""

print("\nПроверка пустой строки через not:")
print(f"Исходное имя: {user_name!r}")
if not user_name:
    print("Имя не заполнено")
else:
    print("Имя заполнено")

# Строки '0', 'False' и строка с пробелом непустые — они truthy.
print("\nНепустые строки с неожиданной истинностью:")
print(f"bool('0') -> {bool('0')!r}")
print(f"bool('False') -> {bool('False')!r}")
print(f"bool(' ') -> {bool(' ')!r}")

# Истинность коллекции зависит от её пустоты, а не от истинности элементов.
# Список [0] содержит один элемент, поэтому считается истинным.
numbers = [0]

print("\nНепустой список с нулём:")
print(f"Исходный список: {numbers!r}")
print(f"bool(numbers) -> {bool(numbers)!r}")
print(f"bool(numbers[0]) -> {bool(numbers[0])!r}")

# is None проверяет именно None, а не все ложные значения.
# Для проверки None используем is None или is not None.
user_name = None

print("\nПроверка отсутствующего значения:")
print(f"Исходное имя: {user_name!r}")
if user_name is None:
    print("Значение имени отсутствует")
else:
    print("Значение имени передано")

# Ноль может быть допустимым результатом: он falsy, но не None.
score = 0

print("\nРазница между if score и if score is not None:")
print(f"Исходные баллы: {score!r}")
if score:
    print("Баллы считаются истинным значением")
else:
    print("Баллы считаются ложным значением")

if score is not None:
    print("Результат передан, даже если он равен нулю")
else:
    print("Результат отсутствует")
