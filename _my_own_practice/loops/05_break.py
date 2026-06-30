# break позволяет досрочно выйти из цикла.

name = None

while True:

    print("""
=== Menu ===
1. Enter your name
2. Say hello
3. Exit
""")

    choice = input("Choose an option: ")

    if choice == "3":
        print("Goodbye!")
        break

    elif choice == "2":

        if name:
            print(f"Hello, {name}!")
            break
        else:
            print("Please enter your name first.")

    elif choice == "1":
        name = input("Enter your name: ")

    else:
        print("Invalid option.")

# Здесь цикл while True никогда не закончится сам.
# Он завершится только тогда, когда выполнится break.