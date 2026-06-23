"""
Блок finally.

Код внутри finally выполняется всегда:

- была ошибка;
- не было ошибки;
- сработал except;
- сработал else.

finally обычно используют для очистки ресурсов:
закрытия файлов, соединений с БД,
сетевых подключений и т.д.
"""
def function_that_may_fail():
    response = None

    while response not in ("y", "n"):
        response = input("Raise an exception? (y/n): ")

    if response == "y":
        raise ValueError

try:
    function_that_may_fail()

except:
    print("Exception handler")

finally:
    print("Finally block")