
#db 열기 
#db 리그 55개의 팀 리스트를 이중 dictionary로 가져오기
# 해당 리스트를 반환받고, page 갯수 만큼 loop 돌아야하고,
# 팀 하나 다 돌고 30초 쉬고 하는 형태로 돌리기 팀 한개당 3개 정도 req가 필요하고 20개 팀이라 가정시 총 60개의 req가 소모되기 때문에
# 리그 하나 돌고 쿨타임 만들고 하는 형태로 운영하면 될듯

from ETLServer.Modules.db_function import * 
from ETLServer.Modules.DL_api_function import * 

api_keys = "a68636f8f2c18511179c56f15e95080c"

db_func = DBfunc()
api_func = ApiPlayerPlayers()

db_func.connect_SQL()

teamId = db_func.read_tlId()

api_func.load_pplayerJson(teamId, api_keys)




