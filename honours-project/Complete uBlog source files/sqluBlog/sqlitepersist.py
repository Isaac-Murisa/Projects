
import sqlite3
import datetime

class SqlitePersist():
	'''This module is an implemenation of the IPersist API for the persistence solution for ublog. This implementation uses sqlite. Data is stored in the database file ublog.sqlite . If changes need to be done for the persistence for ublog, this implementation should be changed and minor changes in the file ublog.py . For purposes of consistency, each post has a time and date stamp which we assume are unique for each post. The time and date stamp will be used as a unique identifier when locating a post to update or delete. 

	How to use:
		To implement this file in ublog.py, import the file and assign the name IPersist. 
		
		from sqlitepersist import SqlitePersist as IPersist
	'''

	def initPersist(self):
		'''Initialize the database'''
		db = sqlite3.connect('ublog.sqlite')
		with open('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()



	def closePersist(self):
		'''Close database when application shutsdown'''
		db = sqlite3.connect('ublog.sqlite')
		db.close()



	def retrievePattern(self, pattern):
		'''Retrieve posts
		pattern - dictionary with filters for a post(s) to be retrieved
		return - a list with the post(s)
		'''

		#retrieve dictionary values passed
		givenAuthor = pattern.get("author")
		givenTitle = pattern.get("title")
		givenStartDate = pattern.get("start_date")
		givenEndDate = pattern.get("end_date")

		con = sqlite3.connect('ublog.sqlite')
		con.row_factory = sqlite3.Row 

		if (pattern == {}):
			posts = con.execute('SELECT * FROM post ORDER BY dateCreated DESC').fetchall()
			return posts




	def addPost(self, pdict):
		'''Add a new post/thread/update an existing post. 
		return - a confirmation string.
		raise ValueError - raise error if the user is trying to add a new post with an existing title, or trying to post a thread without an existing title.
		'''
		
		con = sqlite3.connect('ublog.sqlite')
		con.row_factory = sqlite3.Row 

		postTitles = con.execute('SELECT title FROM post').fetchall

		if (pdict['intent'] == "newTitle"):
			for p in postTitles:
				if (pdict['title'] == p):
					raise ValueError("Post title already exists. Try a new title or post a thread under the same post")

		if (pdict['intent'] == "newThread"):
			for p in postTitles:
				if (pdict['title'] == p):
					pass
				else:
					raise ValueError("Post title was not found. Try to posting a new title with the title")

		if (pdict['intent'] == "updatePost"):
			con.execute('UPDATE post SET title=? text=? WHERE dateCreated=?', (pdict['title'], pdict['text'], pdict['giveDate'],))
			con.commit()
			return "updated"

		con.execute('INSERT INTO post (title, text, author) VALUES ( ?, ?, ?)', (pdict['title'], pdict['text'], pdict['author'],))

		con.commit()
		return "added"




	def deletePost(self, deletePost):
		'''Delete a post matching a datetime
		raise ValueError - raise ValueError if the post to be deleted cannot be found
		'''

		con = sqlite3.connect('ublog.sqlite')
		con.row_factory = sqlite3.Row 
		try:
			con.execute('DELETE FROM post WHERE dateCreated=?', deletePost['givenDate'],)
			con.commit()
		except:
			raise ValueError("Cannot locate post to delete")
		
		
