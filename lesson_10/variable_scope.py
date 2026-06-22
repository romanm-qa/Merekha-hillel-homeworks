# Variable Scope
# Область видимости переменных в Python.
# Переменные могут быть глобальными (доступны во всем файле)
# и локальными (доступны только внутри функции).

name = "Roman"  # глобальная переменная

def greeting():
    name = "Alex"  # локальная переменная
    print(name)

greeting()
print(name)
# Результат:
# Alex  -> локальная переменная внутри функции
# Roman -> глобальная переменная не изменилась

# Пример использования global

user_name = "Roman"  # глобальная переменная

def change_name():
    global user_name

    # Изменяем глобальную переменную
    user_name = "Alex"

    print(f"Inside function: {user_name}")

change_name()

print(f"Outside function: {user_name}")

# Результат:
# Inside function: Alex
# Outside function: Alex

# Пример области видимости Enclosing (внешняя функция)
def create_username():
    user_name = "Borya"

    def add_suffix():
        # Здесь нет своей переменной user_name,
        # поэтому Python берет ее из внешней функции create_username()
        return user_name + "_qa"

    print(add_suffix())

create_username()
# Результат:
# Roman_qa