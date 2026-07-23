import requests
from pathlib import Path

BASE_URL = "https://images-api.nasa.gov"

SEARCH_URL = f"{BASE_URL}/search"
SEARCH_PARAMS = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20,
}

ASSET_URL_TEMPLATE = f"{BASE_URL}/asset/{{nasa_id}}"


def search_mars_images():
    # Отправляем запрос на поиск изображений и проверяем успешность ответа
    response = requests.get(SEARCH_URL, params=SEARCH_PARAMS)
    response.raise_for_status()

    # Преобразуем JSON-ответ в словарь и получаем список найденных материалов
    search_data = response.json()
    search_items = search_data["collection"]["items"]

    # Из каждого материала достаём nasa_id
    nasa_ids = []

    for item in search_items:
        # data — это список, поэтому берём первый элемент с индексом 0
        nasa_id = item["data"][0]["nasa_id"]
        nasa_ids.append(nasa_id)

    # Для скачивания двух изображений достаточно первых двух идентификаторов
    return nasa_ids[:2]


def get_jpg_url(nasa_id):
    # Подставляем nasa_id в шаблон адреса и запрашиваем список файлов
    asset_url = ASSET_URL_TEMPLATE.format(nasa_id=nasa_id)

    response = requests.get(asset_url)
    response.raise_for_status()

    # Получаем список доступных файлов для выбранного материала
    asset_data = response.json()
    asset_items = asset_data["collection"]["items"]

    # Ищем первый файл с расширением .jpg
    for item in asset_items:
        file_url = item["href"]

        if file_url.lower().endswith(".jpg"):
            return file_url

    # Если JPG-файл не найден, возвращаем None
    return None


def download_image(image_url, filename):
    # Скачиваем бинарное содержимое изображения и проверяем успешность ответа
    response = requests.get(image_url)
    response.raise_for_status()

    # Сохраняем полученные байты в локальный JPG-файл
    with open(filename, "wb") as image_file:
        image_file.write(response.content)


def main():
    # Получаем два идентификатора изображений из результатов поиска
    nasa_ids = search_mars_images()
    # Определяем папку текущего файла, чтобы сохранять изображения рядом с кодом
    current_directory = Path(__file__).parent

    # Нумеруем два изображения, начиная с единицы
    for image_number, nasa_id in enumerate(nasa_ids, start=1):
        jpg_url = get_jpg_url(nasa_id)

        # Скачиваем файл только в том случае, если JPG-ссылка была найдена
        if jpg_url:
            filename = current_directory / f"mars_photo{image_number}.jpg"
            download_image(jpg_url, filename)


if __name__ == "__main__":
    main()
