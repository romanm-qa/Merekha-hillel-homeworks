"""
Блок else в try/except.
Код в else выполняется только тогда, когда в блоке try НЕ возникло ошибок.
Если произошла ошибка и сработал except, блок else будет пропущен.
"""
def divide_numbers():
    while True:
        try:
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))

            result = first_number / second_number

        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)
            print("Please try again")
            print()

        else:
            print("Result:", result)
            break

divide_numbers()

"""
Логика работы:

try
    Если ошибки нет -> выполняется else

except
    Если ошибка есть -> выполняется except

else
    Выполняется только при успешном выполнении try
"""