#db 열기
#당일 fixture 데이터 쪽 빨아오기
#fixture 데이터 기반으로 api call
#들어온 data 형태에 맞춰서 적재

from datetime import datetime
from ETLServer.Modules.db_function import *

now_date = datetime.now().date().strftime("%Y-%m-%d")

api_keys = "a68636f8f2c18511179c56f15e95080c"

db_func = DBfunc()

db_func.connect_SQL()

fixture_id = db_func.read_fixtureId(now_date)
print(fixture_id)
