import json
import os
import datetime

tmpList = [1.3, "get", "22_03_30", "13:30:30", "200"]

tmpDic = {"resTime" : tmpList[0], "method": tmpList[1], "date":tmpList[2], "time": tmpList[3], "stat": tmpList[4]}

nowDate = datetime.datetime.now().date().strftime("%Y_%m_%d")

directory = os.path.join(os.path.dirname(__file__),"..",'datas','Logs')

def loadMonitoringJson(tmpList):
	with open("%s/%s/%s.json" %(directory, nowDate, nowDate), "a+") as json_file:
		data = tmpDic
		json.dump(data,json_file, indent=4)

