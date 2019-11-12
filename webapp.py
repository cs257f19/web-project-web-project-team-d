#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016
    Modified by Eric Alexander, January 2017

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import flask
from flask import render_template, request, redirect
import json
import sys

app = flask.Flask(__name__)

@app.route('/') #DEFAULT HOMEPAGE
def home():
    return render_template('HomePage.html')


@app.route('/about/') #ABOUT
def about():
    return render_template('aboutpage.html')


@app.route('/comparison/' , methods=['POST' , 'GET']) #COMPARISON, do stuff.
def defaultComparison():
    
    if request.method == 'POST':
        field1 = request.form["DV1"]
        field2 = request.form["DV2"]
        staffpick = request.form["staffPick"]
        spotlight = request.form["spotlight"]

    return render_template('datapage.html')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
