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

            return render_template('datapage.html', table=table, field1=field1, field2=field2, newTable = newtable_json, spotlight=spotlight, staffpick=staffpick)

        elif (field1 == "Pledged Amount" and field2 == "Backer Count"):
            table = []
            table = ds.getBackersAndPledged(spot, staff)

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                pledged = ds.convertCurrency(row[1], currency)
                rowX = [pledged, row[0]]
                newTable.append(rowX)
                i = i+1

            newtable_json = json.dumps(newTable)

            return render_template('datapage.html', table=table, field1=field2, field2=field1, newTable = newtable_json, spotlight=spotlight, staffpick=staffpick)

        elif (field1 == "Backer Count" and field2 == "Goal"):
            table = []
            table = ds.getBackersAndGoal(spot, staff)

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                goal = ds.convertCurrency(row[1], currency)
                rowX = [row[0], goal]
                newTable.append(rowX)
                i = i+1

            newtable_json = json.dumps(newTable)

            return render_template('datapage.html', table=table, field1=field1, field2=field2, newTable = newtable_json, spotlight=spotlight, staffpick=staffpick)

        elif (field1 == "Goal" and field2 == "BackerCount"):
            table = []
            table = ds.getBackersAndGoal(spot, staff)

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                goal = ds.convertCurrency(row[1], currency)
                rowX = [goal, row[0]]
                newTable.append(rowX)
                i = i+1

            newtable_json = json.dumps(newTable)

            return render_template('datapage.html', table=table, field1=field2, field2=field1, newTable = newtable_json, spotlight=spotlight, staffpick=staffpick)
        elif (field1 == "Pledged Amount" and field2 == "Goal"):
            table = []
            table = ds.getPledgedAndGoal(spot, staff)

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                pledged = ds.convertCurrency(row[0], currency)
                goal = ds.convertCurrency(row[1], currency)
                rowX = [pledged, goal]
                newTable.append(rowX)
                i = i+1

            newtable_json = json.dumps(newTable)

            return render_template('datapage.html', table=table, field1=field1, field2=field2, newTable = newtable_json, spotlight=spotlight, staffpick=staffpick)

        elif (field1 == "Goal" and field2 == "Pledged Amount"):
            table = []
            table = ds.getPledgedAndGoal(spot, staff)

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                pledged = ds.convertCurrency(row[0], currency)
                goal = ds.convertCurrency(row[1], currency)
                rowX = [goal, pledged]
                newTable.append(rowX)
                i = i+1

            newtable_json = json.dumps(newTable)

            return render_template('datapage.html', table=table, field1=field2, field2=field1, newTable = newtable_json, spotlight=spotlight, staffpick=staffpick)

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

    ###TO_DO###

    if request.method == 'POST':

        #Casting Data from User

        ds = datasource.DataSource()
        ds.connect('beckerr2', 'barn787sign')

        minBackers = int(request.form["backers_min"])
        maxBackers = int(request.form["backers_max"])
        minPledged = int(request.form["pledged_min"])
        maxPledged = int(request.form["pledged_max"])
        minGoal = int(request.form["goal_min"])
        maxGoal = int(request.form["goal_max"])
        displayVariable = request.form["DV"]




        chartData = []

        if (displayVariable == "Spotlight"):
            isSpotlightedCount = 0
            isNotSpotlightedCount = 0 ###WORKINGHERE###

            if ((not (minBackers == 0 and maxBackers == 0)) and (not (minPledged== 0 and maxPledged== 0)) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByAll(minBackers, maxBackers, minPledged, maxPledged, minGoal, maxGoal)

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                params = "All"

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (not (minPledged== 0 and maxPledged== 0)) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByBackersPledged(minBackers, maxBackers, minPledged, maxPledged)
                params = "BP"

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (minPledged== 0 and maxPledged== 0) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByBackersGoal(minBackers, maxBackers, minGoal, maxGoal)
                params = "BG"

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0) and (not (minPledged== 0 and maxPledged== 0)) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByPledgedGoal(minPledged, maxPledged, minGoal, maxGoal)
                params = "PG"

                a = 1
                i = 10000000000^10000000000000000000000000000000000000000000000000000000000000000000000000000000000
                breakYouGodDamnFool = i * 3.1415926
                while True:
                    a = a + 1
                    print("yaaaaaaaaaaas")

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (minPledged== 0 and maxPledged== 0) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByBackers(minBackers, maxBackers)
                params = "B"

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (not (minPledged== 0 and maxPledged== 0)) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByPledged(minPledged, maxPledged)
                params = "P"

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (minPledged== 0 and maxPledged== 0) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByGoal(minGoal, maxGoal)
                params = "G"

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (minPledged== 0 and maxPledged== 0) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByNone()
                params = "None"

                for row in chartData:
                    if (row[10] == "T"):
                        isSpotlightedCount = isSpotlightedCount + 1
                    elif (row[10] == "F"):
                        isNotSpotlightedCount = isNotSpotlightedCount + 1

                newTable = []

                row1 = ["Spotlighted", isSpotlightedCount]
                newTable.append(row1)

                row2 = ["Not Spotlighted", isNotSpotlightedCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            else:
                print ("We fucked up")

        if (displayVariable == "Staffpick"):
            # all staffpick sorts:
            isStaffpickCount = 0
            isNotStaffpickCount = 0

            if ((not (minBackers == 0 and maxBackers == 0)) and (not (minPledged== 0 and maxPledged== 0)) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByAll(minBackers, maxBackers, minPledged, maxPledged, minGoal, maxGoal)
                params = "All"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (not (minPledged== 0 and maxPledged== 0)) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByBackersPledged(minBackers, maxBackers, minPledged, maxPledged)
                params = "BP"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (minPledged== 0 and maxPledged== 0) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByBackersGoal(minBackers, maxBackers, minGoal, maxGoal)
                params = "BG"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (not (minPledged== 0 and maxPledged== 0)) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByPledgedGoal(minPledged, maxPledged, minGoal, maxGoal)
                params = "PG"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (minPledged== 0 and maxPledged== 0) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByBackers(minBackers, maxBackers)
                params = "B"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (not (minPledged== 0 and maxPledged== 0)) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByPledged(minPledged, maxPledged)
                params = "P"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (minPledged== 0 and maxPledged== 0) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByGoal(minGoal, maxGoal)
                params = "G"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (minPledged== 0 and maxPledged== 0) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByNone()
                params = "None"

                for row in chartData:
                    if (row[11] == "T"):
                        isStaffpickCount = isStaffpickCount + 1
                    elif (row[11] == "F"):
                        isNotStaffpickCount = isNotStaffpickCount + 1

                newTable = []

                row1 = ["Staff-Picked", isStaffpickCount]
                newTable.append(row1)

                row2 = ["Not Staff-Picked", isNotStaffpickCount]
                newTable.append(row2)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            else:
                print ("We fucked up")

        if (displayVariable == "Status"):
            #all status sorts
            statusSuccess = 0
            statusFailed = 0
            statusCancelled = 0
            statusSuspended = 0
            statusLive = 0

            if ((not (minBackers == 0 and maxBackers == 0)) and (not (minPledged== 0 and maxPledged== 0)) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByAll(minBackers, maxBackers, minPledged, maxPledged, minGoal, maxGoal)
                params = "All"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)


            elif ((not (minBackers == 0 and maxBackers == 0)) and (not (minPledged== 0 and maxPledged== 0)) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByBackersPledged(minBackers, maxBackers, minPledged, maxPledged)
                params = "BP"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (minPledged== 0 and maxPledged== 0) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByBackersGoal(minBackers, maxBackers, minGoal, maxGoal)
                params = "BG"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (not (minPledged== 0 and maxPledged== 0)) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByPledgedGoal(minPledged, maxPledged, minGoal, maxGoal)
                params = "PG"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((not (minBackers == 0 and maxBackers == 0)) and (minPledged== 0 and maxPledged== 0) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByBackers(minBackers, maxBackers)
                params = "B"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (not (minPledged== 0 and maxPledged== 0)) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByPledged(minPledged, maxPledged)
                params = "P"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (minPledged== 0 and maxPledged== 0) and (not (minGoal== 0 and maxGoal== 0))):
                chartData = ds.getFilterByGoal(minGoal, maxGoal)
                params = "G"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            elif ((minBackers == 0 and maxBackers == 0)and (minPledged== 0 and maxPledged== 0) and (minGoal== 0 and maxGoal== 0)):
                chartData = ds.getFilterByNone()
                params = "None"

                for row in chartData:
                    if (row[12] == "S"):
                        statusSuccess = statusSuccess + 1
                    elif (row[12] == "F"):
                        statusFailed = statusFailed + 1
                    elif (row[12] == "C"):
                        statusCancelled = statusCancelled + 1
                    elif (row[12] == "X"):
                        statusSuspended = statusSuspended + 1
                    elif (row[12] == "L"):
                        statusLive = statusLive + 1

                newTable = []

                row1 = ["Succesful", statusSuccess]
                newTable.append(row1)

                row2 = ["Failed", statusFailed]
                newTable.append(row2)

                row3 = ["Cancelled", statusCancelled]
                newTable.append(row3)

                row4 = ["Suspended", statusSuspended]
                newTable.append(row4)

                row5 = ["Live", statusLive]
                newTable.append(row5)

                newtable_json = json.dumps(newTable)

                return render_template('chartpage.html', displayVariable = displayVariable, newTable = newtable_json, params=params, minBackers = minBackers, maxBackers = maxBackers, minPledged = minPledged, maxPledged = maxPledged, minGoal = minGoal, maxGoal = maxGoal)

            else:
                print ("We fucked up")
    return render_template('chartpage.html')


    




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
