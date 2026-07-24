import requests

# Загружаем изображение на сервер с помощью POST-запроса
upload_url = "http://127.0.0.1:8080/upload"

with open("mars_photo1.jpg", "rb") as image_file:
    files = {"image": image_file}
    response = requests.post(upload_url, files=files)

print("POST status code:", response.status_code)
print("POST response:", response.json())

# Получаем URL загруженного изображения с помощью GET-запроса
get_url = "http://127.0.0.1:8080/image/mars_photo1.jpg"
headers = {"Content-Type": "text"}

get_response = requests.get(get_url, headers=headers)

print("GET status code:", get_response.status_code)
print("GET response:", get_response.json())

# Удаляем загруженное изображение с помощью DELETE-запроса
delete_url = "http://127.0.0.1:8080/delete/mars_photo1.jpg"

delete_response = requests.delete(delete_url)

print("DELETE status code:", delete_response.status_code)
print("DELETE response:", delete_response.json())
