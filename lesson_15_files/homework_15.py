import csv
import json
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

from pygments import console


# ==========================
# Task 1 - CSV
# ==========================
# 1. Прочитать два CSV-файла.
# 2. Объединить данные.
# 3. Найти и удалить дубликаты.
# 4. Сохранить результат в result_<your_second_name>.csv
def read_csv(filename):
    data = []

    with open(filename) as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return data


data_1 = read_csv("random_1.csv")
data_2 = read_csv("random_2.csv")

result = data_1 + data_2

unique_rows = []

for row in result:
    if row not in unique_rows:
        unique_rows.append(row)

with open("result_merekha.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(unique_rows)

# ==========================
# Task 2 - JSON
# ==========================
# 1. Проверить все JSON-файлы в папке.
# 2. Определить, какие из них невалидны.
# 3. Записать ошибки в лог-файл json_<your_second_name>.log используя logger.error()
logging.basicConfig(
    filename="json_merekha.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

json_files = Path("json_files").glob("*.json")


def check_json(filename):
    try:
        with open(filename) as json_file:
            json.load(json_file)

        print(f"{filename} - валидный JSON")

    except json.JSONDecodeError as error:
        logger.error(f"{filename}: {error}")


for file in json_files:
    check_json(file)

# ==========================
# Task 3 - XML
# ==========================
# 1. Прочитать groups.xml.
# 2. Найти группу по номеру (group/number).
# 3. Получить значение timingExbytes/incoming.
# 4. Вывести результат через logger.info().
xml_logger = logging.getLogger("xml_logger")
xml_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)
xml_logger.addHandler(console_handler)


def find_incoming_by_group_number(filename, group_number):
    tree = ET.parse(filename)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text

    return None


result = find_incoming_by_group_number(
    "xml_files/groups.xml", 2
)

xml_logger.info(result)
