import os, json
from datetime import datetime
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
nowDate = datetime.now().date().strftime("%y%m%d")

def create_pplayerFolder():
    if not os.path.exists("%s/players/players" % directory):
        os.mkdir("%s/players/players" % directory)
        print("folder created")
    else:
        print("already exists!")        

def create_pplayerJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_tmpLeagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/players/players/%s_%s_players.json" % (directory, nowDate,leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

create_pplayerFolder()
create_pplayerJson()


