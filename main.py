from flask import Flask, request
from translate import translate_text
import logging
import json
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
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
    handle_dialog(response, request.json)
    logging.info(f'Response: {response!r}')
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = 'Привет, какое слово перевести?'
        sessionStorage[user_id] = {
            'first_name': None
        }
        return
    if 'переведи слово' == req['request']['original_utterance'].lower()[:14]:
        res['response']['text'] = translate_text(req['request']['original_utterance'][14:])
    elif 'переведите слово' == req['request']['original_utterance'].lower()[:16]:
        res['response']['text'] = translate_text(req['request']['original_utterance'][16:])
    else:
        res['response']['text'] = 'Не совсем понимаю что вы хотите перевести'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
