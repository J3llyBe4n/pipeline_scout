from ETLServer.Modules.db_function import *
from ETLServer.Modules.DL_api_function import *
import datetime

api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'

db_func = DBfunc()

api_func = ApiFixtureTStats()

db_func.connect_SQL()

gmt_nowDate = datetime.datetime.utcnow().date().strftime('%Y-%m-%d')
fixture_id = db_func.read_fixtureId(gmt_nowDate)

api_func.load_fixtureTStatsJson(fixture_id,api_keys)

db_func.close_SQL()