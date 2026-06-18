# HW 9.1. Геометрична фігура "Ромб"
# Створити клас геометричної фігури "Ромб".
# Атрибути:
# - side_a: довжина сторони a
# - angle_a: кут між сторонами a і b
# - angle_b: суміжний з кутом angle_a
# Вимоги:
# 1. side_a повинна бути більше 0.
# 2. angle_a + angle_b повинно дорівнювати 180.
# 3. angle_b обчислюється автоматично.
# 4. Для встановлення значень атрибутів використати __setattr__.
class Rhombus:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):

        if key == "side_a" and value <= 0:
            raise ValueError("side_a should be greater than 0")

        if key == "angle_a" and (value <= 0 or value >= 180):
            raise ValueError("angle_a should be greater than 0 and less than 180")

        if key == "angle_b":
            raise AttributeError("angle_b is calculated automatically")

        super().__setattr__(key, value)

        if key == "angle_a":
            super().__setattr__("angle_b", 180 - value)


# Valid case
rhombus = Rhombus(10, 150)
print(rhombus.side_a)    # 10
print(rhombus.angle_a)   # 150
print(rhombus.angle_b)   # 30

# Change angle_a
rhombus.angle_a = 120
print(rhombus.angle_a)   # 120
print(rhombus.angle_b)   # 60

# Invalid side_a
# Rhombus(0, 90)
# Rhombus(-10, 90)

# Invalid angle_a
# Rhombus(10, 0)
# Rhombus(10, 180)
# Rhombus(10, 200)
# Rhombus(10, -20)

# angle_b manual change should be forbidden
# rhombus.angle_b = 999