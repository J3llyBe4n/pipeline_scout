import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), 'datas', 'DataLake', 'fixtures')
nowDate = datetime.datetime.now().date().strftime("%y%m%d")


def create_eventsFolder():
    if not os.path.exists("%s/events" %directory):
        os.mkdir("%s/events" %directory)
        print("folder created")
    else:
        print("already exists!")


def create_eventsDayFolder():
    if not os.path.exists("%s/events/%s" %(directory, nowDate)):
        os.mkdir("%s/events/%s" %(directory, nowDate))
        print("folder created! : %s" %nowDate)
    else:
        print("already exists")


def create_eventsJson():

        file_path = "%s/events/%s/%s_events.json" % (directory,nowDate, nowDate)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)


create_eventsFolder()
create_eventsDayFolder()
create_eventsJson()