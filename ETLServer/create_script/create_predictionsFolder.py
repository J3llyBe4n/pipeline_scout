# 배치 주기는 매일
# 경기 전에 돌아야하기 때문에 아침에 돌아야함

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake')
now_date = datetime.datetime.utcnow().date().strftime("%y%m%d")
now_year = datetime.datetime.now().date().strftime("%Y")
now_year = int(now_year) - 1

def create_predictionsFolder():
    if not os.path.exists("%s/predictions" %directory):
        os.mkdir("%s/predictions" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_predictionsSeasonFolder():
    if not os.path.exists("%s/predictions/%s" %(directory, now_year)):
        os.mkdir("%s/predictions/%s" %(directory, now_year))
        print("folder created! : %s" %now_year)
    else:
        print("already exists")

def create_predictionsJson():
    file_path = "%s/predictions/%s/%s_predictions.json" % (directory, now_year, now_date)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
    
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

create_predictionsFolder()
create_predictionsSeasonFolder()
create_predictionsJson()
