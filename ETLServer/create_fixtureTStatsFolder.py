import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake', 'fixtures')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")


def create_fixtureTStatsFolder():
    if not os.path.exists("%s/Tstatistics" %directory):
        os.mkdir("%s/Tstatistics" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_fixtureTStatsDayFolder():
    if not os.path.exists("%s/Tstatistics/%s" %(directory, nowDate)):
        os.mkdir("%s/Tstatistics/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
    else:
        print("already exists")


def create_fixtureTStatsJson():

        file_path = "%s/Tstatistics/%s/%s_Tstatistics.json" % (directory,nowDate, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_fixtureTStatsFolder()
create_fixtureTStatsDayFolder()
create_fixtureTStatsJson()