# Array наследуется от встроенного list.
# Мы переопределяем методы append(), extend() и insert(),
# чтобы разрешать хранить только элементы указанного типа.
# Перед добавлением элемента выполняется проверка через isinstance().
# Если тип неверный — выбрасывается ошибка.
# После проверки вызывается оригинальный метод list через super().

class Array(list):

    def __init__(self, element_type):
        super().__init__()
        self.element_type = element_type

    def check_type(self, item):
        if not isinstance(item, self.element_type):
            raise ValueError(f"Element type must be {self.element_type}")

    def append(self, item):
        self.check_type(item)
        super().append(item)

    def extend(self, items):
        for item in items:
            self.check_type(item)
        super().extend(items)

    def insert(self, index, item):
        self.check_type(item)
        super().insert(index, item)


int_array = Array(int)

int_array.append(1)
int_array.append(2)
int_array.append(3)

int_array.extend([4, 5, 6])

int_array.insert(2, 2)

#int_array.append("Hello World")

print(int_array)
