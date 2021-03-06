import requests

answer = requests.get(
    "https://geocode-maps.yandex.ru/1.x/?format=json&"
    "apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Барнаул")
if answer:
    json_data = answer.json()
    print(json_data["response"]["GeoObjectCollection"]["featureMember"][0][
        "GeoObject"][
        "metaDataProperty"][
        "GeocoderMetaData"]["Address"]["postal_code"])
else:
    print(answer.reason)
