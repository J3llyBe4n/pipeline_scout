# 해당 배치 주기는 1년입니다.
# 시즌이 시작하기 전에 한번 돌아야합니다.
#

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/leagues')
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) #
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")

# leagues/YYYY
def create_leaguesSeasonFolder():
    if not os.path.exists("%s/%s" %(directory, now_Year)):
        os.mkdir("%s/%s" %(directory, now_Year))
        print("folder created")
    else:
        print("already exists")

# leagues/YYYY/leagueId_leagueInfo.json
def create_leaguesJson():

    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_leagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/%s/%s_leagueInfo.json" % (directory, now_Year, leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_leaguesSeasonFolder()
create_leaguesJson()