# db server에서 55개 리그id 리스트 적재 
# 해당 리그id 리스트를 통해 for 문으로, api request
# 해당 불러온 데이터 json으로 datas/DataLake/39_220424_standings.json으로 적재까지!

from ETLServer.Modules.db_func import *
from ETLServer.Modules.DL_api_func import * 

api_keys = "a68636f8f2c18511179c56f15e95080c"

#db관련 func class 생성
dbFunc = DBfunc()

#api 관련 func class 생성
apiFunc = ApiStandings()

#db server에 연결 
dbFunc.connectSQLServer()

#db server에서 leauge_id 불러오기 
tmp_leagueId = dbFunc.readTmpID()

#apiFunc 에서 req 함수 call
apiFunc.load_standingJson(tmp_leagueId, api_keys)





