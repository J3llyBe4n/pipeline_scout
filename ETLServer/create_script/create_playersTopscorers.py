#
#
#

import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/players')
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) #
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")

# players/Topscorers
def create_pTopscorersFolder():
    if not os.path.exists("%s/Topscorers" % directory):
        os.mkdir("%s/Topscorers" % directory)
        print("folder created")
    else:
        print("already exists!")

# players/Topscorers/YYYY
def create_pTopscorersSeasonFolder():
    if not os.path.exists("%s/Topscorers/%s" %(directory, now_Year)):
        os.mkdir("%s/Topscorers/%s" %(directory, now_Year))
        print("folder created : %s" %now_Year)
    else:
        print("already exists")

# players/Topscorers/YYYY/ymd_Ptopscorers.json
def create_pTopscorersJson():
    file_path = "%s/Topscorers/%s/%s_Ptopscorers.json" % (directory, now_Year, now_Date)
    data = {'data' : []}
        
    if os.path.exists(file_path):
        print("file exists")
        
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


create_pTopscorersFolder()
create_pTopscorersSeasonFolder()
create_pTopscorersJson()