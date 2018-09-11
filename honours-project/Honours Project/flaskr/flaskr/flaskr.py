# all the imports
import os
import sys
import sqlite3
import shelve
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

# Shelve file for storage
#blogshelve = shelve.open('blogfile.db', writeback=True)

@app.route('/')
def show_entries():
    blogshelve = shelve.open('blogfile.txt', writeback=True)
    try:
        entry_list = list(blogshelve.keys())
        post_list = []
        if (len(entry_list) == 0):   #if there are no entries
            return render_template('show_entries.html', post_list=post_list)
        else:
            for k in entry_list:
                temp = blogshelve[k]
                for e in temp:
                    post_list.append(e)

            print( str(post_list), file=sys.stderr)  
            return render_template('show_entries.html', post_list=post_list)
    finally:
        blogshelve.close()

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    blogshelve = shelve.open('blogfile.txt', writeback=True)
    try:
        try:
            flag = session['username'] in blogshelve.keys()
        except KeyError:
            blogshelve[session['username']] = []
        blogshelve[session['username']].append((
            request.form['title'],
            request.form['text'],
        ))

        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))
    finally:
        blogshelve.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
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
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
