from ETLServer.Modules.db_function import * 
from ETLServer.Modules.DL_api_function import * 
import datetime

now_date = datetime.datetime.utcnow().date().strftime("%Y-%m-%d")

#api_keys = "a68636f8f2c18511179c56f15e95080c"
api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'
# api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

db_func = DBfunc()
api_func = ApiPredictions()

db_func.connect_SQL()

fixture_id = db_func.read_fixtureId(now_date)

api_func.load_predictionsJson(fixture_id, api_keys)

db_func.close_SQL()