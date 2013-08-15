# -*- coding: utf-8 -*-

import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<string:profile>/')
def get_profile():
    return 'Hello World!'

@app.route('/<string:profile>/<path:document>/')
def get_profile():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()