#이놈은 배치 주기가 하루 입니다.
#배치는 하루 데이터가 넣는 script 이전에 돌아야합니다.
#00:00~00:30 내에 돌아야 합니다.

import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), "../datas/DataLake/fixtures")
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) # 
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")

# fixtures/fixtures
def create_fixturesFolder():
    if not os.path.exists("%s/fixtures" %directory):
        os.mkdir("%s/fixtures" %directory)
        print("folder created!")
    else:
        print("already exists!")

# fixtures/fixtures/YYYY
def create_fixturesSeasonFolder():
    if not os.path.exists("%s/fixtures/%s" %(directory, now_Year)):
        os.mkdir("%s/fixtures/%s" %(directory, now_Year))
        print("folder created")
    else:
        print("already exists!")

# fixtures/fixtures/YYYY/ymd_fixture.json
def create_fixturesJson():
    file_path = "%s/fixtures/%s/%s_fixture.json" % (directory, now_Year, now_Date)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
    
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


create_fixturesFolder()
create_fixturesSeasonFolder()
create_fixturesJson()