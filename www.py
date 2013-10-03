# -*- coding: utf-8 -*-

import os

import requests
from markdown2 import markdown
from flask import Flask, request, render_template, redirect, session, g

API_URL = os.environ['API_URL']

app = Flask(__name__)
app.debug = True
app.secret_key = 'phoiwafhipowhfopwhofe'

requests = requests.session()

@app.route('/')
def hello():
    return render_template('index.html', text=markdown('# Fallib: Documentation for Humans. \n## Users \n\n- [kennethreitz](/kennethreitz)'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'PUT'])
def login_post():
    session['username'] = request.form['username']
    session['password'] = request.form['password']

    return render_template('login.html', user=session['username'])


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST', 'PUT'])
def signup_post():

    username = request.form['username']
    password = request.form['password']

    url = '{}/signup'.format(API_URL)
    data = {'username': username, 'password': password}

    r = requests.post(url, data=data)

    if r.ok:
        session['username'] = username
        session['password'] = password

    return login_post()

@app.route('/<path:document>')
def get_document(document):

    profile = False

    # strip
    split = document.split('/')
    if len(split) == 1:
        # Profile without a slash.
        return redirect('{}/'.format(document))

    if not split[1]:
        # This is a proper profile URL.
        document = split[0]
        profile = True

    api_url = '{}/{}'.format(API_URL, document)
    html_url = '{}/{}/html'.format(API_URL, document)

    api = requests.get(api_url)
    html = requests.get(html_url)

    payload = {}
    payload['doc'] = api.json()[u'document']
    payload['doc']['html'] = html.text
    payload['path'] = document
    payload['profile'] = profile

    return render_template('document.html', **payload), api.status_code

@app.route('/content/<path:document>')
def get_content(document):
    url = '{}/content/{}/text'.format(API_URL, document)
    r = requests.get(url)
    return render_template('index.html', text=r.text)

if __name__ == '__main__':
    app.run()