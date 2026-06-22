# issubclass() -> проверяет класс

print(issubclass(bool, int))      # True
print(issubclass(float, int))     # False
print(issubclass(int, float))     # False
print(issubclass(complex, object)) # True

class Base:
    pass

class Child(Base):
    pass

print(issubclass(Child, Base))    # True
print(issubclass(Base, object))   # True
print(issubclass(Child, object))  # True
print(issubclass(Base, Child))    # False

# Пример для сравнения с isinstance()

child = Child()

print(isinstance(child, Child))   # True
print(isinstance(child, Base))    # True

print(issubclass(Child, Base))    # True