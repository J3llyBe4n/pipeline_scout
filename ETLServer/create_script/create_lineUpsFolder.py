#이놈은 배치 주기가 하루 입니다.
#배치는 하루 데이터가 넣는 script 이전에 돌아야합니다.
#00:00~00:30 내에 돌아야 합니다.

import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) #
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")

# fixtures/lineups
def create_lineUpsFolder():
    if not os.path.exists("%s/lineups" %directory):
        os.mkdir("%s/lineups" %directory)
        print("folder created")
    else:
        print("already exists!")

# fixtures/lineups/YYYY
def create_lineUpsSeasonFolder():
    if not os.path.exists("%s/lineups/%s" %(directory, now_Year)):
        os.mkdir("%s/lineups/%s" %(directory, now_Year))
        print("folder created! : %s" %now_Year)
    else:
        print("already exists")

# fixtures/lineups/YYYY/ymd_lineUps.json
def create_lineUpsJson():
    file_path = "%s/lineups/%s/%s_lineUps.json" % (directory, now_Year, now_Date)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
    
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


create_lineUpsFolder()
create_lineUpsSeasonFolder()
create_lineUpsJson()