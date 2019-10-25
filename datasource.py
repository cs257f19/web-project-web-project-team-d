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
		self.connection = null

	def connect(user, password):
		'''
		Establishes a connection to the database with the following credentials:
			user - username, which is also the name of the database
			password - the password for this database on perlman

		Returns: a database connection.

		Note: exits if a connection cannot be established.
		'''
		try:
			connection = psycopg2.connect(host="localhost",database=user, user=user, password=password)
		except Exception as e:
			print("Connection error: ", e)
			exit()
		return connection

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
		return []


	def getKickstartersInCategory(self, category):
		'''
        Returns a list of all of the kickstarter projects that are in the specified category.

        PARAMETERS:
            category - The category of the project (integer values)

        RETURN:
            a list of all of the kickstarter projects that are in the specfied category.
        '''
		return []

	def getKickstartersInState(self, state):
		'''
        Returns a list of all of the kickstarter projects that are in the given state.

        PARAMETERS:
            state - a string defining the current state of the project
			(S for success, F for failed, C for cancelled, L for live, X for suspended)

        RETURN:
			a list of all of the kickstarter projects that are in the given state
		'''
		return []

	def getKickstartersInSpotlight(self, spotlight):
		'''
        Returns a list of all of the kickstarter projects that are in the given spotlight state.

        PARAMETERS:
            spotlight - a string defining whether the project has spotlight status (T/F)

        RETURN:
			a list of all of the kickstarter projects that are in the given spotlight state.
		'''
		return []

	def getKickstartersInStaffPick(self, pick):
		'''
        Returns a list of all of the kickstarter projects that are in the given staff pick state.

        PARAMETERS:
            spotlight - a string defining whether the project has staff pick status (T/F)

        RETURN:
			a list of all of the kickstarter projects that are in the given staff pick state.
		'''
		return []

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

	def getKickstartersCreatedInDateRange(self, start, end):
		'''
        Returns a list of all of the kickstarter projects that were created in the specified date range.

        PARAMETERS:
            start - the starting date of the range in unix time
            end - the ending date of the range in unix time

        RETURN:
            a list of all of the kickstarter projects that were created in the specified date range.
        '''
		return []


	def getKickstartersLaunchedInDateRange(self, start, end):
		'''
        Returns a list of all of the kickstarter projects that were launched in the specified date range.

        PARAMETERS:
            start - the starting date of the range in unix time
            end - the ending date of the range in unix time

        RETURN:
            a list of all of the kickstarter projects that were launched in the specified date range.
        '''
		return []

	def getKickstartersDeadlineInDateRange(self, start, end):
		'''
        Returns a list of all of the kickstarter projects whose deadlines are in the specified date range.

        PARAMETERS:
            start - the starting date of the range in unix time
            end - the ending date of the range in unix time

        RETURN:
            a list of all of the kickstarter projects whose deadlines are in the specified date range.
        '''
		return []

	def getKickstartersStateChangedInDateRange(self, start, end):
		'''
        Returns a list of all of the kickstarter projects whose states changed in the specified date range.

        PARAMETERS:
            start - the starting date of the range in unix time
            end - the ending date of the range in unix time

        RETURN:
            a list of all of the kickstarter projects whose states changed in the specified date range.
        '''
		return []


	def getBackersVsPledged(self):
		'''
		Returns a list with only the number of backers and pledged amount


		PAREMETERS:
			none

		RETURN:
			a list with only the number of backers and pledged amount
		'''
		return []


	def getUniqueCurrencies():
		'''
		Returns a list with only the strings representing unique currencies


		PAREMETERS:
			connection - the connection to the database

		RETURN:
			a list with only the strings representing unique currencies
		'''
		return []

	def main():
		user = 'beckerr2'
		password = getpass.getpass()

		ds = DataSource()
		ds.connect(user, password)

		ds.disconnect()


	if __name__ == "__main__":
		main()
