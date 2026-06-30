# Пользователь вводит числа.
# Когда вводит 0 — цикл заканчивается.

number = int(input("Enter number (0 to stop): "))

while number != 0:
    print("You entered:", number)

    number = int(input("Enter number (0 to stop): "))

print("Program finished.")
