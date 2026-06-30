# Бесконечный цикл.
# Программа работает, пока пользователь сам не решит выйти.

while True:
    print("\n=== Menu ===")
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Program started.")

    elif choice == "2":
        print("Settings opened.")

    # Если пользователь выбрал Exit — выходим из бесконечного цикла.
    elif choice == "3":
        print("Goodbye!")
        break

    # Обработка неверного ввода.
    else:
        print("Invalid option. Try again.")