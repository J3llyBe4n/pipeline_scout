import requests as re
import time
from datetime import datetime

# uri = 'https://v3.football.api-sports.io/teams?id=42&league=39&season=2022'

getBaseInfoUrl = "https://v3.football.api-sports.io/leagues?id=139"
headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': 'a86d420d0d8840c8e722e16cf9742f7b'
        }

def resTime(res):
        # responseTime = round((time.time() - startTime),4)

        responseTime = (time.time() - res)
        #응답시간 변수 이름 responeTime
        return responseTime

def getUrl():
        endPointUrl = getBaseInfoUrl[:getBaseInfoUrl.index('?')]
        return endPointUrl

def getCrudOpt():
        crudOption = status['Access-Control-Allow-Methods']
        crudOption = crudOption[:crudOption.index(',')]
        return crudOption


def getTimeStamp():
        dateString = status['date']
        dateObj = datetime.strptime(dateString, "%a, %d %b %Y %H:%M:%S %Z")
        year = dateObj.year
        month = dateObj.month
        day = dateObj.day
        # gmt gg 
        hour = dateObj.hour
        minute = dateObj.minute
        second = dateObj.second

        nowDate = str(year) + "_" + str(month) + "_" + str(day)
        nowTime = str(hour) + "_" + str(minute) + "_" + str(second)

        return nowDate, nowTime

def httpStatus():
        httpStatus = baseStatus.status_code
        return httpStatus



startTime = time.time()
baseStatus = re.get(url = getBaseInfoUrl, headers = headers)
resTime(startTime)

status = baseStatus.headers

getUrl()
getCrudOpt()
getTimeStamp()
httpStatus()
