# Поиск подстрок в строке

test_message = "test passed, test finished"

# in отвечает на вопрос «есть ли подстрока?» и возвращает bool.
contains_test = "test" in test_message
contains_error = "error" in test_message

print("Проверка наличия:")
print(f"Исходная строка: {test_message!r}")
print(f"'test' in test_message  -> {contains_test}")
print(f"'error' in test_message -> {contains_error}")

# find() возвращает индекс первого вхождения или -1.
first_test = test_message.find("test")
missing_error = test_message.find("error")

print("\nПервое вхождение — find():")
print(f"Исходная строка: {test_message!r}")
print(f"test_message.find('test')  -> {first_test}")
print(f"test_message.find('error') -> {missing_error}")

# rfind() возвращает индекс последнего вхождения или -1.
# Индекс отсчитывается от начала строки, даже если поиск идёт справа.
last_test = test_message.rfind("test")
last_error = test_message.rfind("error")

print("\nПоследнее вхождение — rfind():")
print(f"Исходная строка: {test_message!r}")
print(f"test_message.rfind('test')  -> {last_test}")
print(f"test_message.rfind('error') -> {last_error}")

# index() похож на find(), но при отсутствии подстроки вызывает ValueError.
first_passed = test_message.index("passed")

print("\nПоиск через index():")
print(f"Исходная строка: {test_message!r}")
print(f"test_message.index('passed') -> {first_passed}")

try:
    test_message.index("error")
except ValueError as error:
    print(f"test_message.index('error') -> ValueError: {error}")

# count() считает неперекрывающиеся вхождения.
test_count = test_message.count("test")

print("\nПодсчёт вхождений — count():")
print(f"Исходная строка: {test_message!r}")
print(f"test_message.count('test') -> {test_count}")

# startswith() и endswith() возвращают bool.
report_name = "report.pdf"
starts_with_report = report_name.startswith("report")
ends_with_pdf = report_name.endswith(".pdf")
ends_with_text = report_name.endswith(".txt")

print("\nНачало и конец строки:")
print(f"Исходная строка: {report_name!r}")
print(f"report_name.startswith('report') -> {starts_with_report}")
print(f"report_name.endswith('.pdf')     -> {ends_with_pdf}")
print(f"report_name.endswith('.txt')     -> {ends_with_text}")
