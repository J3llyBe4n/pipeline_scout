#이놈은 1시즌에 한번 도는 놈입니다. 
#시즌 시작날 기준으로 해당 스크립트가 돌아야합니다.

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), "../datas/DataLake")
nowDate = datetime.datetime.utcnow().date().strftime("%y%m%d")
nowDate = str(int(nowDate) - 1 )

def create_fixtureBaseFolder():
    if not os.path.exists("%s/fixtures" %directory):
        os.mkdir("%s/fixtures" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_seasonFixtureFolder():
    if not os.path.exists("%s/fixtures/fixtures/2022" %directory):
        os.mkdir("%s/fixtures/fixtures/2022" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_fixtureFolder():
    if not os.path.exists("%s/fixtures/fixtures" %directory):
        os.mkdir("%s/fixtures/fixtures" %directory)
        print("folder created!")
    else:
        print("already exists!")

def create_fixtureJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_tmpLeagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/fixtures/fixtures/2022/%s_%s_fixture.json" % (directory, nowDate,leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_fixtureBaseFolder()
create_fixtureFolder()
create_seasonFixtureFolder()
create_fixtureJson()