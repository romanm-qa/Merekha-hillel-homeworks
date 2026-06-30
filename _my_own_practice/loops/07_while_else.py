# while...else
# else выполнится только если цикл закончился без break.

secret_number = 7
attempts = 3

while attempts:
    guess = int(input("Guess the number: "))
    attempts -= 1

    if guess == secret_number:
        print("You guessed it!")
        break
else:
    print("No attempts left. You lost.")

# else относится именно к while, а не к if.
# Он выполняется только тогда,
# когда цикл завершился без break.
# Если внутри while сработал break,
# блок else будет пропущен.