from pathlib import Path

# __file__ — это путь к текущему Python-файлу
print(__file__)

# Path(__file__) превращает строку с путём в объект Path
current_file = Path(__file__)
print(current_file)

# .parent берёт папку, в которой лежит текущий файл
# BASE_DIR = базовая папка проекта
BASE_DIR = current_file.parent
print(BASE_DIR)

# Создаем путь к файлу users.txt
users_file = BASE_DIR / "users.txt"
print(users_file) 