from datetime import datetime, timedelta
import os
import json

def getGmtTime(self):
    tmpGmtPresentTime = (datetime.now() - timedelta(hours=9)).strftime("%Y-%m-%d")
    gmtPresentTime = tmpGmtPresentTime.replace('-', '_')
    return gmtPresentTime

def makeDirectory(self,input_time):
    self.newDirectoryPath = './%s' % input_time
    os.makedirs(self.newDirectoryPath)

def createJson(self,dir_path):
    dir_path = self.newDirectoryPath
    data = {}
    filePath = os.path.join(dir_path, 'tmpfile.json')
    with open(filePath, 'w') as f:
        json.dump(data,f)
    f.close()



