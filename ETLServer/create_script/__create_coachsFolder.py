import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
now_date = datetime.datetime.utcnow().date().strftime("%y%m%d")

def create_coachsFolder():
    if not os.path.exists("%s/coachs" % directory):
        os.mkdir("%s/coachs" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_coachsDayFolder():
    if not os.path.exists("%s/coachs/%s" %(directory, now_date)):
        os.mkdir("%s/coachs/%s" %(directory, now_date))
        print("folder created! : %s" %now_date)
    else:
        print("already exists")

def create_coachsJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_leagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/coachs/%s/%s_%s_coachs.json" % (directory, now_date, now_date, leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

create_coachsFolder()
create_coachsDayFolder()
create_coachsJson()