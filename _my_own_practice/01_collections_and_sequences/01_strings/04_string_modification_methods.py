# Методы обработки строк возвращают результат, исходная строка не меняется.

# replace(old, new, count): замена подстроки; count ограничивает число замен.
message = "I love Python"
replaced_word = message.replace("Python", "QA")
replaced_all = message.replace("o", "0")
replaced_once = message.replace("o", "0", 1)

print("Замена — replace():")
print(f"Исходная строка: {message!r}")
print(f"Заменить 'Python' на 'QA': {replaced_word!r}")
print(f"Заменить все 'o' на '0': {replaced_all!r}")
print(f"Заменить одну 'o' на '0': {replaced_once!r}")
print(f"После замен исходная строка: {message!r}")

# split() без аргумента разбивает по группам любых пробельных символов.
# split(',') использует точный разделитель — запятую.
spaced_languages = " Python   Java\tGo "
comma_languages = "Python,Java,Go"
split_on_whitespace = spaced_languages.split()
split_on_commas = comma_languages.split(",")

print("\nРазделение — split():")
print(f"Исходная строка: {spaced_languages!r}")
print(f"spaced_languages.split() -> {split_on_whitespace!r}")
print(f"Исходная строка: {comma_languages!r}")
print(f"comma_languages.split(',') -> {split_on_commas!r}")
print(f"Тип результата split(): {type(split_on_commas).__name__}")

# Явный разделитель ' ' сохраняет пустой элемент между двумя пробелами.
print(f"'a  b'.split(' ') -> {'a  b'.split(' ')!r}")

# join() вызывается у разделителя; все элементы должны быть строками.
joined_languages = " | ".join(split_on_commas)

print("\nОбъединение — join():")
print(f"Исходный список: {split_on_commas!r}")
print(f"' | '.join(split_on_commas) -> {joined_languages!r}")

# strip() удаляет пробельные символы только по краям.
# lstrip() удаляет их слева, rstrip() — справа.
padded_text = " \tHello World\n "
trimmed_both = padded_text.strip()
trimmed_left = padded_text.lstrip()
trimmed_right = padded_text.rstrip()

print("\nОчистка краёв:")
print(f"Исходная строка: {padded_text!r}")
print(f"padded_text.strip()  -> {trimmed_both!r}")
print(f"padded_text.lstrip() -> {trimmed_left!r}")
print(f"padded_text.rstrip() -> {trimmed_right!r}")

# Аргумент strip() — набор символов, а не точная подстрока.
decorated_name = "___Roman___"
clean_name = decorated_name.strip("_")
print(f"Исходная строка: {decorated_name!r}")
print(f"decorated_name.strip('_') -> {clean_name!r}")
print(f"'www.example.com'.strip('w.com') -> {'www.example.com'.strip('w.com')!r}")

# Для точного префикса или суффикса есть отдельные методы.
tagged_user = "test_user"
report_name = "report.json"
user_without_prefix = tagged_user.removeprefix("test_")
report_without_suffix = report_name.removesuffix(".json")

print("\nУдаление точного префикса и суффикса:")
print(f"Исходная строка: {tagged_user!r}")
print(f"tagged_user.removeprefix('test_') -> {user_without_prefix!r}")
print(f"Исходная строка: {report_name!r}")
print(f"report_name.removesuffix('.json') -> {report_without_suffix!r}")
