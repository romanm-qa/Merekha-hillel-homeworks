"""
Внутри функции можно обработать одну ошибку,
а другую передать выше.

Если ошибка не была обработана текущим try/except,
она поднимается дальше по стеку вызовов,
пока не найдётся подходящий except.
"""
def function():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))

        print(first / second)

    except ValueError:
        print("Invalid value")

try:
    function()

except ZeroDivisionError:
    print("ZeroDivisionError detected!")