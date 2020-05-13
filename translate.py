import requests


def translate_text(string):
    return requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200513T040902Z.ef11949d385c6eee.aa537b0a8e95ca3c5cf09f86bb31f597c65be0d1&text='+ string +'&lang=ru-en').json()
