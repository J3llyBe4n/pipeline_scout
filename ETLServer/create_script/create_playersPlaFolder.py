# 배치 주기 일주일
# 배치 아침에 돌아야함
#

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/players')
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) #
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")


today = datetime.datetime.today()
year, week_num, day_of_week = today.isocalendar()

# players/Players
def create_pPlayersFolder():
    if not os.path.exists("%s/Players" % directory):
        os.mkdir("%s/Players" % directory)
        print("folder created")
    else:
        print("already exists!")

# players/Players/YYYY
def create_pPlayersSeasonFolder():
    if not os.path.exists("%s/Players/%s" %(directory, now_Year)):
        os.mkdir("%s/Players/%s" %(directory, now_Year))
        print("folder created : %s" %now_Year)
    else:
        print("already exists")

# players/Players/YYYY/week_num
def create_pPlayersWeekFolder():
    if not os.path.exists("%s/Players/%s/%s" %(directory, now_Year, week_num)):
        os.mkdir("%s/Players/%s/%s" %(directory, now_Year, week_num))
        print("folder created")
    else:
        print("alreday exists")

# players/Players/YYYY/week_num/leagueId_players.json
def create_pPlayersJson():
    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB league_id 리스트 반환 
    tmp_leagueId = db_func.read_tmpLeagueId()

    print(tmp_leagueId)

    for i in tmp_leagueId:
        leagueId = i 
        file_path = "%s/Players/%s/%s/%s_players.json" % (directory, now_Year, week_num, leagueId)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)



create_pPlayersFolder()
create_pPlayersSeasonFolder()
create_pPlayersWeekFolder()
create_pPlayersJson()
