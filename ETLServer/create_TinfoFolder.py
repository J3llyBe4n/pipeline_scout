import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
nowDate = datetime.datetime.now().date().strftime("%Y_%m_%d")

def create_teamsInfoFolder():
    if not os.path.exists("%s/teams/teams_info" % directory):
        os.mkdir("%s/teams/teams_info" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_teamsInfoJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_leagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/teams/teams_info/%s_%s_Tinfo.json" % (directory, nowDate,leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

# create_teamsFolder()
if __name__ == "__main__":
    create_teamsInfoFolder()
    create_teamsInfoJson()