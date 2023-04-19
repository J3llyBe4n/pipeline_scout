import mysql.connector

class DBfunc:

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

	def insertPipeLeagueData(self,data):

		for i in range(len(data)):
			insertDataList = []
			insertDataList.append(data[i]['league_name'])
			insertDataList.append(data[i]['api_league_id'])
			insertDataList.append(data[i]['nation_name'])
			insertSql = 'insert into pipe_league (league_name, api_league_id,league_nation) values ("%s",%d,"%s")' %(insertDataList[0],insertDataList[1],insertDataList[2])
			self.cursor.execute(insertSql)
			# print("insert Done!")
		 	self.conn.commit()

