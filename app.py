# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

# import os
import json
from flask import Flask, request


app = Flask(__name__)
# web_hook_secret_key = os.environ.get('WEBHOOK_SECRET_KEY')


@app.route("/", methods=['POST'])
def hello():
    print(json.loads(request.data))
    return "Hello World!"


if __name__ == "__main__":
    app.run()
