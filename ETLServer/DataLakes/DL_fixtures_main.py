# db 서버에서 league id 리스트로 반환
# 해당 리스트 적재 후, 리그별로, fixture 데이터 받아옴
# json 이름 라벨링 후 데이터 적재
# req log 남기기

from ETLServer.Modules.db_function import * 
from ETLServer.Modules.DL_api_function import * 

#api_keys = "a68636f8f2c18511179c56f15e95080c"
api_keys = 'a86d420d0d8840c8e722e16cf9742f7b'
# api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

#db 관련func 내장 class 생성
db_func = DBfunc()

apiFunc = ApiFixtures()

#db 서버 열어주기
db_func.connect_SQL()

#league_id 불러오기
tmp_leagueId = db_func.read_tmpLeagueId()

#json 파일 로드 하고 로컬에 관리해주기
apiFunc.load_fixtureJson(tmp_leagueId, api_keys)


