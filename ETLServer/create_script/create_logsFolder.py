import os
import datetime
import json

now_Date = datetime.datetime.utcnow().date().strftime("%Y_%m_%d")
print(now_Date)
directory = os.path.join(os.path.dirname(__file__), '..', 'datas')

def createLogsFolder():
    if not os.path.exists("%s/Logs" %directory):
        os.mkdir("%s/Logs" %directory)
        print("folder created")
    else:
        print("already exists!")

def createLogsDateFolder():
    if not os.path.exists("%s/Logs/%s" %(directory,now_Date)):
        os.mkdir("%s/Logs/%s" %(directory,now_Date))
        print("folder created")
    else:
        print("already exists!")

def createJsonFile():
    file_path = "%s/Logs/%s/%s.json" % (directory, now_Date, now_Date)
    data = {'data' : []}

    if os.path.exists(file_path):
        print("file exists")

    else:    
        with open("%s/Logs/%s/%s.json" %(directory, now_Date, now_Date), "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("file created")

def createBlobFile():
    file_path = "%s/Logs/%s/%s.json" % (directory, now_Date, now_Date)
    data = {'data' : []}

    if os.path.exists(file_path):
        print("file exists")

    else:
        with open("%s/Logs/%s/%s_blob_logs.json" %(directory, now_Date, now_Date), "w") as json_file:
            json.dump(data, json_file, indent=4)

createLogsFolder()
createLogsDateFolder()
createJsonFile()
# createBlobFile()