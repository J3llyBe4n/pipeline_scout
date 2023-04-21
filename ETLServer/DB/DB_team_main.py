import requests
from ETLServer.Modules.api_func import ApiTeamBlock
from ETLServer.Modules.db_func import DBfunc

api_keys = "a68636f8f2c18511179c56f15e95080c"

#db func 불러오기 위해서 class 생성 
DB_func = DBfunc()

#api_func 불러오기 위해서 class 생성
api_func = ApiTeamBlock()

#기능 실행 [sql server 붙이기] 
DB_func.connectSQLServer()

#기능 실행 [sql server에서 적재되어있는 api_league_id 리스트 적재]
tempId = DB_func.readLeagueId()

#기능 실행 [적재한 league_id 를 통해 team id 가 적재 되어있는 api call 하여 필요한 데이터 만들기]
tempAPI = api_func.loadTeamData(tempId, api_keys)

#print(tempAPI)

#teamAPI 내에 데이터중에 필요한 부분만 extract
dicList = api_func.transformTeamData(tempAPI)

#가공된 데이터를 db로 밀어넣기
DB_func.insertPipeTeamData(dicList)

DB_func.closeSQLServer()





