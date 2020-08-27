import shelve
import datetime


class ShelvePersist():
	"""The persistence solution implements the IPersist interface (API). The solution uses Shelve to store post data."""


	def initPersist(self):
		'''Create the file to be used by the shelve'''
		blogshelve = shelve.open('blogfile.txt', writeback=True)
		blogshelve.close()



	def closePersist(self):
		'''Close the persistence solution'''
		blogshelve.close()



	def retrievePattern(self, pattern):
		'''Retrieve posts matching a given pattern
		pattern - dictionary with filters for a post(s) to be retrieved
		return - a list with the post(s)
		'''

		global blogshelve
		global post_list
		blogshelve = shelve.open('blogfile.txt', writeback=True)


		post_list = []		#list to hold posts retrieved

		#Get the list of keys
		listof_keys = list(blogshelve.keys())

		#retrieve dictionary values passed
		givenAuthor = pattern.get("author")
		givenTitle = pattern.get("title")
		givenStartDate = pattern.get("start_date")
		givenEndDate = pattern.get("end_date")

		#Retrieve all posts
		for key in listof_keys:
			authorsPosts = blogshelve[key]
			for p in authorsPosts:
				post_list.append(p)

		blogshelve.sync()
		return post_list


	def addPost(self, pdict):
		'''Add a post or update an already exsisting post

		pdict - dictionary containing new post data
		newtitle - if True, create a new post. updatePost should be false.
		udatePost - if True, update an already exsisting post. newTitle should be False

		return - a string confirming operation done'''
		
		blogshelve = shelve.open('blogfile.txt', writeback=True)
		
		#If the user already exsist then continue to add post to users list of posts. Else create a new list for the user
		flag = pdict['author'] in blogshelve.keys()
		if (flag == False):
			blogshelve[pdict['author']] = []


		#Raise a UblogException if post title already exsist while trying to add a new post
		if (pdict['intent'] == "newPost"):
			for p in post_list:
				if (p[1] == pdict['title']):
					raise ValueError("Post title already exists. Try a new title or post a thread under the same post")

		#Raise a Ublog Exception if post title does not exsist while trying to add a post to a thread. A title shuld be provided for an exsisting post/thread
		if (pdict['intent'] == "newThread"):
			foundTitle = False
			for p in post_list:
				if ((p[1]) == pdict['title']):
					foundTitle = True
			if (foundTitle == False):
				raise ValueError("Post title was not found. Try to posting a new title with the title")

		#If the intent is to update a post, locate the post from the authors post list using the datetime and update.
		if (pdict['intent' == "updatePost"]):
			for p in blogshelve[pdict['author']]:
				if (p[3] == pdict['givenDate']):
					blogshelve[pdict['author']].append((
						pdict['author'],
						pdict['title'],
						pdict['text'],		
						datetime.datetime.now(),
					))
				else:
					raise ValueError("No post with that date found to update")
			blogshelve.sync()
			return "updated"


		blogshelve[pdict['author']].append((
			pdict['author'],
			pdict['title'],
			pdict['text'],		
			datetime.datetime.now(),
		))
		blogshelve.sync()
		return "added"




	def deletePost(self, deleteDict):
		'''Delete a post

		return - confirmation if the post was deleted'''

		temp = blogshelve[deleteDict['author']]
		for p in temp:
			if (p[3] == deleteDict['givenDate']):
				del p
				blogshelve.sync()
				return True
			else:
				raise UblogException("Post cannot be deleted or unavailable")
				return False

