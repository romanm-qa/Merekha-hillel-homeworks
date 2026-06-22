# isinstance()
# Проверяет, является ли объект экземпляром указанного класса.
# Возвращает:
# True  - если объект принадлежит этому классу
# False - если не принадлежит

print(isinstance(8, int))          # True
print(isinstance("str", int))      # False

print(isinstance(True, bool))      # True
print(isinstance(True, int))       # True (!)

print(isinstance("a string", object))  # True
print(isinstance(None, object))        # True

print(isinstance("False", str))    # True