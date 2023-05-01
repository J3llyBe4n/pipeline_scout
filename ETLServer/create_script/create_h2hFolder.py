#배치 주기 매일 
#데이터 들어가기 전에 스크립트가 돌아가야함.

import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')
nowYear = datetime.datetime.utcnow().date().strftime("%Y")
nowDate = datetime.datetime.utcnow().date().strftime("%y%m%d")
nowYear = int(nowYear) - 1


def create_h2hFolder():
    if not os.path.exists("%s/H2h" %directory):
        os.mkdir("%s/H2h" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_seasonH2hFolder():
    if not os.path.exists("%s/h2h/%s" %(directory, nowYear)):
        os.mkdir("%s/h2h/%s" %(directory, nowYear))
        print("folder created! : %s" %nowYear)
    else:
        print("already exists")


def create_h2hJson():
    file_path = "%s/h2h/%s/%s_h2h.json" % (directory,nowYear, nowDate)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
        
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


create_h2hFolder()
create_seasonH2hFolder()
create_h2hJson()



