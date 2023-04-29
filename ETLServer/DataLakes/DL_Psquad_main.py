from ETLServer.Modules.db_function import * 
from ETLServer.Modules.DL_api_function import * 

api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

#db관련 func class 생성
dbFunc = DBfunc()

#api 관련 func class 생성
apiFunc = ApiPsquad()

#db server에 연결 
dbFunc.connect_SQL()

#db server에서 leauge_id 불러오기 
tmp_teamId = dbFunc.read_teamId()

#apiFunc 에서 req 함수 call
apiFunc.load_psquadJson(tmp_teamId, api_keys)