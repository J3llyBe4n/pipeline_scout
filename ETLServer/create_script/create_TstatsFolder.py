# 배치 주기 매일
# 배치 경기 다 끝나고 돌아야함

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

def create_teamsStatisticsFolder():
    if not os.path.exists("%s/teams/Statistics" % directory):
        os.mkdir("%s/teams/Statistics" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_seasonTeamsStatisticsFolder():
    if not os.path.exists("%s/teams/Statistics/%s" %(directory, now_year)):
        os.mkdir("%s/teams/Statistics/%s" %(directory, now_year))
        print("folder created")
    else:
        print("already exists")


def create_teamStatisticsJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_leagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/teams/statistics/%s/%s_Tstats.json" % (directory, now_year, leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

create_teamsFolder()
create_teamsStatisticsFolder()
create_seasonTeamsStatisticsFolder()
create_teamStatisticsJson()