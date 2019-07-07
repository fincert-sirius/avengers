# Функция принимает аргументы DOMAIN(имя домена(можно без http), FROM((точно работает в годах)начало временного промежутка,
# которгого ведется поиск), TO(конец промежутка)
# Вывод в json-файле типа [['timestamp','original_url','html_length'], [...],[...], ...]

import requests

domain_name = 'sberbank.ru'
from_date = 2017
to_date = 2019


def web_archive(DOMAIN, FROM, TO):
    # Готовим запрос.
    # Ключи web archive: [["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
    web_request = "https://web.archive.org/cdx/search/cdx?url=*.{}/*&output=json&from={}&to={}&fl=timestamp,original,length".format(
        DOMAIN, str(FROM), str(TO))
    response = None
    try:
        response = requests.get(web_request)

        if response:
            json_response = response.json()
            return json_response
        else:
            return "Ошибка выполнения запроса:\n", "Http статус:", response.status_code, "(", response.reason, ")"

    except:
        return "Запрос не удалось выполнить. Проверьте подключение к сети Интернет."


print(web_archive(domain_name, from_date, to_date))
