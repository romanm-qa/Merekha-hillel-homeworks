# Множественное наследование (Multiple Inheritance)
# Класс может наследоваться сразу от нескольких родителей.
# В таком случае дочерний класс получает доступ
# к атрибутам и методам всех родительских классов.

class Bird:

    def fly(self):
        print("I am flying")


class Horse:

    def run(self):
        print("I am running")

# Pegasus наследует методы и Bird, и Horse.
class Pegasus(Horse, Bird):
    pass

pegasus = Pegasus()

pegasus.run()
pegasus.fly()