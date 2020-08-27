'''
Datetime not the best but will be used
'''

import sqlite3
import datetime

schema = "schema.sql"
dataBase = "sqluBlog/ublog.db"


def connect_db():
	'''Connects to the database'''

	databaseConnection = sqlite3.connect(dataBase)
	databaseConnection.row_factory = sqlite3.Row 
	return databaseConnection			#Return the connection object back to caller



def initPersist(self):
	'''Initialize the database'''

	db = connect_db()
	with open(schema, mode='r') as f:
			db.cursor().executescript(f.read())
	db.commit()



def closePersist(self):
	''''''
	con = connect_db()
	con.close()



def retrievePattern(self, pattern):
	''''''
	#retrieve dictionary values passed
	givenAuthor = pattern.get("author")
	givenTitle = pattern.get("title")
	givenStartDate = pattern.get("start_date")
	givenEndDate = pattern.get("end_date")

	con = connect_db()

	if (pattern == {}):
		posts = con.execute(
			'SELECT id, title, text, dateCreated, author_id'
			' FROM post'
			' ORDER BY dateCreated DESC'
		).fetchall()
		return posts




def addPost(self, pdict):
	''''''
	
	con = connect_db()
	postTitles = con.execute('SELECT title FROM posts ').fetchall

	if (pdict['intent'] == "newTitle"):
		for p in postTitles:
			if (pdict['title'] == p):
				raise UblogException("")

	if (pdict['intent'] == "newThread"):
		for p in postTitles:
			if (pdict['title'] = p):
				pass
			else:
				raise UblogException("")

	if (pdict['intent'] == "updatePost"):
		con.execute('UPDATE ')
		con.commit()
		return "updated"

	con.execute(
		'INSERT INTO post (title, text, author, date)'
		'VALUES ( ?, ?, ?, ?)'
		(pdict['title'], pdict['text'], pdic['author'], datetime.datetime.now())
	)

	con.commit()
	return "added"




def deletePost(self, deletePost):
	'''Delete a post matching a datetime'''

	con = connect_db()
	try:
		con.execute('DELETE ', deletePost['givenDate'],)
		con.commit()
	except:
		raise UblogException("")
	
	
