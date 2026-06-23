"""
Создание нового исключения внутри except.
Иногда мы перехватываем одну ошибку,
но хотим сообщить о проблеме через другую.
В таком случае можно создать новое исключение
с помощью raise.
raise ValueError("Описание ошибки")
"""
a = 5
b = 0

def run():
    try:
        result = a / b
        print(result)

    except ZeroDivisionError:
        print("ZeroDivisionError")

        if b == 0:
            raise ValueError("b cannot be 0")

try:
    run()

except TypeError:
    print("TypeError")

except ValueError:
    print("Global ValueError detected")