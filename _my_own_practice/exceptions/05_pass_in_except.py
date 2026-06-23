"""
pass в блоке except.
Иногда ошибка ожидаема и нам не нужно
никак её обрабатывать.
В таком случае можно использовать pass.
Ошибка будет перехвачена,
но никакой код выполнен не будет.
"""
try:
    number = int(input("Enter number: "))
except ValueError:
    pass # pass = ничего не делать

print("Program continues")