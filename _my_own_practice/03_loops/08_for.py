# Цикл for перебирает элементы последовательности.
# В данном случае — символы строки.

text = input("Enter text: ")
find_char = input("Enter character to find: ")

count = 0

for char in text:
    if char == find_char:
        count += 1
        print(f"Found: {char}")

print(f"Total found: {count}")

# text — это строка.
# Цикл for берет по одному символу из строки и сохраняет его в переменную char.
# На каждой итерации char содержит новый символ.
# Если символ совпал с тем, который ищем, увеличиваем счетчик count.