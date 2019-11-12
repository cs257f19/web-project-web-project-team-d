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

        spotlight = request.form["SL"]
        staffpick = request.form["SP"]
        return "wow..!!!!!"
    return render_template('datapage.html')

'''
        

        ds = datasource.DataSource()

        if (field1 == "backerCount" and field2 == "pledgedAmount"):
            
            table = ds.getBackersAndPledged()'''

            
            #Call getBackersAndPledged which returns a list of tuples with backeramount/pledged amount
            #Display list in a table?   [HANDLED]


            

        # return render_template('datapage.html', field1=field1, field2=field2, staffpick=staffpick, spotlight=spotlight)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
