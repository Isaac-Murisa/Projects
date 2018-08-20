import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
		flaskr.app.testing = True
		self.app = flaskr.app.test_client()
		with flaskr.app.app_context():
			flaskr.init_db()
	
	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(flaskr.app.config['DATABASE'])
		
	def Username(self, username):
		return self.app.post('/security', data=dict(
			usr = username), follow_redirects=True)
	
	
	#test if the user is not in the database or wrong user name provided.
	def test_user(self):
		rv = self.Username('default')
		assert b'Wrong username' in rv.data
		rv  = self.Username('icm')
		assert b'Answer question' in rv.data
	
	#test answer input wrong and correct answers
	def test_uestion(self):
		self.Username('icm')
		rv = self.app.post('/question', data=dict(
			userAnswer = 'Isaac'), follow_redirects=True)
		assert b'Enter new password' in rv.data
		rv = self.app.post('/question', data=dict(
			useranswer = 'MeAgain'), follow_redirects=True)
		assert b'Try Again' in rv.data
	
if __name__ == '__main__':
	unittest.main()