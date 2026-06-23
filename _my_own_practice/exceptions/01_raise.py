"""
Exceptions (исключения) — это ошибки, которые возникают во время выполнения программы.
Они помогают:
- не завершать программу аварийно;
- обрабатывать ошибки и показывать понятные сообщения;
- контролировать некорректные данные от пользователя.
raise — ключевое слово, которое позволяет вручную вызвать исключение.
Используется, когда данные не соответствуют нашим требованиям
или выполнение программы нужно остановить.
Примеры встроенных исключений:
- ValueError
- TypeError
- AttributeError
- ZeroDivisionError
- IndexError
- KeyError
"""
'''
1) length of password >=8
2) 2 uppercase letters
3) one of special characters (?!.,:)
param: password (str)
return: None or raise ValueError
'''
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

    SPEC_CHARS = "?!.,:"

    count_upper_chars = 0
    exists_special_chars = False

    for element in password:
        if element in SPEC_CHARS:
            exists_special_chars = True
        if 'A' <= element <= 'Z':
            count_upper_chars += 1

    if count_upper_chars < 2:
        raise ValueError("Password must be at least 2 uppercase letters")
    if not exists_special_chars:
        raise ValueError("Password must contain at least one special character")

validate_password("qwertnnmkmpmpm!kmJUkmy")
