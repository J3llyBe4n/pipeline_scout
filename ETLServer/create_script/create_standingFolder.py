# 배치 주기는 매일
# 배치는 매일 경기 끝나느 저녁에 돌아야함

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake')
now_year = datetime.datetime.utcnow().date().strftime("%Y")
nowDate = datetime.datetime.utcnow().date().strftime("%y%m%d")
now_year = int(now_year) - 1 


def create_standingFolder():
    if not os.path.exists("%s/standings" %directory):
        os.mkdir("%s/standings" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_seasonStandingFolder():
    if not os.path.exists("%s/standings/%s" %(directory, now_year)):
        os.mkdir("%s/standings/%s" %(directory, now_year))
        print("folder created")
    else:
        print("already exists!")


def create_standingJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_tmpLeagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/standings/%s/%s_standing.json" % (directory, now_year,nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_standingFolder()
create_seasonStandingFolder()
create_standingJson()




