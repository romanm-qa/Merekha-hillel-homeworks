# 5, 12, 23, 29 — ASCII, максимальная цифра, палиндром, число прописью

# ==========================================
# Задача 5. Проверка ASCII-кода
# ==========================================
# Дано целое число, обозначающее ASCII-код символа.
# Определить, соответствует ли код английской букве.
# Вернуть True, если это английская буква, иначе False.

def is_english_letter(code):
    if code in range(65, 90 + 1) or code in range(97, 122 + 1):
        return True
    else:
        return False


print("=" * 50)
print("Задача 5. Проверка ASCII-кода")
print("=" * 50)

print(f"code=65 ('A') → {is_english_letter(65)!r}")
print(f"code=90 ('Z') → {is_english_letter(90)!r}")
print(f"code=97 ('a') → {is_english_letter(97)!r}")
print(f"code=122 ('z') → {is_english_letter(122)!r}")
print(f"code=64 ('@') → {is_english_letter(64)!r}")
print(f"code=48 ('0') → {is_english_letter(48)!r}")
print(f"code=123 ('{{') → {is_english_letter(123)!r}")
print()


# ==========================================
# Задача 12. Максимальная цифра числа
# ==========================================
# Дано вещественное число.
# Найти максимальную цифру этого числа.
# Пример: 56.457 → 7.

def find_max_digit(number):
    max_digit = 0

    for digit in str(number):
        if digit.isdigit():
            if int(digit) > max_digit:
                max_digit = int(digit)

    return max_digit


print("=" * 50)
print("Задача 12. Максимальная цифра числа")
print("=" * 50)

print(f"number=56.457 → {find_max_digit(56.457)!r}")
print(f"number=123.456 → {find_max_digit(123.456)!r}")
print(f"number=908.12 → {find_max_digit(908.12)!r}")
print(f"number=111.11 → {find_max_digit(111.11)!r}")
print(f"number=0.25 → {find_max_digit(0.25)!r}")
print(f"number=-78.32 → {find_max_digit(-78.32)!r}")
print(f"number=0.0 → {find_max_digit(0.0)!r}")
print()


# ==========================================
# Задача 23. Проверка палиндрома
# ==========================================
# Дано слово.
# Проверить, одинаково ли оно читается
# слева направо и справа налево.
# Вернуть True, если палиндром, иначе False.

def is_palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False


print("=" * 50)
print("Задача 23. Проверка палиндрома")
print("=" * 50)

print(f"word='radar' → {is_palindrome('radar')!r}")
print(f"word='level' → {is_palindrome('level')!r}")
print(f"word='madam' → {is_palindrome('madam')!r}")
print(f"word='python' → {is_palindrome('python')!r}")
print(f"word='hello' → {is_palindrome('hello')!r}")
print(f"word='a' → {is_palindrome('a')!r}")
print(f"word='' → {is_palindrome('')!r}")
print()


# ==========================================
# Задача 29. Перевод числа в текст
# ==========================================
# Дано целое число от 1 до 999.
# Вернуть число прописью.
# Пример: 123 → "сто двадцать три".

def number_to_words(number):
    if not isinstance(number, int) or not 1 <= number <= 999:
        raise ValueError("Число должно быть целым от 1 до 999")

    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
    }
    teens = {
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать",
    }
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
    }
    hundreds = {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот",
    }

    hundreds_digit = number // 100
    tens_digit = (number // 10) % 10
    units_digit = number % 10
    last_two_digits = number % 100

    words = []

    if hundreds_digit > 0:
        words.append(hundreds[hundreds_digit])

    if last_two_digits in range(10, 20):
        words.append(teens[last_two_digits])

    else:
        if tens_digit >= 2:
            words.append(tens[tens_digit])

        if units_digit > 0:
            words.append(units[units_digit])

    return " ".join(words)


print("=" * 50)
print("Задача 29. Перевод числа в текст")
print("=" * 50)

print(f"number=1 → {number_to_words(1)!r}")
print(f"number=9 → {number_to_words(9)!r}")
print(f"number=10 → {number_to_words(10)!r}")
print(f"number=19 → {number_to_words(19)!r}")
print(f"number=20 → {number_to_words(20)!r}")
print(f"number=42 → {number_to_words(42)!r}")
print(f"number=100 → {number_to_words(100)!r}")
print(f"number=105 → {number_to_words(105)!r}")
print(f"number=115 → {number_to_words(115)!r}")
print(f"number=456 → {number_to_words(456)!r}")
print(f"number=999 → {number_to_words(999)!r}")
print()
