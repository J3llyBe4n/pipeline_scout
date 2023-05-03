#
#
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

# players/Squads
def create_pSquadsFolder():
    if not os.path.exists("%s/Squads" % directory):
        os.mkdir("%s/Squads" % directory)
        print("folder created")
    else:
        print("already exists!")

# players/Squads/YYYY
def create_pSquadsSeasonFolder():
    if not os.path.exists("%s/Squads/%s" %(directory, now_Year)):
        os.mkdir("%s/Squads/%s" %(directory, now_Year))
        print("folder created")
    else:
        print("already exists!")

# players/Squads/YYYY/teamId_Psquad.json
def create_pSquadsJson():

    db_func = DBfunc()

    #DB server연결 
    db_func.connect_SQL()

    #DB team_id 리스트 반환 
    tmp_teamId = db_func.read_teamId()

    print(tmp_teamId)
    for i in tmp_teamId:
        team_id = i
        file_path = "%s/Squads/%s/%s_Psquad.json" % (directory, now_Year, team_id)
        data = {'data' : []}
            
        if os.path.exists(file_path):
            print("file exists")
            
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_pSquadsFolder()
create_pSquadsSeasonFolder()
create_pSquadsJson()