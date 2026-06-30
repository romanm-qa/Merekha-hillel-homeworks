# В Python любое ненулевое число считается True.
# Поэтому while x эквивалентно while x != 0.

x = 5

while x:
    print(x)
    x -= 1

print("x =", x)

# while x:
# Пока x не равен 0, условие считается True.
#
# while x != 0:
# Делает то же самое, но запись более явная.
#
# Оба варианта работают одинаково.

print(bool(10))   # True
print(bool(1))    # True
print(bool(-5))   # True
print(bool(0))    # False