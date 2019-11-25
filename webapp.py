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
        if(spotlight == "True"):
            spot = "t"
        elif(spotlight == "False"):
            spot = "f"
        else:
            spot = ""
            
        if(staffpick == "True"):
            staff = "t"
        elif(staffpick == "False"):
            staff = "f"
        else:
            staff = ""

        if (field1 == "Backer Count" and field2 == "Pledged Amount"):
            
            table = []
            table = ds.getBackersAndPledged(spot, staff)

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                pledged = ds.convertCurrency(row[1], currency)
                rowX = [row[0], pledged]
                newTable.append(rowX)
                i = i+1

            newtable_json = json.dumps(newTable)

            return render_template('datapage.html', table=table, field1=field1, field2=field2, newTable = newtable_json)
        elif (field1 == "Backer Count" and field2 == "Goal" and spotlight == "IDC" and staffpick == "IDC"):
            table = []
            table = ds.getBackersAndGoal(spot, staff)

            newTable = []
            i=0
            for row in table:
                goal = row[2]
                goal = ds.convertCurrency(row[1], goal)
                rowX = [row[0], goal]
                newTable.append(rowX)
                i = i+1

            newtable_json = json.dumps(newTable)

            return render_template('datapage.html', table=table, field1=field1, field2=field2, newTable = newtable_json)
    return render_template('datapage.html')


@app.route('/comparison/table' , methods=['POST' , 'GET']) #COMPARISON, do stuff.
def tableComparison():

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

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                pledged = ds.convertCurrency(row[1], currency)
                rowX = [row[0], pledged]
                newTable.append(rowX)
                i = i+1

            bestTable = []
            for row in table:
                for index in row:
                    bestTable.append(index)



            newtable_json = json.dumps(newTable)

            return render_template('datapage_table.html', table=table, field1=field1, field2=field2, newTable = newtable_json)
    return render_template('datapage_table.html')


@app.route('/comparison/chart' , methods=['POST' , 'GET']) #CHART, do stuff.
def chartComparison():
    if request.method == 'POST':
        minBackers = int(request.form["backers_min"])
        maxBackers = int(request.form["backers_max"])
        minPledged = int(request.form["pledged_min"])
        maxPledged = int(request.form["pledged_max"])
        minGoal = int(request.form["goal_min"])
        maxGoal = int(request.form["goal_max"])
        spotlight = int(request.form["SL"])
        staffpick = int(request.form["SP"])

        filterByBackerCount = True
        filterByPledgedAmount = True
        filterByGoal = True
        filterBySpotlight = True
        filterByStaffpick = True

        back int(num_str)

        










    return render_template('chartpage.html')


    ''' if request.method == 'POST':

        field1 = request.form["DV1"]
        field2 = request.form["DV2"]
        spotlight = request.form["SL"]
        staffpick = request.form["SP"]

        ds = datasource.DataSource()
        ds.connect('beckerr2', 'barn787sign')

        if (field1 == "Backer Count" and field2 == "Pledged Amount" and spotlight == "IDC" and staffpick == "IDC"):

            table = []
            table = ds.getBackersAndPledged()

            newTable = []
            i=0
            for row in table:
                rowX = [row[0], row[1]]
                newTable.append(rowX)
                i = i+1

            bestTable = []
            for row in table:
                for index in row:
                    bestTable.append(index)



            newtable_json = json.dumps(newTable)

            return render_template('datapage_table.html', table=table, field1=field1, field2=field2, newTable = newtable_json)
    return render_template('datapage_table.html')'''




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
