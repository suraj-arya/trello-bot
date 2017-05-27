# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

import os
import json

from flask import Flask, request

from .change_list import change_list


app = Flask(__name__)
# web_hook_secret_key = os.environ.get('WEBHOOK_SECRET_KEY')


@app.route("/", methods=['GET'])
def hello():
    return 'Hello world!'


@app.route("/", methods=['POST'])
def index():
    data = json.loads(request.data)
    header = request.headers.get('X-GitHub-Event', '').strip()
    print(data)

    if header != 'pull_request':
        return 'NOOP'

    action = data.get('action')
    move_to = None
    if action == 'open':
        move_to = os.environ.get('UNDER_REVIEW_LIST_ID')

    elif action == 'closed':
        merged = data['pull_request'].get('merged', False)
        if merged:
            move_to = os.environ.get('MERGED_LIST_ID')
    else:
        return 'NOOP'

    title = data['pull_request']['title']
    body = data['pull_request']['body']

    tokens = '{} {}'.format(title, body).split()
    card_id = None
    try:
        for token in tokens:
            if 'TRELLO' in token.upper():
                card_id = token.split(':')[-1].strip()
    except Exception as e:
        print(e.message)
        return '', 500

    if None not in (card_id, move_to):
        try:
            change_list(card_id, move_to)
        except Exception as e:
            print(e.message)
            return '', 500

    return "Hello World!"


if __name__ == "__main__":
    app.run()
