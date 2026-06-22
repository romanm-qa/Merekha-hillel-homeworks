# MRO (Method Resolution Order)
# MRO — это порядок, в котором Python ищет методы и атрибуты.
# Если метода нет в текущем классе, Python идет выше по цепочке наследования.
# При множественном наследовании порядок родителей очень важен.
class A:

    def method(self):
        print("A method")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()

# Python ищет method() в таком порядке:
# D -> B -> C -> A -> object
print(D.mro())

# В D, B и C метода method() нет.
# Поэтому Python дойдет до A и вызовет A.method().
d.method()

print("-" * 30)

# Кейс 2.
# Теперь метод есть в B.
# Python остановится на B и до A уже не пойдет.

class A2:

    def method(self):
        print("A2 method")

class B2(A2):

    def method(self):
        print("B2 method")

class C2(A2):
    pass

class D2(B2, C2):
    pass

d2 = D2()

# Порядок поиска:
# D2 -> B2 -> C2 -> A2 -> object
print(D2.mro())

# Python найдет method() в B2 и сразу выполнит его.
d2.method()

print("-" * 30)

# Кейс 3.
# Теперь метод есть в C.
# В B метода нет, поэтому Python пойдет дальше в C.

class A3:

    def method(self):
        print("A3 method")

class B3(A3):
    pass

class C3(A3):

    def method(self):
        print("C3 method")

class D3(B3, C3):
    pass

d3 = D3()

# Порядок поиска:
# D3 -> B3 -> C3 -> A3 -> object
print(D3.mro())

# В D3 метода нет.
# В B3 метода нет.
# В C3 метод есть, поэтому выполнится C3.method().
d3.method()

print("-" * 30)

# Кейс 4.
# Меняем порядок родителей: D4(C4, B4)
# Теперь Python сначала пойдет в C4, а потом в B4.

class A4:

    def method(self):
        print("A4 method")

class B4(A4):

    def method(self):
        print("B4 method")

class C4(A4):

    def method(self):
        print("C4 method")

class D4(C4, B4):
    pass

d4 = D4()

# Порядок поиска:
# D4 -> C4 -> B4 -> A4 -> object
print(D4.mro())

# Так как первым родителем указан C4,
# Python найдет method() именно в C4.
d4.method()