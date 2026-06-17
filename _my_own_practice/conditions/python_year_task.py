"""
PYTHON_YEAR = 1995

1) Якщо рік дорівнює 1995 — вивести "молодець"
2) Якщо різниця між введеним роком і 1995 не більше 10 років — вивести "майже молодець"
3) В іншому випадку — вивести "геть мимо"
"""
user_year = int(input("Enter your choice: ----> "))
pyton_year = 1995
allowed_difference = 10

if user_year == pyton_year:
    print("Ты молодец")

# 1995 < 2006 <= 1995 + 10 ---> 1995 < 2006 <= 2005 ---> True and False = False
# Что такое почти молодец? - год больше 1995 и не больше 1995 + 10
elif pyton_year < user_year <= pyton_year + allowed_difference:
    print("Почти молодец")
else:
    print("Вообще мимо")