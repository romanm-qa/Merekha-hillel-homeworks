# Импортируем функцию login из файла auth.py
from auth import login

def test_login_success():
    actual_result = login("roman@test.com", "123456")
    expected_result = "Login Successful"

    assert actual_result == expected_result

def test_login_wrong_password():
    actual_result = login("roman@test.com", "12345")
    expected_result = "Email or Password Incorrect"

    assert actual_result == expected_result

def test_login_wrong_email():
    actual_result = login("roman@@test.com", "123456")
    expected_result = "Email or Password Incorrect"

    assert actual_result == expected_result

def test_login_wrong_email_and_password():
    actual_result = login("roma3n@test.com", "12345")
    expected_result = "Email or Password Incorrect"

    assert actual_result == expected_result


