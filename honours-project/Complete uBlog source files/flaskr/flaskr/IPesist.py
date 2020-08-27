import shelve

class IPersist(interface.interface):
	"""Persistence API for the ublog application.

	How To Use:
	Create an instance of the IPersist class and assign the object to a variable.
	
	Example:
	x = IPersist()
	
	"""
		

	def retrievePatten(self, patten):
		"""Retrieve 20 posts matching a patten. Call function with a patten to retrieve posts that match patten.

		Patten -- Patten is a dictionary with any combination of the attributes below. 

		title -- title to match.
		datefrom -- retrieve posts from date range starting from. Must be in the format %y-%m.
		dateto -- retrieve posts from date range up to. Must be in the format %y-%m.
		username -- retrieve posts by a specific user with username.
		id -- retrieve a post that match an id

		return -- default number of posts matching patten provided.

		"""
		pass

	def addPost(self, pdict, newtitle=true, updatePost=false):
		"""Add a new post, comment or update an existing post.
		
		pdict -- content of the post in the form of a dictionary. (title and text)
		newtitle -- set to true if the post is a new title, otherwise false.
		updatePost -- set to true if the post already exists and its an update, otherwise false.

		exceptions - a UBlogExcpetion is raseid if: raise Exception("Cant find post to update")
		returns the post with an id field injected or none if no post added

		"""
		pass

	def deletePost(self, patten):
		"""Delete a post or comment matching a patten

		patten -- dictionary with the following attributes

		username -- username of author who made post
		title -- title of post to be deleted
		date -- date when post was made
		id -- id number of post

		raise Exception("Cant locate post")

		return -- an int of the number of posts deleted
		"""
		pass

	@interface.default
	def initialize(self, persist_name): 
		"""Initialize and open the shelve file to be used for ublog

		persist_file -- provide a filename to be used by shelve

		return -- 
		"""
		
		file_open_conn = shelve.open(persist_file, writeback=True)
		
		return file_open_conn
		
	@interface.default
	def closeFile(self, file_open_conn):
		"""Close an opened file connection

		file_open_conn -- connection object to shelve open file
		"""
		file_open_conn.close()

	@interface.default
	def syncFile(self, file_open_conn):
		"""Update any changes to the shelve file without closing file

		file_open_conn -- connection to shelve open file
		"""
		file_open_conn.sync()


class Ublogxception(Exception):
	def __init__(self):
		Exception.__init__(self,"Can't find post to update or post does not exist")

class PostNotFound(Exception):
	def __init__(self):
		Exception.__init__(self, "Post not found matching patten")

class NewPostError(Exception):
	def __init__(self):
		Exception.__init__(self, "Can't create new post and update post at the same time")
