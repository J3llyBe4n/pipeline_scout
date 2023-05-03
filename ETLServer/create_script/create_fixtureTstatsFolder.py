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

# fixtures/Tstatistics
def create_fixturesTstatsFolder():
    if not os.path.exists("%s/Tstatistics" %directory):
        os.mkdir("%s/Tstatistics" %directory)
        print("folder created")
    else:
        print("already exists!")

# fixtures/Tstatistics/YYYY
def create_fixturesSeasonTstatsFolder():
    if not os.path.exists("%s/Tstatistics/%s" %(directory, now_Year)):
        os.mkdir("%s/Tstatistics/%s" %(directory, now_Year))
        print("folder created! : %s" %now_Year)
    else:
        print("already exists")

# fixtures/Tstatistics/YYYY/ymd_Tstatistics.json
def create_fixturesTstatsJson():
    file_path = "%s/Tstatistics/%s/%s_Tstatistics.json" % (directory, now_Year, now_Date)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
    
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


create_fixturesTstatsFolder()
create_fixturesSeasonTstatsFolder()
create_fixturesTstatsJson()