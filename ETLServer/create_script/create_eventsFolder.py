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

# fixture/events
def create_eventsFolder():
    if not os.path.exists("%s/events" %directory):
        os.mkdir("%s/events" %directory)
        print("folder created")
    else:
        print("already exists!")

# fixture/events/YYYY
def create_eventsSeasonFolder():
    if not os.path.exists("%s/events/%s" %(directory, now_Year)):
        os.mkdir("%s/events/%s" %(directory, now_Year))
        print("folder created! : %s" %now_Year)
    else:
        print("already exists")

# fixture/events/YYYY/ymd_events.json
def create_eventsJson():
    file_path = "%s/events/%s/%s_events.json" % (directory, now_Year, now_Date)
    data = {'data' : []}
    
    if os.path.exists(file_path):
        print("file exists")
    
    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            print('json file created!')


create_eventsFolder()
create_eventsSeasonFolder()
create_eventsJson()