
# 모듈 import(공통)
import sys
sys.path.append('../')
from Modules.db_function import *
from Modules.DL_api_function import * 

# API keys
api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

# db관련 func class 생성(공통)
dbFunc = DBfunc()

# api 관련 func class 생성
# DL_api_function에 클래스 추가 : ApiPtopscoreres
apiFunc = ApiPtopscoreres()

# db server에 연결(공통)
dbFunc.connect_SQL()

# db server에서 leauge_id 불러오기
# 필요한 리스트 : 리그 id
tmp_leagueId = dbFunc.read_leagueId()

# apiFunc 에서 req 함수 call
# DL_api_function에 함수 추가 : load_ptopscorersJson
apiFunc.load_ptopscorersJson(tmp_leagueId, api_keys)
