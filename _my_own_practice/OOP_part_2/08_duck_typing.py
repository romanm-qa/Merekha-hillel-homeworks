# Duck Typing (утиная типизация)
# Если объект выглядит как утка, плавает как утка и крякает как утка, значит это утка.
# Python обычно не интересует тип объекта. Его интересует:
# "Есть ли у объекта нужный метод?"
# То есть Python смотрит на поведение объекта, а не на его класс.

class Duck:

    def sound(self):
        print("Quack")


class Dog:

    def sound(self):
        print("Woof")


def make_sound(animal):
    animal.sound()


duck = Duck()
dog = Dog()

make_sound(duck)
make_sound(dog)