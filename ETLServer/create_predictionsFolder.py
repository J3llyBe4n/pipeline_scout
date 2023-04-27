import os
import datetime
import json
from ETLServer.Modules.db_function import *

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
nowDate = datetime.datetime.utcnow().date().strftime("%y%m%d")

def create_predictionsFolder():
    if not os.path.exists("%s/predictions" %directory):
        os.mkdir("%s/predictions" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_predictionsDayFolder():
    if not os.path.exists("%s/predictions/%s" %(directory, nowDate)):
        os.mkdir("%s/predictions/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
    else:
        print("already exists")

def create_predictionsJson():
    file_path = "%s/predictions/%s/%s_predictions.json" % (directory,nowDate, nowDate)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
    
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

create_predictionsFolder()
create_predictionsDayFolder()
create_predictionsJson()
