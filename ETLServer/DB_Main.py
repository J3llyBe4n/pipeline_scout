import requests
from DB_func import *
from Api_func import *

api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

DB_Func = DBfunc()
print("test")
API_Func = API_block()

DB_Func.connectSQLServer()

tempId = DB_Func.readTmpID()
print("test")

cnt, tempAPI = API_Func.load_pipe_league_API(tempId, api_keys)

dicList = API_Func.tmp_pipe_league_API(tempAPI)

DB_Func.insertPipeLeagueData(dicList)

DB_Func.closeSQLServer()
