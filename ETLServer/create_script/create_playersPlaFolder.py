# 배치 주기 일주일
# 배치 아침에 돌아야함

import os, json, datetime
from datetime import datetime
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake')
nowDate = datetime.now().date().strftime("%y%m%d")
now_year = datetime.now().date().strftime("%Y")
now_year = int(now_year) - 1


today = datetime.today()
year, week_num, day_of_week = today.isocalendar()


def create_pplayerFolder():
    if not os.path.exists("%s/players/Players" % directory):
        os.mkdir("%s/players/Players" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_seasonpPlayerFolder():
    if not os.path.exists("%s/players/Players/%s" %(directory, now_year)):
        os.mkdir("%s/players/Players/%s" %(directory, now_year))
        print("folder created : %s" %now_year)
    else:
        print("already exists")

def create_weekPlayerFolder():
    if not os.path.exists("%s/players/Players/%s/%s" %(directory, now_year, week_num)):
        os.mkdir("%s/players/Players/%s/%s" %(directory, now_year, week_num))
        print("folder created")
    else:
        print("alreday exists")


def create_pplayerJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_tmpLeagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/players/players/%s/%s/%s_players.json" % (directory, now_year, week_num,leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)



create_pplayerFolder()
create_seasonpPlayerFolder()
create_weekPlayerFolder()
create_pplayerJson()
