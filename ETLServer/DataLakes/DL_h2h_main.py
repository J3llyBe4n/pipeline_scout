# Db 서버 열기
# pipe_round table 내에 경기가 오늘 날짜인 데이터 다 빨아오기 homeid - awayid
# 위에서 만든 리스트를 파라미터로 가져가 h2h api call 하여서 받는 데이터 맞는 json에 적재 하기
# task가 다 돌면 batch 내부에 json 파일 날려주기
# 서버 닫기


from ETLServer.Modules.db_function import * 
from ETLServer.Modules.DL_api_function import * 
from datetime import datetime

api_keys = "a68636f8f2c18511179c56f15e95080c"

db_func = DBfunc()
api_func = ApiH2h()

db_func.connect_SQL()

now_date = datetime.now().date().strftime("%Y_%m_%d")
print(now_date)

round_data = db_func.read_roundInfo(now_date)

api_func.load_h2hJson(round_data, api_keys)












