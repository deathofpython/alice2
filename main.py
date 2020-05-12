from flask import Flask, request
import logging
import json
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

k = 0
obj = ['Слона', 'Кролика']

sessionStorage = {}


@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(request.json, response)

    logging.info(f'Response:  {response!r}')

    return json.dumps(response)


def handle_dialog(req, res):
    global k
    user_id = req['session']['user_id']

    if req['session']['new']:
        sessionStorage[user_id] = {
            'suggests': [
                "Не хочу.",
                "Не буду.",
                "Отстань!",
            ]
        }
        res['response']['text'] = 'Привет! Купи ' + obj[k].lower() + '!'
        res['response']['buttons'] = get_suggests(user_id)
        return
    if any(i in req['request']['original_utterance'].lower() for i in ['ладно', 'куплю', 'покупаю',
                                                                       'хорошо', 'я покупаю', 'я куплю']):
        res['response']['text'] = obj[k] + ' можно найти на Яндекс.Маркете!'
        if k == 0:
            k = 1
            res['response']['text'] += '\nА теперь купи ' + obj[k] + '!'
        else:
            k = 0
            res['response']['end_session'] = True
        return

    res['response']['text'] = \
        f"Все говорят '{req['request']['original_utterance']}', а ты купи {obj[k]}!"
    res['response']['buttons'] = get_suggests(user_id)


def get_suggests(user_id):
    session = sessionStorage[user_id]
    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text=" + obj[k][:-1],
            "hide": True
        })

    return suggests


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
