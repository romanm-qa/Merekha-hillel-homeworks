# Match-case (аналог switch-case из других языков)
#
# Используется, когда нужно сравнить одну переменную
# с несколькими возможными значениями.
#
# Вместо длинной конструкции:
#
# if choice == 1:
#     ...
# elif choice == 2:
#     ...
# elif choice == 3:
#     ...
#
# можно использовать:
#
# match choice:
#     case 1:
#         ...
#     case 2:
#         ...
#     case 3:
#         ...
#     case _:
#         ...
#
# case _ работает как else.

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Вы выбрали вариант 1")
    case 2:
        print("Вы выбрали вариант 2")
    case 3:
        print("Вы выбрали выриант 3")
    case _:
        print("Нет такой опции")
