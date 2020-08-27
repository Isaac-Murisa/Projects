class IPersist():
	"""Persistence API for the ublog application.

	How To Use:
	Create an instance of the IPersist class and assign the object to a variable.
	
	Example:
	x = IPersist()
	
	"""

	def initPersist(self): 
		"""Initialize and open the persistence file to be used for ublog"""
		pass
		

	def closePersist(self):
		"""Close the open persistence file when the application stops execution"""
		pass


	def retrievePattern(self, pattern):
		"""Retrieve posts matching a pattern. 

		Pattern -- is a dictionary with any combination of the attributes below. 

		title -- title to match.
		datefrom -- retrieve posts from date range starting from. Must be in the format %y-%m.
		dateto -- retrieve posts from date range up to. Must be in the format %y-%m.
		author -- retrieve posts by a specific user with username.

		Accepted Patterns:
		None -- if no pattern is given, the function will retain all posts.
		{"author":"*value*"} -- this pattern returns post(s) by an author/user.
		{"author":"value", "title":"value"} -- this pattern should have the author and title keys with their corresponding values. Returns post(s) matching the author and title.
		{"title":"value", "datefrom":"value", "dateto":"value"} -- this pattern retains a post thread for a title, matching the date range provided.
		
		returns -- a list of posts retrieved matching pattern or all the posts if pattern was not provided.
		"""
		pass


	def addPost(self, pdict):
		"""Add a new post, comment or update an existing post.
		
		pdict -- content of the post in the form of a dictionary. (title and text)
		newtitle -- set to true if the post is a new title, otherwise false.
		updatePost -- set to true if the post already exists and its an update, otherwise false.

		exceptions - a UBlogExcpetion is raseid if a post which was meant to updated is not found.

		returns -- the post with an id field injected or None if no post added
		"""
		pass


	def deletePost(self, deleteDict):
		"""Delete a post or comment matching a pattern

		author --  author who made post
		title -- title of post to be deleted
		date -- date when post was made
		id -- id number of post

		Accepted Patterns:
		{"author":"value"} -- delete all the posts made by a user.
		{"author":"value", "title":"value"} -- delete a post thread including the original post.
		{"author":"value","id":"value"} -- delete a single post by author matching the given id.

		exceptions -- a UblogExceprion is raised if post cannot be found.

		return -- confirmation if post was deleted
		"""
		pass


class UblogException(Exception):
	"""Exception class for UblogExceptions

	Attributes:
	mag -- provide a message to accompany the raised exception. This field is optional.
	"""
	def __init__(self, msg=None):
		if msg is None:
			msg = "An error occured with uBlog API usage"
		Exception.__init__(self, msg)
		
