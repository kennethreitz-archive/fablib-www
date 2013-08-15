# -*- coding: utf-8 -*-

import os

import requests
from flask import Flask

API_URL = os.environ['API_URL']

app = Flask(__name__)
app.debug = True
s = requests.session()

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<string:profile>/')
def get_profile(profile):
    return 'Hello World!'

@app.route('/<string:profile>/<path:document>/')
def get_document(profile, document):
    url = '{}/{}/{}'.format(API_URL, profile, document)
    r = s.get(url)
    return r.content

if __name__ == '__main__':
    app.run()