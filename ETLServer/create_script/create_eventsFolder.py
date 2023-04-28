import os
import datetime
import json

#이놈은 배치 주기가 하루 입니다.
#배치는 하루 데이터가 넣는 script 이전에 돌아야합니다.



directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')
nowYear = datetime.datetime.now().date().strftime("%Y")
nowDate = datetime.datetime.now().date().strftime("%y%m%d")
nowYear = int(nowYear) - 1


def create_eventsFolder():
    if not os.path.exists("%s/events" %directory):
        os.mkdir("%s/events" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_seasonEventsFolder():
    if not os.path.exists("%s/events/%s" %(directory, nowYear)):
        os.mkdir("%s/events/%s" %(directory, nowYear))
        print("folder created! : %s" %nowYear)
    else:
        print("already exists")


def create_eventsJson():

        file_path = "%s/events/%s/%s_events.json" % (directory,nowYear, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_eventsFolder()
create_seasonEventsFolder()
create_eventsJson()