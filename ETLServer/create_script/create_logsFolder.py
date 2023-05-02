import os
import datetime
import json

nowDate = datetime.datetime.utcnow().date().strftime("%Y_%m_%d")
print(nowDate)
directory = os.path.join(os.path.dirname(__file__), '..', 'datas', 'Logs')

def createFolder():
    os.mkdir("%s/%s" %(directory, nowDate))
    print("folder created")

def createJsonFile():
    data = {'data' : []}
    with open("%s/%s/%s.json" %(directory, nowDate, nowDate), "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("file created")

def createBlobFile():
    data = {'data' : []}
    with open("%s/%s/%s_blob_logs.json" %(directory, nowDate, nowDate), "w") as json_files:
        json.dump(data, json_file, indent=4)

createFolder()
createJsonFile()
createBlobFile()