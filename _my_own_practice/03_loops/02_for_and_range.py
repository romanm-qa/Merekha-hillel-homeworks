# for перебирает элементы итерируемого объекта по одному.
# На каждой итерации переменная char получает следующий символ.
text = "Python"

print("Перебор строки:")
print(f"Исходная строка: {text!r}")

for char in text:
    print(f"Текущий символ: {char!r}")

# При переборе списка переменная name получает очередной элемент.
names = ["Roman", "Alex", "Kate"]

print("\nПеребор списка:")
print(f"Исходный список: {names!r}")

for name in names:
    print(f"Текущее имя: {name!r}")

# Внутри цикла можно проверять условие и накапливать результат.
text = "banana"
target = "a"
count = 0

print("\nПодсчёт символов:")
print(f"Исходная строка: {text!r}")
print(f"Искомый символ: {target!r}")

for char in text:
    if char == target:
        count += 1

print(f"Количество совпадений: {count!r}")

# Если объект пустой, тело цикла не выполнится ни разу.
numbers = []

print("\nПеребор пустого списка:")
print(f"Исходный список: {numbers!r}")

for number in numbers:
    print(f"Эта строка не появится: {number!r}")

print("Цикл завершён")

# range(stop) задаёт последовательность целых чисел от 0 до stop.
# Правая граница stop НЕ включается.
# range — отдельный тип, а не список.
print("\nrange(stop):")
print(f"range(4) -> {range(4)!r}")
print(f"list(range(4)) -> {list(range(4))!r}")

for number in range(4):
    print(f"Текущее число: {number!r}")

# range(start, stop) позволяет задать начало.
# start включается, stop не включается.
print("\nrange(start, stop):")
print(f"list(range(2, 5)) -> {list(range(2, 5))!r}")

for number in range(2, 5):
    print(f"Текущее число: {number!r}")

# range(start, stop, step) позволяет задать шаг.
# По умолчанию шаг равен 1.
print("\nrange(start, stop, step):")
print(f"list(range(1, 8, 2)) -> {list(range(1, 8, 2))!r}")

for number in range(1, 8, 2):
    print(f"Текущее число: {number!r}")

# Отрицательный шаг позволяет двигаться в обратную сторону.
print("\nОтрицательный шаг:")
print(f"list(range(3, 0, -1)) -> {list(range(3, 0, -1))!r}")

for number in range(3, 0, -1):
    print(f"Текущее число: {number!r}")

# Если направление шага не позволяет дойти до stop, range будет пустым.
print("\nПустой range:")
print(f"list(range(3, 0)) -> {list(range(3, 0))!r}")
print(f"list(range(0, 3, -1)) -> {list(range(0, 3, -1))!r}")

# Шаг не может быть равен нулю: возникает ValueError.
print("\nНулевой шаг:")

try:
    range(1, 5, 0)
except ValueError as error:
    print(f"range(1, 5, 0) -> {type(error).__name__}: {error}")

# Если значение переменной не нужно, её часто называют _.
# Здесь важно только повторить действие три раза.
print("\nПовторение действия:")
print(f"Количество повторений: {3!r}")

for _ in range(3):
    print("Hello!")

# enumerate() позволяет получать индекс и элемент одновременно.
# По умолчанию индексы начинаются с 0.
names = ["Roman", "Alex", "Kate"]

print("\nПеребор с индексами:")
print(f"Исходный список: {names!r}")

for index, name in enumerate(names):
    print(f"Индекс: {index!r}; имя: {name!r}")

# start задаёт начало нумерации, но не меняет индексы самого списка.
print("\nНумерация с единицы:")
print(f"Исходный список: {names!r}")

for position, name in enumerate(names, start=1):
    print(f"Номер: {position!r}; имя: {name!r}")

# zip() позволяет перебирать несколько объектов одновременно.
# Здесь каждая пара распаковывается в name и score.
names = ["Roman", "Alex", "Kate"]
scores = [90, 85, 95]

print("\nСовместный перебор через zip():")
print(f"Исходные имена: {names!r}")
print(f"Исходные баллы: {scores!r}")

for name, score in zip(names, scores):
    print(f"Имя: {name!r}; балл: {score!r}")

# По умолчанию zip() заканчивает перебор на самом коротком объекте.
scores = [90, 85]

print("\nzip() с разной длиной списков:")
print(f"Исходные имена: {names!r}")
print(f"Исходные баллы: {scores!r}")

for name, score in zip(names, scores):
    print(f"Имя: {name!r}; балл: {score!r}")

# Обычный перебор словаря возвращает ключи.
user = {"name": "Roman", "role": "student"}

print("\nПеребор ключей словаря:")
print(f"Исходный словарь: {user!r}")

for key in user:
    print(f"Текущий ключ: {key!r}")

# items() позволяет получать ключ и значение одновременно.
print("\nПеребор ключей и значений:")
print(f"Исходный словарь: {user!r}")

for key, value in user.items():
    print(f"Ключ: {key!r}; значение: {value!r}")

# Обычное целое число не является итерируемым объектом.
print("\nПопытка перебрать число:")
number = 5
print(f"Исходное число: {number!r}")

try:
    for item in number:
        print(item)
except TypeError as error:
    print(f"for item in number -> {type(error).__name__}: {error}")
