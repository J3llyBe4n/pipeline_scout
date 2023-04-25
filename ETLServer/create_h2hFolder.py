import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake', 'fixtures')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")


def create_h2hFolder():
    if not os.path.exists("%s/h2h" %directory):
        os.mkdir("%s/h2h" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_h2hDayFolder():
    if not os.path.exists("%s/h2h/%s" %(directory, nowDate)):
        os.mkdir("%s/h2h/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
    else:
        print("already exists")


def create_h2hJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_tmpLeagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/h2h/%s_%s_h2h.json" % (directory, nowDate,leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_h2hFolder()
create_h2hDayFolder()
create_h2hJson()



