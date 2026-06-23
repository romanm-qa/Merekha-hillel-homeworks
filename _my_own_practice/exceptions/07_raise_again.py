"""
Повторное выбрасывание исключения.
Иногда ошибку нужно обработать локально
(например, записать в лог или вывести сообщение),
но при этом передать её выше.
Для этого используется raise без аргументов.
raise повторно выбрасывает текущую ошибку.
"""
def function():
    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))

        print(a / b)

    except ValueError as error:
        print("ValueError:", error)

        raise

try:
    function()

except TypeError:
    print("TypeError detected")

except ValueError:
    print("Global ValueError handler")

except ZeroDivisionError:
    print("ZeroDivisionError detected")

"""
Где используется raise в except:

- запись ошибки в лог;
- отправка ошибки в систему мониторинга;
- дополнительная обработка ошибки;
- передача ошибки на более высокий уровень приложения.
"""