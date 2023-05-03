# 배치 주기는 매일
# 배치는 매일 경기 끝나느 저녁에 돌아야함
#

import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/standings')
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) #
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")

# standings/YYYY
def create_standingSeasonFolder():
    if not os.path.exists("%s/%s" %(directory, now_Year)):
        os.mkdir("%s/%s" %(directory, now_Year))
        print("folder created")
    else:
        print("already exists!")

# standings/YYYY/ymd_standing.json
def create_standingJson():
    file_path = "%s/%s/%s_standing.json" % (directory, now_Year, now_Date)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
    
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)



create_standingSeasonFolder()
create_standingJson()