import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake', 'fixtures')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")


def create_fixturePStatsFolder():
    if not os.path.exists("%s/Pstatistics" %directory):
        os.mkdir("%s/Pstatistics" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_fixturePStatsDayFolder():
    if not os.path.exists("%s/Pstatistics/%s" %(directory, nowDate)):
        os.mkdir("%s/Pstatistics/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
    else:
        print("already exists")


def create_fixturePStatsJson():

        file_path = "%s/Pstatistics/%s/%s_Pstatistics.json" % (directory,nowDate, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_fixturePStatsFolder()
create_fixturePStatsDayFolder()
create_fixturePStatsJson()