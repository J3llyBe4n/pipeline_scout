# 이놈은 매일 돌아야하는 스크립트 입니다. 
# 이놈은 데이터가 들어가기 이전에, 아침에 돌아야합니다.

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')
nowYear = datetime.datetime.now().date().strftime("%Y")
nowDate = datetime.datetime.now().date().strftime("%y%m%d")
nowYear = int(nowYear) -1


def create_fixturePStatsFolder():
    if not os.path.exists("%s/Pstatistics" %directory):
        os.mkdir("%s/Pstatistics" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_fixturePStatsDayFolder():
    if not os.path.exists("%s/Pstatistics/%s" %(directory, nowYear)):
        os.mkdir("%s/Pstatistics/%s" %(directory, nowYear))
        print("folder created! : %s" %nowYear)
    else:
        print("already exists")


def create_fixturePStatsJson():

        file_path = "%s/Pstatistics/%s/%s_Pstatistics.json" % (directory,nowYear, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_fixturePStatsFolder()
create_fixturePStatsDayFolder()
create_fixturePStatsJson()