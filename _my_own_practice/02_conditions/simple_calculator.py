"""
1) Ввести первое число з консолі
2) Обрати математичну операцію (+, -, *, /)
3) Ввести друге число з консолі
4) Вивести результат обчислення
"""
from unittest import case

first_number = float(input("Enter the first number: "))
operation = input("Enter the operation: ")
second_number = float(input("Enter the second number: "))
result = None

match operation:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        if second_number == 0:
            print("We cannot use 0")
        else:
            result = first_number / second_number
    case _:
        print("Invalid operation")

if result is not None:
    print(result)