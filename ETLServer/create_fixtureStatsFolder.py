import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake', 'fixtures')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")


def create_fixtureStatsFolder():
    if not os.path.exists("%s/statistics" %directory):
        os.mkdir("%s/statistics" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_fixtureStatsDayFolder():
    if not os.path.exists("%s/statistics/%s" %(directory, nowDate)):
        os.mkdir("%s/statistics/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
    else:
        print("already exists")


def create_fixtureStatsJson():

        file_path = "%s/statistics/%s/%s_statistics.json" % (directory,nowDate, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_fixtureStatsFolder()
create_fixtureStatsDayFolder()
create_fixtureStatsJson()