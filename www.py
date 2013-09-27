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
    return render_template('index.html', text=markdown('# Fallib: Documentation for Humans. \n## Users \n\n- [kennethreitz](/kennethreitz)'))

@app.route('/')
def login():
    return render_template('index.html', text=markdown('# Fallib\n\n## Document ALL the Things!'))

@app.route('/<path:document>/')
def get_document(document):
    url = '{}/{}/html'.format(API_URL, document)
    r = s.get(url)
    return render_template('index.html', text=r.text), r.status_code

@app.route('/content/<path:document>')
def get_content(document):
    url = '{}/content/{}/text'.format(API_URL, document)
    r = s.get(url)
    return render_template('index.html', text=r.text)

if __name__ == '__main__':
    app.run()