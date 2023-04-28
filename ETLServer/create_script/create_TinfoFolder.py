#배치 주기 1년
# 시즌 시작할떄 다 돌아가야함


import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")
now_year = datetime.datetime.now().date().strftime("%Y")
now_year = int(now_year) - 1

def create_teamsFolder():
    if not os.path.exists("%s/teams" % directory):
        os.mkdir("%s/teams" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_teamsInfoFolder():
    if not os.path.exists("%s/teams/Teams_info" % directory):
        os.mkdir("%s/teams/Teams_info" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_seasonTeamFolder():
    if not os.path.exists("%s/teams/Teams_info/%s" %(directory, now_year)):
        os.mkdir("%s/teams/Teams_info/%s" %(directory, now_year))
        print("folder created")
    else:
        print("already exists")

def create_teamsInfoJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_leagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/teams/teams_info/%s/%s_Tinfo.json" % (directory, now_year,leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

# create_teamsFolder()
if __name__ == "__main__":
    create_teamsFolder()
    create_teamsInfoFolder()
    create_seasonTeamFolder()
    create_teamsInfoJson()