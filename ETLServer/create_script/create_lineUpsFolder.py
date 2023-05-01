# 배치 주기는 1일입니다.
# 아침에 돌아야합니다. 

import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')
now_year = datetime.datetime.utcnow().date().strftime("%Y")
nowDate = datetime.datetime.utcnow().date().strftime("%y%m%d")
now_year = int(now_year) - 1

def create_lineUpsFolder():
    if not os.path.exists("%s/lineups" %directory):
        os.mkdir("%s/lineups" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_seasonsLineUpsFolder():
    if not os.path.exists("%s/lineups/%s" %(directory, now_year)):
        os.mkdir("%s/lineups/%s" %(directory, now_year))
        print("folder created! : %s" %now_year)
    else:
        print("already exists")


def create_lineUpsJson():

        file_path = "%s/lineups/%s/%s_lineUps.json" % (directory, now_year, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_lineUpsFolder()
create_seasonsLineUpsFolder()
create_lineUpsJson()