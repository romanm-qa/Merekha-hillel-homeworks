# Написать функцию capitalize_text(), которая принимает строку и возвращает ее,
# где каждое слово начинается с заглавной буквы, а остальные буквы — строчные.

# split() создал новый список, разбив исходную строку на отдельные слова

# Task 1. capitalize_text()

# append() добавляет каждое слово (после capitalize()) в новый список
# join() объединяет список обратно в одну строку.
text = "hello WORLD!"

def capitalize_text(text):
    result = []

    for word in text.split():
        result.append(word.capitalize())

    return " ".join(result)

print(capitalize_text(text))

# Создать функцию word_count, которая принимает строку текста и возвращает количество слов в этом тексте.
# Считать словами любую последовательность символов, разделенных пробелом

# Task 2. word_count()

# split() → разбил строку на слова;
# len() → посчитал количество элементов.
text_string = "Cats have nice eyes"

def word_count(tex_string):

    return len(text_string.split())

print(word_count(text_string))

# Написать функцию concatenate_strings, которая принимает список строк
# и объединяет их в одну строку через указанный символ.

# Task 3. concatenate_strings()

list_of_strings = ["Python", "is", "awesome"]
separator = "-"

def concatenate_strings(list_of_strings, separator):

    return separator.join(list_of_strings)

print(concatenate_strings(list_of_strings, separator))

# Task 4. String methods

sample_text = "Hello World"

# upper() -> переводит всю строку в верхний регистр
# lower() -> переводит всю строку в нижний регистр
# startswith() -> проверяет, начинается ли строка с указанного текста
# endswith() -> проверяет, заканчивается ли строка указанным текстом
print(sample_text.upper())
print(sample_text.lower())
print(sample_text.startswith("Hello"))
print(sample_text.startswith("World"))
print(sample_text.endswith("World"))
print(sample_text.endswith("Hello"))

# Написать функцию is_palindrome(), которая принимает строку и возвращает True,
# если строка является палиндромом, иначе False.

# Task 4. is_palindrome()
word = "level"

def is_palindrome(word):

    if word == word[::-1]:

        return True

    return False

print(is_palindrome(word))

# Task 5. reverse_words()
# Примеры срезов (slice):
# [:]     → копия всей строки (или списка)
# [:3]    → первые 3 элемента
# [2:]    → с 3-го элемента до конца
# [1:4]   → элементы с индексами 1, 2, 3
# [::2]   → каждый второй элемент
# [::-1]  → все элементы в обратном порядке

sentence = "Python is awesome"

def reverse_words(sentence):

    reversed_sentence = sentence.split()[::-1]

    return " ".join(reversed_sentence)

print(reverse_words(sentence))

# Task 6. remove_spaces()

# Написать функцию remove_spaces(), которая принимает строку
# и возвращает эту же строку, но без пробелов.
sample_string = " Pyt hon is aw esome "

def remove_spaces(sample_string):

    return sample_string.replace(" ", "")

print(remove_spaces(sample_string))