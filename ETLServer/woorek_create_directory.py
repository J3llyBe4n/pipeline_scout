from datetime import datetime, timedelta
import os
import json

tmpGmtPresentTime = (datetime.now() - timedelta(hours=9)).strftime("%Y-%m-%d")
gmtPresentTime = tmpGmtPresentTime.replace('-','_')
newDirectoryPath = './%s' %gmtPresentTime
if not os.path.exists(newDirectoryPath):
    os.makedirs(newDirectoryPath)

dirPath = '%s' %gmtPresentTime

data = {}

filePath = os.path.join(dirPath, 'tmpfile.json')
with open(filePath, 'w') as f:
    json.dump(data,f)

f.close()



