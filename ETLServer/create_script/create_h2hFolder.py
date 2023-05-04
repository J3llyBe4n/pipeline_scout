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

# fixtures/H2h
def create_h2hFolder():
    if not os.path.exists("%s/H2h" %directory):
        os.mkdir("%s/H2h" %directory)
        print("folder created")
    else:
        print("already exists!")

# fixtures/H2h/YYYY
def create_h2hSeasonFolder():
    if not os.path.exists("%s/h2h/%s" %(directory, now_Year)):
        os.mkdir("%s/h2h/%s" %(directory, now_Year))
        print("folder created! : %s" %now_Year)
    else:
        print("already exists")

# fixtures/H2h/YYYY/ymd_h2h.json
def create_h2hJson():
    file_path = "%s/h2h/%s/%s_h2h.json" % (directory, now_Year, now_Date)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
        
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            print('json file created!')


create_h2hFolder()
create_h2hSeasonFolder()
create_h2hJson()



