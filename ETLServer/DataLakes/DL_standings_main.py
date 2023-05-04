# db server에서 55개 리그id 리스트 적재 
# 해당 리그id 리스트를 통해 for 문으로, api request
# 해당 불러온 데이터 json으로 datas/DataLake/39_220424_standings.json으로 적재까지!

import sys
sys.path.append('../')
# visual code가 추가한 경로만 인식해서 모듈을 불러오기 위해 임의로 상위 폴더 경로를 박았어요

from ETLServer.Modules.db_function import *
from ETLServer.Modules.DL_api_function import *

# from ETLServer.Modules.db_function import *
# from ETLServer.Modules.DL_api_function import * 

#api_keys = "a68636f8f2c18511179c56f15e95080c"
api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'
# api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

#db관련 func class 생성
dbFunc = DBfunc()

#api 관련 func class 생성
apiFunc = ApiStandings()

#db server에 연결 
dbFunc.connect_SQL()

#db server에서 leauge_id 불러오기 
tmp_leagueId = dbFunc.read_tmpLeagueId()

#apiFunc 에서 req 함수 call
apiFunc.load_standingJson(tmp_leagueId, api_keys)





