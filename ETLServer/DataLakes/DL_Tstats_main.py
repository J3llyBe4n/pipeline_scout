from ETLServer.Modules.db_function import *
from ETLServer.Modules.DL_api_function import *
import datetime

api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'

db_func = DBfunc()

apiFunc = ApiTeamStatistics()

#db 서버 열어주기
db_func.connect_SQL()

tmp_TeamLeagueId = db_func.read_LeagueTeamId()

gmt_nowDate = datetime.datetime.utcnow().date().strftime('%Y-%m-%d')
print(gmt_nowDate)

#json 파일 로드 하고 로컬에 관리해주기
apiFunc.Api_TstatsJson(tmp_TeamLeagueId, api_keys, round_date=gmt_nowDate)

db_func.close_SQL()