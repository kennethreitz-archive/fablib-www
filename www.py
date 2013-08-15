# -*- coding: utf-8 -*-

import os

import requests
from markdown2 import markdown
from flask import Flask, request, render_template

API_URL = os.environ['API_URL']

app = Flask(__name__)
app.debug = True
s = requests.session()

@app.route('/')
def hello():
    return render_template('index.html', text=markdown('yo.\n\n# bro'))

@app.route('/<string:profile>')
def get_profile(profile):
    url = '{}/{}/{}'.format(API_URL, profile, document)
    r = s.get(url)
    return render_template('index.html', text=markdown(r.content))

@app.route('/<string:profile>/<path:document>')
def get_document(profile, document):
    url = '{}/render/{}/{}'.format(API_URL, profile, document)
    r = s.get(url)
    return render_template('index.html', text=markdown(r.content))

if __name__ == '__main__':
    app.run()