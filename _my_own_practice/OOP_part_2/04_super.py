# super()
# super() позволяет обратиться к родительскому классу.
# Чаще всего используется для:
# - вызова родительского __init__()
# - вызова переопределенного метода родителя
# super() не означает "родительский класс".
# На самом деле super() идет к следующему классу согласно MRO (Method Resolution Order).
# Поэтому super() особенно важен при множественном наследовании.

class Product:

    def __init__(self, price, art, percent_sale = 0, is_sale = False):
        self.price = price
        self.art = art
        self.percent_sale = percent_sale
        self.is_sale = is_sale

    def print_info(self):
        print(
            f"Price is {self.get_price()}\n"
            f"Art is {self.art}\n"
            f"Is sale ---> {self.is_sale}"
        )

    def get_price(self):
        if not self.is_sale:
            return self.price
        return self.price * (1 - self.percent_sale / 100)

class Phone(Product):

    def __init__(self, color, model, brand, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.model = model
        self.brand = brand

    def print_info(self):
        super().print_info()
        print(
            f"Color: {self.color}\n"
            f"Model: {self.model}\n"
            f"Brand: {self.brand}\n"
        )

base_product = Product(price=100, art="Hello World!", percent_sale=10)
phone = Phone("White", model="X", brand="Apple", price=100, is_sale=True,
              percent_sale=40, art="some phone")

base_product.print_info()
print("*" * 20)
phone.print_info()