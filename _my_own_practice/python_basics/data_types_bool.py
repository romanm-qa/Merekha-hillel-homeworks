# ==========================================
# Python Fundamentals
# Topic: Data Types — bool
# ==========================================

# Boolean (bool) имеет только два значения:
# True  - истина
# False - ложь

is_student = True
is_employed = False

print("is_student:", is_student, type(is_student))
print("is_employed:", is_employed, type(is_employed))

print()

# ==========================================
# Comparison operators
# ==========================================

print(10 > 5)      # True
print(10 < 5)      # False
print(10 == 10)    # True
print(10 != 10)    # False
print(10 >= 10)    # True
print(10 <= 5)     # False

print()

# ==========================================
# Bool from values
# ==========================================

print(bool(1))       # True
print(bool(100))     # True

print(bool(0))       # False

print(bool("Hello")) # True
print(bool(""))      # False

print(bool([1, 2]))  # True
print(bool([]))      # False

print()

# ==========================================
# Real QA examples
# ==========================================

user_is_logged_in = True
course_completed = False

print("User is logged in:", user_is_logged_in)
print("Course completed:", course_completed)

# Fun fact
print(True + True)     # 2
print(True + False)    # 1
print(False + False)   # 0