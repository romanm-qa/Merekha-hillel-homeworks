"""
Обработка нескольких ошибок в одном except.

Если для разных ошибок нужна одинаковая логика обработки,
их можно перечислить через запятую в кортеже.

except (ValueError, ZeroDivisionError) as error:

Переменная error содержит информацию
о возникшей ошибке.
"""
def divide_numbers():
    while True:
        try:
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))

            print(first_number / second_number)
            break

        except (ValueError, ZeroDivisionError) as error:
            print(error)

divide_numbers()