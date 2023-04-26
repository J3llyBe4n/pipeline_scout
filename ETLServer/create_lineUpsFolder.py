import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake', 'fixtures')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")


def create_lineUpsFolder():
    if not os.path.exists("%s/lineups" %directory):
        os.mkdir("%s/lineups" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_lineUpsDayFolder():
    if not os.path.exists("%s/lineups/%s" %(directory, nowDate)):
        os.mkdir("%s/lineups/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
    else:
        print("already exists")


def create_lineUpsJson():

        file_path = "%s/lineups/%s/%s_lineUps.json" % (directory,nowDate, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_lineUpsFolder()
create_lineUpsDayFolder()
create_lineUpsJson()