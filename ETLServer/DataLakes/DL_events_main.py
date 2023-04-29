# db 열기 
# pipe_round 테이블에서 오늘 축구 경기 쫙 다 빨아오기 
# 해당 경기 fixture id 값 리스트로 반환
# fixture를 기반으로 json에 붙여넣기
# 그날 00시에 돌면 해당 경기 데이터를 받아올 수 가없음 따라서, 해당 경기 날 경기가 다 끝나는 시간 ex 해당날 밤 11:30 분 이런식으로 배치를 돌려야함

import sys #
sys.path.append('../') #
from Modules.db_function import * #
from Modules.DL_api_function import * #
from datetime import datetime

now_date = datetime.now().date().strftime("%Y-%m-%d")

api_keys = "a68636f8f2c18511179c56f15e95080c"

db_func = DBfunc()
api_func = ApiEvents()

db_func.connect_SQL()

fixture_id = db_func.read_fixtureId(now_date)

api_func.load_eventsJson(fixture_id, api_keys)


