# Методы изменения регистра строк
# Они возвращают результат; исходная строка не меняется.

mixed_case = "pYtHoN testing"

lowercase = mixed_case.lower()  # Все буквы в нижнем регистре
uppercase = mixed_case.upper()  # Все буквы в верхнем регистре
capitalized = mixed_case.capitalize()  # Первая буква заглавная, остальные строчные
titled = mixed_case.title()  # Каждое слово начинается с заглавной буквы
swapped = mixed_case.swapcase()  # Поменять регистр каждой буквы

print("Методы изменения регистра:")
print(f"Исходная строка:      {mixed_case!r}")
print(f"mixed_case.lower():   {lowercase!r}")
print(f"mixed_case.upper():   {uppercase!r}")
print(f"mixed_case.capitalize(): {capitalized!r}")
print(f"mixed_case.title():      {titled!r}")
print(f"mixed_case.swapcase():   {swapped!r}")
print(f"После вызовов методов:   {mixed_case!r}")

# Если результат не присвоить, он не сохранится в переменной.
word = "Python"
word.lower()

print("\nНеизменяемость строки:")
print(f"word после word.lower(): {word!r}")

lowered_word = word.lower()
print(f"lowered_word: {lowered_word!r}")
print(f"word по-прежнему: {word!r}")

# Для сравнения Unicode-текста без учёта регистра пригодится casefold().
german_word = "Straße"
comparison_word = "STRASSE"
same_ignoring_case = german_word.casefold() == comparison_word.casefold()

print("\nСравнение без учёта регистра:")
print(f"Строки: {german_word!r} и {comparison_word!r}")
print(f"lower():    {german_word.lower() == comparison_word.lower()}")
print(f"casefold(): {same_ignoring_case}")
