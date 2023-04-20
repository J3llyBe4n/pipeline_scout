import json
import os
import datetime

def loadMonitoringJson(tmpList):

	nowDate = datetime.datetime.now().date().strftime("%Y_%m_%d")

	directory = os.path.join(os.path.dirname(__file__),"..",'datas','Logs')


	with open("%s/%s/%s.json" %(directory, nowDate, nowDate), "a+") as json_file:
		json.dump(tmpList,json_file, indent=4)

