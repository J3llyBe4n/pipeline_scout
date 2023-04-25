# db 서버에서 league id 리스트로 반환
# 해당 리스트 적재 후, 리그별로, fixture 데이터 받아옴
# json 이름 라벨링 후 데이터 적재
# req log 남기기

from ETLServer.Modules.db_func import *

#db 관련func 내장 class 생성
db_func = DBfunc()

#db 서버 열어주기
db_func.connectSQLServer()

#league_id 불러오기
league_id = db_func.readTmpID()



