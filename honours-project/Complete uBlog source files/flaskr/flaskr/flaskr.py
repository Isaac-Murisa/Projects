"""This module is a modified flaskr.py file implementing python shelve as the persistence option. This module does not use any database.The shelve implementation uses the blogshelve.txt to store data. 

Data Structure:
	Shelve stores data in the form of a dictionary, each data entry for this blog is keyed using username. Each dictonary contains a list of 	tuples. Each tuple is a post which holds the post title, post text and the date post was made.
	{ "username":"[ (tuple 1), (tuple 2), (tuple 3), (tuple 4), ... ]" }

Tuple structure:
	title - title for each post
	text - post content
	date - date post was made
"""

import os
import sys
import shelve
import datetime
print(sys.path)

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
#global blogshelve
#global post_retrieved

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


def initialize():
	'''Create the file to be used for the persistence'''
	shelveFile = shelve.open('blogfile.txt', writeback=True)
	shelveFile.close()



@app.cli.command('initdb')
def initdb_command():
    """Clear the existing data and create new tables."""
    initialize()
    print('Initialized the database.')



@app.teardown_appcontext
def closePersist(error):
	'''After a request is done, close the shelve file'''
	blogshelve.close()



@app.route('/')
def show_entries():
	"""Retrieve all the posts in the file. For each user, traverse the list of post tuples and add them to the retrieval list which will be passed for rendering. 
	"""
	global blogshelve
	global post_retrieved
	blogshelve = shelve.open('blogfile.txt', writeback=True)

	entry_list = list(blogshelve.keys())    #get the list of all the keys in blogfile
	post_retrieved = []

	for k in entry_list:		#For each key in blogfile get the list of post tuples
		temp = blogshelve[k]
		for e in temp:
			post_retrieved.append(e)		#Get each post tuple from the list of post tuple

	return render_template('show_entries.html', post_list=post_retrieved)		#Pass the list of post tuples to the template

	blogshelve.sync()




@app.route('/add', methods=['POST'])
def add_entry():
	"""Add a post made by user. User should be logged in to add a post."""

	#Only logged-in users can create a post
	if not session.get('logged_in'):
		abort(401)

	blogshelve = shelve.open('blogfile.txt', writeback=True)

	#Check if user has already made a post before. If not, then define a list to contain post tuples
	flag = session['username'] in blogshelve.keys()
	if (flag == False):
		blogshelve[session['username']] = []

	#Check if the the new post being added has a title which already exsist. If the title already exsist notify the user and do not add any post. A new post should have a unique title.
	if (request.form['intent'] == "newPost"):
		for p in post_retrieved:
			if (request.form['title'] == p[0]):
				flash('Post title already exists. Try a new title or post a thread under the same post')
				return redirect(url_for('show_entries'))

	#Check if the new thread post has a title which already exsist. If the title does not exsist notify the user and post is not added. A thread should follow an exsist title. 
	if (request.form['intent'] == "newThread"):
		foundTitle = False
		for p in post_retrieved:
			if (request.form['title'] == p[0]):
				foundTitle = True
		if (foundTite == False):
			flash('Post title was not found. Try posting a new title with the title')
			return redirect(url_for('show_entries'))
	

	# Proceed to add a new post tuple to user's post list
	blogshelve[session['username']].append((
		request.form['title'],
		request.form['text'],
		datetime.datetime.now(),
	))

	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

	#sync changes made
	blogshelve.sync()




@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login with the default login credentials and update session"""

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
	"""Logout current user"""

	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))
