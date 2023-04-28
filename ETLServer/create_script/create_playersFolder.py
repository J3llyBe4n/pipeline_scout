#배치 주기 복잡 이야기해야함
# 아침에 돌아야함

import os, json
from datetime import datetime

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake')
now_date = datetime.utcnow().date().strftime("%y%m%d")

seasons = 2022

def create_basePlayersFolder():
    if not os.path.exists("%s/players" % directory):
        os.mkdir("%s/players" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_pTopscorersFolder():
    if not os.path.exists("%s/players/Topscorers" % directory):
        os.mkdir("%s/players/Topscorers" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_pSquadsFolder():
    if not os.path.exists("%s/players/Squads" % directory):
        os.mkdir("%s/players/Squads" % directory)
        print("folder created")
    else:
        print("already exists!")


def create_seasonSquadFolder():
    if not os.path.exists("%s/players/Squads/%s" %(directory, seasons)):
        os.mkdir("%s/players/Squads/%s" %(directory, seasons))
        print("folder created")
    else:
        print("already exists!")

def create_seasonTopscorersFolder():
    if not os.path.exists("%s/players/Topscorers/%s" %(directory, seasons)):
        os.mkdir("%s/players/Topscorers/%s" %(directory, seasons))
        print("folder created : %s" %seasons)
    else:
        print("already exists")


def create_SquadJson(tmp_teamId):

    for i in tmp_teamId:
        team_id = i
        file_path = "%s/players/Squads/%s/%s_Psquad.json" % (directory, seasons, team_id)
        data = {'data' : []}
            
        if os.path.exists(file_path):
            print("file exists")
            
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

def create_ptopscorersJson(tmp_leagueId):

    for i in tmp_leagueId:
        league_id = i
        file_path = "%s/players/Topscorers/%s/%s_Ptopscorers.json" % (directory, seasons, league_id)
        data = {'data' : []}
            
        if os.path.exists(file_path):
            print("file exists")
            
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


if __name__ == "__main__":

    from ETLServer.Modules.db_function import *
    from ETLServer.Modules.DL_api_function import * 

    dbFunc = DBfunc()
    dbFunc.connect_SQL()
    tmp_teamId = dbFunc.read_teamId()
    tmp_leagueId = dbFunc.read_leagueId()


    create_basePlayersFolder()
    create_pTopscorersFolder()
    create_pSquadsFolder()
    create_seasonSquadFolder()
    create_seasonTopscorersFolder()
    create_SquadJson(tmp_teamId)
    create_ptopscorersJson(tmp_leagueId)