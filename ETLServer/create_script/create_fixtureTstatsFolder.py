#배치 주기 매일
#데이터 들어가는 스크립트 돌기전에 아침에 돌아야함 

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')
nowYear = datetime.datetime.utcnow().date().strftime("%Y")
nowDate = datetime.datetime.utcnow().date().strftime("%y%m%d")
nowYear = int(nowYear) - 1


def create_fixtureTstatsFolder():
    if not os.path.exists("%s/Tstatistics" %directory):
        os.mkdir("%s/Tstatistics" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_seasonFixtureTstatsFolder():
    if not os.path.exists("%s/Tstatistics/%s" %(directory, nowYear)):
        os.mkdir("%s/Tstatistics/%s" %(directory, nowYear))
        print("folder created! : %s" %nowYear)
    else:
        print("already exists")


def create_fixtureTstatsJson():

        file_path = "%s/Tstatistics/%s/%s_Ftstats.json" % (directory, nowYear, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_fixtureTstatsFolder()
create_seasonFixtureTstatsFolder()
create_fixtureTstatsJson()