import os
import datetime
import json
from ETLServer.Modules.db_func import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")


def create_standingFolder():
    if not os.path.exists("%s/standings" %directory):
        os.mkdir("%s/standings" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_standingJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connectSQLServer()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.readTmpID()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/standings/%s_%s_standing.json" % (directory, nowDate,leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_standingFolder()
create_standingJson()




