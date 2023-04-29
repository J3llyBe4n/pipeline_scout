import sys #
sys.path.append('../') #
from Modules.db_function import * #
from Modules.DL_api_function import * #
import datetime

api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'

db_func = DBfunc()

api_func = ApiFixtureStats()

db_func.connect_SQL()

gmt_nowDate = datetime.datetime.utcnow().date().strftime('%Y-%m-%d')
fixture_id = db_func.read_fixtureId(gmt_nowDate)

api_func.load_fixtureStatsJson(fixture_id,api_keys)

db_func.close_SQL()