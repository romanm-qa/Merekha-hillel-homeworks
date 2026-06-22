# Создаем класс Cat.
# У каждого кота будет имя и метод sound().
class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some sound"

# Простое наследование. Cat наследует все атрибуты и методы класса Animal.
class Cat(Animal):

    def __init__(self, name, age):

        # У Cat появился свой __init__ из-за нового атрибута age.
        # Поэтому вызываем конструктор родителя через super(),
        # чтобы не потерять создание атрибута name.
        super().__init__(name)
        # Добавляем новый атрибут только для Cat.
        self.age = age

    # Переопределяем метод родителя. Без этого метода вывод был бы: Some sound
    def sound(self):
        return ("Meow")

cat = Cat("Barsik", 3)

print(f"Кота зовут {cat.name} и ему {cat.age} года")
print(f"Он делает {cat.sound()}")

animal = Animal("Неизвестный зверь")

print(f"{animal.name} издал {animal.sound()}")

class Dog(Animal):

    def sound(self):
        return "Woof"

dog = Dog("Sharik")

print(f"Собаку зовут {dog.name} и он издает звук {dog.sound()}")

# Множественное наследование.
# CatDog наследует и Cat, и Dog.
class CatDog(Cat, Dog):
    pass

# При создании объекта будет использован __init__ из Cat, потому что Cat указан первым в списке наследования.
cat_dog = CatDog("Tom", 5)

print(cat_dog.name) # Атрибут name получен через Cat -> Animal
print(cat_dog.age) # Атрибут age добавлен в классе Cat
# Метод sound() также будет взят из Cat, потому что Cat ищется раньше Dog.
print(cat_dog.sound())