# for...else
# else выполнится только если цикл завершился без break.
for number in range(10):
    if number % 3 == 0:
        print(number)
else:
    print("The loop finished successfully.")

# Ищем число в списке.
numbers = [5, 8, 12, 18, 21]
target = 12

for number in numbers:
    if number == target:
        print("Number found!")
        break
else:
    print("Number not found.")