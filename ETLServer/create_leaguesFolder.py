import os
from datetime import datetime
import json
# from ETLServer.Modules.db_function import *
# from Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
now_date = datetime.utcnow().date().strftime("%y%m%d")

seasons = 2022

def create_leaguesFolder():
    if not os.path.exists("%s/leagues" % directory):
        os.mkdir("%s/leagues" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_leaguesJson(tmp_leagueId):

    for i in tmp_leagueId:
        league_id = i
        file_path = "%s/leagues/%s_%s_leagues.json" % (directory, now_date, league_id)
        data = {'data' : []}
            
        if os.path.exists(file_path):
            print("file exists")
            
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

# create_teamsFolder()
if __name__ == "__main__":

    from Modules.db_function import *
    from Modules.DL_api_function import * 

    dbFunc = DBfunc()
    dbFunc.connect_SQL()
    tmp_leagueId = dbFunc.read_leagueId()

    create_leaguesFolder()
    create_leaguesJson(tmp_leagueId)