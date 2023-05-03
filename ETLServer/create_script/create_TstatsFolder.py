# 배치 주기 매일
# 배치 경기 다 끝나고 돌아야함
#

import os
import datetime
import json

directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/teams')
now_Year = datetime.datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) #
now_Date = datetime.datetime.utcnow().date().strftime("%y%m%d")
# yesterday = (datetime.datetime.utcnow().date() - datetime.timedelta(days=1)).strftime("%y%m%d")

# teams/Statistics
def create_teamsStatisticsFolder():
    if not os.path.exists("%s/Statistics" % directory):
        os.mkdir("%s/Statistics" % directory)
        print("folder created")
    else:
        print("already exists!")

# teams/Statistics/YYYY
def create_teamsStatisticsSeasonFolder():
    if not os.path.exists("%s/Statistics/%s" %(directory, now_Year)):
        os.mkdir("%s/Statistics/%s" %(directory, now_Year))
        print("folder created")
    else:
        print("already exists")


def create_teamsStatisticsJson():
    file_path = "%s/Statistics/%s/%s_Tstats.json" % (directory, now_Year, now_Date)
    data = {'data' : []}

    if os.path.exists(file_path):
        print("file exists")

    else:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)



create_teamsStatisticsFolder()
create_teamsStatisticsSeasonFolder()
create_teamsStatisticsJson()