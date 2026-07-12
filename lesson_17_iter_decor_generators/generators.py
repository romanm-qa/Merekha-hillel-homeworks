def numbers():
    print("Старт")
    yield 1
    print("После первого yield")
    yield 2
    print("Конец")


for number in numbers():
    print(number)