from ETLServer.Modules.db_function import *
from ETLServer.Modules.DL_api_function import *
import datetime

api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'

db_func = DBfunc()

api_func = ApiCoachs()

db_func.connect_SQL()

tmp_TeamLeagueId = db_func.read_LeagueTeamId()

api_func.load_coachsJson(tmp_TeamLeagueId,api_keys)

db_func.close_SQL()