import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")

def create_teamsFolder():
    if not os.path.exists("%s/teams" % directory):
        os.mkdir("%s/teams" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_teamsStatisticsFolder():
    if not os.path.exists("%s/teams/statistics" % directory):
        os.mkdir("%s/teams/statistics" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_teamStatisticsDayFolder():
    if not os.path.exists("%s/h2h/%s" %(directory, nowDate)):
        os.mkdir("%s/teams/statistics/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
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
        file_path = "%s/teams/statistics/%s/%s_%s_Tstats.json" % (directory, nowDate, nowDate, leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

# create_teamsFolder()
create_teamsStatisticsFolder()
create_teamStatisticsDayFolder()
create_teamStatisticsJson()