# Instance Attributes (атрибуты объекта)

# Атрибуты объекта принадлежат конкретному объекту.
# Каждый объект может иметь свои собственные значения.

class Human:
    pass

# Создаем объекты
alex = Human()
john = Human()

# Создаем атрибуты для объекта alex
alex.name = "Alex"
alex.age = 30

# Создаем атрибуты для объекта john
john.name = "John"
john.age = 36

print(f"{alex.name} is {alex.age} years old")
print(f"{john.name} is {john.age} years old")

# Важно:
# Такой способ используется только для понимания того, как работают атрибуты объекта.
# alex.name = "Alex"
# alex.age = 30

# john.name = "John"
# john.age = 36

# В реальных проектах так обычно не делают, потому что легко забыть создать какой-либо атрибут.