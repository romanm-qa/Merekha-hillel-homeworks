# ==========================================
# Python Fundamentals
# Topic: Comparison Operators
# ==========================================

a = 10
b = 5

# Greater than (>)

print("a > b:", a > b)

# Less than (<)

print("a < b:", a < b)

# Greater than or equal (>=)

print("a >= b:", a >= b)

# Less than or equal (<=)

print("a <= b:", a <= b)

# Not equal (!=)

print("a != b:", a != b)

# Equal (==)

print("a == b:", a == b)

# ==========================================
# Equality vs Identity
# ==========================================

var1 = "hello world"
var2 = var1

print(var1 == var2)
print(var1 is var2)

# ==========================================
# == vs is
# ==========================================

string1 = "Python"
string2 = "Python"

print(string1 == string2)  # True
print(string1 is string2)  # Может быть True

print()

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # True
print(list1 is list2)  # False