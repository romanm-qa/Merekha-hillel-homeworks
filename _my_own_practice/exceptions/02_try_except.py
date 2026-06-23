"""
try / except
Используется для обработки ошибок во время выполнения программы.
try:
    код, который может вызвать ошибку
except:
    код, который выполнится, если ошибка произошла
Преимущество:
программа не падает с Traceback,
а обрабатывает ошибку и продолжает работу.
"""

# В блоке try может быть несколько потенциальных ошибок,
# но за один запуск будет обработана только первая возникшая ошибка.

my_list = [1, 2, 3]

try:
    number = int(input("Enter number: "))  # ValueError
    result = 10 / number                   # ZeroDivisionError
    print(my_list[10])                     # IndexError

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Division by zero")

except IndexError:
    print("Index out of range")

except Exception:
    # Общий обработчик для всех остальных ошибок
    print("Unexpected error")

"""
Порядок except имеет значение.

Python проверяет блоки except сверху вниз
и выполняет первый подходящий.

Сначала указываются более конкретные исключения:
- ValueError
- ZeroDivisionError
- IndexError

Общий except Exception должен находиться последним.
"""