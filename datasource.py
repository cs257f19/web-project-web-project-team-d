'''
datasource.py

Code for the back-end of our Kickstarter analysis tool

author: Eric Neidhart, Sonya Romanenko, Ryan Becker
date: 25 October 2019
Adapted from the templates provided in the assignment
'''

import psycopg2
import getpass

class DataSource:
	'''
	DataSource executes all of the queries on the database.
	It also formats the data to send back to the frontend, typically in a list
	or some other collection or object.
	'''

	def __init__(self):
		self.connection = None

	def connect(self, user, password):
		'''
		Establishes a connection to the database with the following credentials:
			user - username, which is also the name of the database
			password - the password for this database on perlman

		Returns: a database connection.

		Note: exits if a connection cannot be established.
		'''
		try:
			self.connection = psycopg2.connect(host="localhost",database=user, user=user, password=password)
		except Exception as e:
			print("Connection error: ", e)
			exit()
		return self.connection

	def disconnect(self):
			self.connection.close()



	def getKickstartersUsingCurrency(self, currency):
		'''
        Returns a list of all of the kickstarter projects that were created using the specified currency (for setting the goal)

        PARAMETERS:
            name - the abbreviated name of the currency

        RETURN:
			a list of all of the kickstarter projects that were created using the specified currency
		'''

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE currency = " +str(currency)
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getKickstartersInState(self, state):
		'''
        Returns a list of all of the kickstarter projects that are in the given state.

        PARAMETERS:
            state - a string defining the current state of the project
			(S for success, F for failed, C for cancelled, L for live, X for suspended)

        RETURN:
			a list of all of the kickstarter projects that are in the given state
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE current_state LIKE '%" +str(state)+"%'"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getKickstartersInSpotlight(self, spotlight):
		'''
        Returns a list of all of the kickstarter projects that are in the given spotlight state.

        PARAMETERS:
            spotlight - a string defining whether the project has spotlight status (T/F)

        RETURN:
			a list of all of the kickstarter projects that are in the given spotlight state.
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE spotlight LIKE '%" +str(spotlight)+"%'"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getKickstartersInStaffPick(self, pick):
		'''
        Returns a list of all of the kickstarter projects that are in the given staff pick state.

        PARAMETERS:
            spotlight - a string defining whether the project has staff pick status (T/F)

        RETURN:
			a list of all of the kickstarter projects that are in the given staff pick state.
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE staff_pick LIKE '%" +str(pick)+"%'"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
			
	def getFilterByAll(self,minBackers, maxBackers, minPledged, maxPledged, minGoal, maxGoal):

		try:
			cursor = self.connection.cursor()
			query = ("SELECT * FROM kickstarter WHERE ((backers_count BETWEEN " + str(minBackers) + " AND " + str(maxBackers) + ") AND (pledged BETWEEN " + str(minPledged) + " AND " + str(maxPledged) + ") AND (goal BETWEEN " +str(minGoal) + " AND " +str(maxGoal) +"))")
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None


	def getFilterByBackersPledged(self,minBackers, maxBackers, minPledged, maxPledged):

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE ((backers_count BETWEEN " + str(minBackers) + " AND " + str(maxBackers) + ") AND (pledged BETWEEN " +str(minPledged) + " AND " +str(maxPledged)+"))"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getFilterByBackersGoal(self,minBackers, maxBackers, minGoal, maxGoal):

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE ((backers_count BETWEEN " + str(minBackers) + " AND " + str(maxBackers) + ") AND (goal BETWEEN " +str(minGoal) +" AND " +str(maxGoal) +"))"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getFilterByPledgedGoal(self,minPledged, maxPledged, minGoal, maxGoal):

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE ((pledged BETWEEN " +str(minPledged) + " AND " +str(maxPledged) +") AND (goal BETWEEN " +str(minGoal) +" AND " +str(maxGoal) +"))"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getFilterByBackers(self,minBackers, maxBackers):

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE (backers_count BETWEEN " + str(minBackers) + " AND " + str(maxBackers) + ")"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getFilterByPledged(self,minPledged, maxPledged):

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE (pledged BETWEEN " +str(minPledged) + " AND " +str(maxPledged)+ ")"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getFilterByGoal(self,minGoal, maxGoal):

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter WHERE (goal BETWEEN " +str(minGoal) +" AND " +str(maxGoal) +")"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getFilterByNone(self):

		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM kickstarter"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
	
	

	def getBackersAndPledged(self, spot, staff):
		'''
		Returns a list with only the number of backers and pledged amount, along with currency type


		PAREMETERS:
			none

		RETURN:
			a list with only the number of backers and pledged amount
		'''
		try:
			cursor = self.connection.cursor()
			if(spot == "t" and staff == "t"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (spotlight='T' AND staff_pick='T') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "t" and staff =="f"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (spotlight='T' AND staff_pick='F') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f" and staff =="f"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (spotlight='F' AND staff_pick='F') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f" and staff =="t"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (spotlight='F' AND staff_pick='T') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "t"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (spotlight='T') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (spotlight='F') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(staff == "t"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (staff_pick='T') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(staff == "f"):
				query = "SELECT	backers_count, pledged, currency FROM kickstarter WHERE (staff_pick='F') ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()
			else:
				query = "SELECT	backers_count, pledged, currency FROM kickstarter ORDER BY pledged DESC"
				cursor.execute(query)
				return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
	
	def getBackersAndGoal(self, spot, staff):
		'''
		Returns a list with only the number of backers and pledged amount, along with currency type

		PAREMETERS:
			none

		RETURN:
			a list with only the number of backers and pledged amount
		'''
		try:
			cursor = self.connection.cursor()
			if(spot == "t" and staff == "t"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (spotlight='T' AND staff_pick='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "t" and staff =="f"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (spotlight='T' AND staff_pick='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f" and staff =="f"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (spotlight='F' AND staff_pick='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f" and staff =="t"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (spotlight='F' AND staff_pick='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "t"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (spotlight='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (spotlight='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(staff == "t"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (staff_pick='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(staff == "f"):
				query = "SELECT	backers_count, goal, currency FROM kickstarter WHERE (staff_pick='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			else:
				query = "SELECT	backers_count, goal, currency FROM kickstarter ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getPledgedAndGoal(self, spot, staff):
		'''
		Returns a list with only the number of backers and pledged amount, along with currency type

		PAREMETERS:
			none

		RETURN:
			a list with only the number of backers and pledged amount
		'''
		try:
			cursor = self.connection.cursor()
			if(spot == "t" and staff == "t"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (spotlight='T' AND staff_pick='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "t" and staff =="f"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (spotlight='T' AND staff_pick='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f" and staff =="f"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (spotlight='F' AND staff_pick='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f" and staff =="t"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (spotlight='F' AND staff_pick='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "t"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (spotlight='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(spot == "f"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (spotlight='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(staff == "t"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (staff_pick='T') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			elif(staff == "f"):
				query = "SELECT	pledged, goal, currency FROM kickstarter WHERE (staff_pick='F') ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()
			else:
				query = "SELECT	pledged, goal, currency FROM kickstarter ORDER BY goal DESC"
				cursor.execute(query)
				return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
	
	def getUniqueCurrencies(self):
		'''
		Returns a list with only the strings representing unique currencies


		PAREMETERS:
			connection - the connection to the database

		RETURN:
			a list with only the strings representing unique currencies
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	DISTINCT currency FROM kickstarter"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def convertCurrency(self, amount, cur_currency):  #Not one of our database query methods.  Don't grade.
		'''
		Returns a double that represents "amount" converted to USD or -1 if the currency type is not present in the dataset.

		PAREMETERS:
		amount - amount of money
		cur_currency - the current currency being used

		RETURN:
		a double that represents "amount" converted to USD, or -1 if incorrect currency
		'''
		aud = 0.68
		cad = .77
		chf = 1.01
		dkk = 0.15
		eur = 1.11
		gbp = 1.28
		hkd = 0.13
		jpy = 0.0092
		mxn = 0.052
		nok = 0.11
		nzd = 0.63
		sek = 0.10
		sgd = 0.73
		usd = 1
		if cur_currency == 'USD':
			return amount
		elif cur_currency == 'EUR':
			new_amount = eur * amount
			return new_amount
		elif cur_currency == 'CAD':
			new_amount = cad * amount
			return new_amount
		elif cur_currency == 'AUD':
			new_amount = aud * amount
			return new_amount
		elif cur_currency == 'CHF':
			new_amount = chf * amount
			return new_amount
		elif cur_currency == 'DKK':
			new_amount = dkk * amount
			return new_amount
		elif cur_currency == 'GBP':
			new_amount = gbp * amount
			return new_amount
		elif cur_currency == 'HKD':
			new_amount = hkd * amount
			return new_amount
		elif cur_currency == 'JPY':
			new_amount = jpy * amount
			return new_amount
		elif cur_currency == 'MXN':
			new_amount = mxn * amount
			return new_amount
		elif cur_currency == 'NOK':
			new_amount = nok * amount
			return new_amount
		elif cur_currency == 'NZD':
			new_amount = nzd * amount
			return new_amount
		elif cur_currency == 'SEK':
			new_amount = sek * amount
			return new_amount
		elif cur_currency == 'SGD':
			new_amount = sgd * amount
			return new_amount
		else:
			return -1




def main():
	user = 'beckerr2'
	password = 'barn787sign'

	ds = DataSource()
	ds.connect(user, password)

	list = ds.getBackersAndPledged()

	for i in range (0,100):
		print (list[i])
	ds.disconnect()


if __name__ == "__main__":
	main()
