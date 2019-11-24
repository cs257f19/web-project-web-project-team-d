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

	def getKickstartersBlurbContains(self, blurb):
		'''
        Returns a list of all of the kickstarter projects that have the given string in their 'blurb'

        PARAMETERS:
            blurb - the string to check within each blurb

        RETURN:
			a list of all of the kickstarter projects that have the given string in their 'blurb'        '''
		return []

	def getKickstartersNameContains(self, name):
		'''
        Returns a list of all of the kickstarter projects that have the given string in their name

        PARAMETERS:
            name - the string to check within each name

        RETURN:
			a list of all of the kickstarter projects that have the given string in their name
		'''
		return []

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

	def getKickerstartersInGoalRange(self, goal_max, goal_min = 0):
		'''
        Returns a list of all of the kickstarter projects whose goal is in the specified range.

        PARAMETERS:
            goal_max - the maximum amount for the goal
			goal_min - the minimum amount for the goal

        RETURN:
            a list of all of the kickstarter projects whose goal is in the specified range.
        '''
		return []

	def getKickerstartersInBackersRange(self, backers_max, backers_min = 0):
		'''
        Returns a list of all of the kickstarter projects that have the specified range of backers.

        PARAMETERS:
            backers_max - the maximum number of backers
			backers_min - the minimum number of backers

        RETURN:
            a list of all of the kickstarter projects that have the specified range of backers.
        '''
		return []

	def getKickerstartersInPledgeRange(self, pledge_max, pledge_min = 0):
		'''
        Returns a list of all of the kickstarter projects that have the specified range of pledge money.

        PARAMETERS:
            pledge_max - the maximum pledge amount
			pledge_min - the minimum pledge amount

        RETURN:
            a list of all of the kickstarter projects that have the specified range of pledged money.
        '''
		return []

	def getBackersAndPledged(self):
		'''
		Returns a list with only the number of backers and pledged amount, along with currency type


		PAREMETERS:
			none

		RETURN:
			a list with only the number of backers and pledged amount
		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	backers_count, pledged, currency FROM kickstarter"
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
		if cur_currency == "USD":
			return amount
		elif cur_currency == "EUR":
			return amount*eur
		elif cur_currency == "CAD":
			return amount*cad
		elif cur_currency == "AUD":
			return amount*aud
		elif cur_currency == "CHF":
			return amount*chf
		elif cur_currency == "DKK":
			return amount*dkk
		elif cur_currency == "GBP":
			return amount*gbp
		elif cur_currency == "HKD":
			return amount*hkd
		elif cur_currency == "JPY":
			return amount*jpy
		elif cur_currency == "MXN":
			return amount*mxn
		elif cur_currency == "NOK":
			return amount*nok
		elif cur_currency == "NZD":
			return amount*nzd
		elif cur_currency == "SEK":
			return amount*sek
		elif cur_currency == "SGD":
			return amount*sgd
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
