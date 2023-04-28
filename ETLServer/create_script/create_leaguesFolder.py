# 해당 배치 주기는 1년입니다.
# 시즌이 시작하기 전에 한번 돌아야합니다.

import os
from datetime import datetime
import json
from ETLServer.Modules.db_function import *
# from Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake')
now_date = datetime.utcnow().date().strftime("%y%m%d")

seasons = 2022

def create_baseLeaguesFolder():
    if not os.path.exists("%s/leagues" % directory):
        os.mkdir("%s/leagues" % directory)
        print("folder created")
    else:
        print("already exists!")


def create_seasonLeagueFolder():
    if not os.path.exists("%s/leagues/%s" %(directory, seasons)):
        os.mkdir("%s/leagues/%s" %(directory, seasons))
        print("folder created")
    else:
        print("already exists")


def create_leaguesJson():

    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_tmpLeagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/leagues/%s/%s_leagueInfo.json" % (directory, seasons, leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_baseLeaguesFolder()
create_seasonLeagueFolder()
create_leaguesJson()
