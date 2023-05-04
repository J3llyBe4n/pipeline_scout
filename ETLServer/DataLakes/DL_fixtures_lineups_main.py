#db 열기
#당일 fixture 데이터 쪽 빨아오기
#fixture 데이터 기반으로 api call
#들어온 data 형태에 맞춰서 적재

from ETLServer.Modules.db_function import * 
from ETLServer.Modules.DL_api_function import *
from datetime import datetime, timedelta

now_date = datetime.utcnow().date().strftime("%Y-%m-%d")

################## 테스트 블록 전날 데이터
yesterday = (datetime.utcnow().date() - timedelta(days=1)).strftime("%Y-%m-%d")
##############

#api_keys = "a68636f8f2c18511179c56f15e95080c"
api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'
# api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

db_func = DBfunc()
api_func = ApiFixtureLineups()

db_func.connect_SQL()

fixture_id = db_func.read_fixtureId(yesterday)
api_func.load_lineUpsJson(fixture_id, api_keys)

#fixture_id = db_func.read_fixtureId(now_date)
#print(fixture_id)
#api_func.load_lineUpsJson(fixture_id, api_keys)
