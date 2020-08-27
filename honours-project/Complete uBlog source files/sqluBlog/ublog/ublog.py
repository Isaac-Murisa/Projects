"""This module is a redesigned module of the flaskr.py with the Dependency Inversion Principle factored. The DIP is factored into the persistence solution. The module uses ducktyping too implement the persistence file. The ipersist.py defines the persistence API for implementing a persistence solution. If any change is to be done on implementing a new persistence solution, the implementation should follow the defined persistence API. To connect to the persistence solution, instantiate a persistence object which will be used to connnect to the persistence implementation. 
"""

import os
import sys
import datetime
import logging
print(sys.path)

from sqlitepersist import SqlitePersist as IPersist	#Persistence API  

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    KEY='0'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#Persistence API object
interface = IPersist()



@app.cli.command('initdb')
def initdb_command():
    """Clear the existing data and create new tables."""
    interface.initPersist()
    print('Initialized the database.')



@app.teardown_appcontext
def closePersist(error):
	'''After a request is done, close the shelve file'''
	interface.closePersist()



@app.route('/')
def show_entries():
	'''Retrieve post matching a pattern. If no pattern is provided all post are retrieved.'''

	pattern = {}		#No pattern provided. Retrieves all posts.
	posts_retrieved = interface.retrievePattern(pattern)
	return render_template('show_entries.html', post_list=posts_retrieved)
	



@app.route('/add', methods=['POST'])
def add_entry():
	'''Add a new post'''	

	#Only logged-in users can create a post
	if not session.get('logged_in'):
		abort(401)

	toAddPost = {
		"author": session['username'],
		"title": request.form['title'],
		"text": request.form['text'],
		"intent": request.form['intent']
	}
	feedback = ""
	try:
		feedback = interface.addPost(toAddPost)

	except ValueError as e:
		logger = logging.Logger('catch_all')
		msg = logger.error(str(e))
		flash(msg)

	if (feedback == "added"):
		flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))




@app.route('/login', methods=['GET', 'POST'])
def login():
	'''Handle login requests. '''

	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			session['username'] = request.form['username']
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)




@app.route('/logout')
def logout():
	'''Handle logout requests.'''

	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

