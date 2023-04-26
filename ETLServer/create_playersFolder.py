import os, json
from datetime import datetime

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake')
now_date = datetime.utcnow().date().strftime("%y%m%d")

seasons = 2022

def create_playersFolder():
    if not os.path.exists("%s/players" % directory):
        os.mkdir("%s/players" % directory)
        print("folder created")
    else:
        print("already exists!")

def create_psquadFolder():
    if not os.path.exists("%s/players/squad" % directory):
        os.mkdir("%s/players/squad" % directory)
        print("folder created")
    else:
        print("already exists!")        

def create_psquadJson(tmp_teamId):

    for i in tmp_teamId:
        team_id = i
        file_path = "%s/players/squad/%s_%s_Psquad.json" % (directory, now_date, team_id)
        data = {'data' : []}
            
        if os.path.exists(file_path):
            print("file exists")
            
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


if __name__ == "__main__":

    from Modules.db_function import *
    from Modules.DL_api_function import * 

    dbFunc = DBfunc()
    dbFunc.connect_SQL()
    tmp_teamId = dbFunc.read_teamId()

    create_playersFolder()
    create_psquadFolder()
    create_psquadJson(tmp_teamId)