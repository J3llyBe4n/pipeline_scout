import os
import datetime
import json

now_Date = datetime.datetime.utcnow().date().strftime("%Y_%m_%d")
print(now_Date)
directory = os.path.join(os.path.dirname(__file__), '..', 'datas', 'Logs')

def createFolder():
    os.mkdir("%s/%s" %(directory, now_Date))
    print("folder created")

def createJsonFile():
    data = {'data' : []}
    with open("%s/%s/%s.json" %(directory, now_Date, now_Date), "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("file created")

def createBlobFile():
    data = {'data' : []}
    with open("%s/%s/%s_blob_logs.json" %(directory, now_Date, now_Date), "w") as json_file:
        json.dump(data, json_file, indent=4)

createFolder()
createJsonFile()
# createBlobFile()