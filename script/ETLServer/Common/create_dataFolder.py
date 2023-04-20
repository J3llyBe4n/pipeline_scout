import os
import datetime
import json

nowDate = datetime.datetime.now().date().strftime("%Y_%m_%d")

def createFolder():
    os.mkdir(nowDate)
    print("folder created")


def createJsonFile():
    data ={}
    with open("%s/%s.json" %(nowDate, nowDate), "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("file created")

createFolder()
createJsonFile()
