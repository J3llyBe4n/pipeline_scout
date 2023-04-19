def insertPipeLeagueData(self,data):
    for i in range(len(data)):
        insertDataList = []
        insertDataList.append(data[i]['리그명'])
        insertDataList.append(data[i]['api_league_id'])
        insertDataList.append(data[i]['국가명'])
        insertSql = 'insert into pipe_league (league_name, api_league_id,league_nation) values ("%s",%d,"%s")' %(insertDataList[0],insertDataList[1],insertDataList[2])
        self.cursor.excute(insertSql)
        # print("insert Done!")
        self.conn.commit()