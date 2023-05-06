#배치 주기 1년
# 시즌 시작할떄 다 돌아가야함
#

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/teams')
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) #
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")

# teams/Info
def create_teamsInfoFolder():
    if not os.path.exists("%s/Info" % directory):
        os.mkdir("%s/Info" % directory)
        print("folder created")
    else:
        print("already exists!")

# teams/Info/YYYY
def create_teamsInfoSeasonFolder():
    if not os.path.exists("%s/Info/%s" %(directory, now_Year)):
        os.mkdir("%s/Info/%s" %(directory, now_Year))
        print("folder created")
    else:
        print("already exists")

# teams/Info/YYYY/leagueId_Tinfo.json
def create_teamsInfoJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_leagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/Info/%s/%s_Tinfo.json" % (directory, now_Year, leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)



create_teamsInfoFolder()
create_teamsInfoSeasonFolder()
create_teamsInfoJson()