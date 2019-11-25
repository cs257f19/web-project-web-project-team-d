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
        elif (field1 == "Backer Count" and field2 == "Goal"):
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
        elif (field1 == "Pledged Amount" and field2 == "Goal"):
            table = []
            table = ds.getPledgedAndGoal(spot, staff)

            newTable = []
            i=0
            for row in table:
                currency = row[2]
                pledged = ds.convertCurrency(row[1], currency)
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

###TO_DO###
'''
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

        filterByBackerCount = True
        filterByPledgedAmount = True
        filterByGoal = True


        
        

        if (minBackers == 0 and maxBackers == 0):
            filterbyBackerCount = False
        
        if (minPledged == 0 and maxPledged == 0):
            filterByPledgedAmount = False
        
        if (minGoal == 0 and maxGoal == 0):
            filterByGoal = False
        
        chartData = []



        #Database Calls, sorted by displayVariable

        #Spotlight: Print two groups, has and has not been spotlighted
        #Displayed data is a list.  Index 0 is a name, 1 is it's data count, 2 is a name, 3 is it's data count, etc.


        if (displayVariable == "Spotlight"):
            isSpotlightedCount = 0
            isNotSpotlightedCount = 0 ###WORKINGHERE###

            if (filterByBackerCount and filterByPledgedAmount and filterByGoal):
                chartData = ds.getFilterByAll(minBackers, maxBackers, minPledged, maxPledged, minGoal, maxGoal)
                
                
                
                
                return render_template('TO_DO.html', displayedData = displayedData, categoryValues = categoryValues, newTable = newtable_json)
            
            elif (filterByBackerCount and filterByPledgedAmount and not filterByGoal): 
                chartData = ds.getFilterByBackersPledged(minBackers, maxBackers, minPledged, maxPledged)
                #

            elif (filterByBackerCount and not filterByPledgedAmount and filterByGoal): 
                chartData = ds.getFilterByBackersGoal(minBackers, maxBackers, minGoal, maxGoal)
                #
            
            elif (not filterByBackerCount and filterByPledgedAmount and filterByGoal): 
                chartData = ds.getFilterByPledgedGoal(minPledged, maxPledged, minGoal, maxGoal)
                #
        
            elif (filterByBackerCount and not filterByPledgedAmount and not filterByGoal): 
                chartData = ds.getFilterByBackers(minBackers, maxBackers)
                #
            
            elif (not filterByBackerCount and filterByPledgedAmount and not filterByGoal): 
                chartData = ds.getFilterByPledged(minPledged, maxPledged)

                #
            
            elif (not filterByBackerCount and not filterByPledgedAmount and filterByGoal): 
                chartData = ds.getFilterByGoal(minGoal, maxGoal)

                #
            
            elif (not filterByBackerCount and not filterByPledgedAmount and not filterByGoal): 
                chartData = ds.getFilterByNone()
                #

            else:
                print ("We fucked up")
            


        if (displayVariable == "Staffpick"):
            # all staffpick sorts:


        if (displayVariable == "Status"):
            #all status sorts
'''

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
