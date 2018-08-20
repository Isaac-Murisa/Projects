import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__) #create the application instance
app.config.from_object(__name__) #load config from this file, flaskr.py
"""
Module for the Reset Password feature. Returns the data of the provided user and as well has a functin to set a new password.
"""

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(os.path.join(app.root_path, 'flaskr.db'))
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	"""Opens a new database connection if there is none yet for the current application context."""

	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db


def getUserInfo(temp_user):
	"""
	Get the user infomation from the database. 
	Pass a user name and get the information.

		e.g. getUserInfo("icm")
			 getUserInfo(username)
	"""
	db = get_db()
	curr = db.execute('select * from users where username=?',(temp_user,))
	d = curr.fetchone()
	return d
	

def setPassword(temp_user, newP):
	"""

	Call the function with the user to which you want to reset the password to.
	And the new password to be inserted.
	The function resets the password with the the new password in the database.

		e.g. setPassword("icm", "*****")
			 setPassword(username, password)
	"""
	db = get_db()
	db.execute('''update users set pass = ? where username=?''', (newP, temp_user,))
	db.commit()



