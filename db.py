import sqlite3
#Важное Примечание!!!!!!
#Добавь в базе данных чтобы дата сама автоматически выставлялась на уровне бд.
class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file)
		self.cursor = self.connection.cursor()

	def add_user(self, user_id):
		with self.connection:
			return self.cursor.execute("INSERT INTO 'database' ('user_id') VALUES (?)", (user_id,))

	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM 'database' WHERE 'user_id' = ?", (user_id,)).fetchall()
			if result:
				return True
			else:
				return False
			

	def set_nickname(self, user_id, nickname):
		with self.connection:
			return self.cursor.execute("UPDATE `database` SET `nickname` = ? WHERE `user_id` = ?", (nickname, user_id,))

	def get_signup(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT `signup` FROM `database` WHERE `user_id` = ?", (user_id,)).fetchall()
			for row in result:
				signup = str(row[0])
			return signup

	def set_signup(self, user_id, signup):
		with self.connection:
			return self.cursor.execute("UPDATE `database` SET `signup` = ? WHERE `user_id` =?", (signup, user_id,))

	def set_message(self, user_id, msg):
		with self.connection:
			return self.cursor.execute("UPDATE `database` SET `message` = ? WHERE `user_id` =?", (msg, user_id,))

	def get_nickname(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT `nickname` FROM `database` WHERE `user_id` = ?", (user_id,)).fetchall()
			for row in result:
				nickname = str(row[0])
			return nickname
