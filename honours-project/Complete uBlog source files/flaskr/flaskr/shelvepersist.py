import shelve

class ShelvePersist(implements(IPersist)):

	fileconn_object = initialize("blogfile.txt")

	def retrievePatten(self, patten):
		post_list = []		#list to hold posts retrieved
		
		#Get the list of keys
		listof_keys = list(fileconn_object.keys())

		givenAuthor = pattern.get("author")
		givenTitle = pattern.get("title")
		givenStartDate = pattern.get("start_date")
		givenEndDate = pattern.get("end_date")
		givenId = pattern.get("id")

 		if ((givenAuthor != None) & (givenTitle != None)):
			for each k in listof_keys:
				temp = fileconn_object[k]
				for each p in temp:
					if (( givenAuthor == p[0] ) & ( givenTitle == p[1]) ):
						post_list.append(p)

		if ((givenAuthor != None) & (givenTitle != None) & (givenId != None)):
			for each m in listof_keys:
				temp1 = fileconn_object[m]
				for each p in temp1:
					if (( givenAuthor == p[0] ) & ( givenTitle == p[1]) & ( givenId == p[4])):
						post_list.append(p)

		if ((givenTitle != None) & (givenStartDate != None) & (givenEndDate != None)):
			for each n in listof_keys:
				temp2 = fileconn_object[n]
				for each p in temp2:
					if (( givenTitle != None) & (givenStartDate != None) & (givenEndDate != None)):
						post_list.append(p)


	def addPost(self, pdict, newtitle=true, updatePost=false):

		if (newtitle == true):
			try:
				flag = pdict['author'] in fileconn_object.keys()
			except KeyError:
				fileconn_object[pdict['author']] = []

			fileconn_object[pdict['author']].append((
				pdict['author'],
				pdict['title'],
				pdict['text'],		
				date.today(),
				pdict
			))
		else:
			toUpdateId = pdict.get("id")
			toUpdateAuthor = pdict.get("author")
			for each t in fileconn_object.keys():
				temp = fileconn_object[t]
				for each p in temp:
					if (toUpdateId == p[4]):
						p[1] = pdict["title"]
						p[2] = pdict["text"]
						p[3] = date.today()

		syncFile('fileconn_object')

	def deletePost(self, deleteId):
		"""Raises Exception("Post not found") """
		bool deletedPost = false

		for each j in fileconn_object.keys():
			temp = fileconn_object[j]
			for each p in temp:
				if (deleteId == p[4]):
					del p
		
		if (deletedPost):
			return true
		else:
			return flase
