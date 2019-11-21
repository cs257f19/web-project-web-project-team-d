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
import datasource

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

#No data processing on this page
@app.route('/') #DEFAULT HOMEPAGE
def default():
    return render_template('HomePage.html')

#No data processing on this page.
@app.route('/home') #DEFAULT HOMEPAGE
def home():
    return render_template('HomePage.html')


#No data processing on this page.
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

        ds = datasource.DataSource()
        ds.connect('beckerr2', 'barn787sign')

        if (field1 == "Backer Count" and field2 == "Pledged Amount" and spotlight == "IDC" and staffpick == "IDC"):

            table = []
            table = ds.getBackersAndPledged()

            #newTable = []
            #i=0
            #for row in table:
            #    rowX = [row[0], row[1]
            #    newTable.append(rowX)
            #    i = i+1
            
            bestTable = []
            for row in table:
                for index in row:
                    bestTable.append(index)

                



            return render_template('datapage.html', table=table, field1=field1, field2=field2, newTable = newTable)
    return render_template('datapage.html')




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
