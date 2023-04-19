import mysql.connector

class DB:

	def connectSQLServer(self):
		self.conn = mysql.connector.connect(user='root', password= 'tmzkdnxj1', host='34.64.214.96', database = 'scout', port = '3306')
		print("Hi! SQL")
		self.cursor = self.conn.cursor()

	def closeSQLServer(self):
		self.conn.close()
		print("BYE! SQL")


	def readTmpID(self):
		listID = []

		readQuery = 'select * from tmp_league'
		self.cursor.execute(readQuery)
		tmpListRaw = self.cursor.fetchall()
		for i in range(len(tmpListRaw)):
			listID.append(tmpListRaw[i][0])

		return listID


database = DB()

database.connectSQLServer()
ttt = database.readTmpID()
print(ttt)
