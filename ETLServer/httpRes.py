import requests as re
from datetime import datetime

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "a68636f8f2c18511179c56f15e95080c"
    }

getBaseInfoUrl = "https://v3.football.api-sports.io/leagues?id=139"

baseStatus = re.get(url = getBaseInfoUrl, headers = headers)
status = baseStatus.headers

httpCode = baseStatus
print(httpCode)
print(type(httpCode))


def getUrl():
    endPointUrl = getBaseInfoUrl[:getBaseInfoUrl.index('?')]
    print(endPointUrl)

def getCrudOpt():
    crudOption = status['Access-Control-Allow-Methods']
    crudOption = crudOption[:crudOption.index(',')]
    print(crudOption)


def getTimeStamp():
dateString = status['date']
dateObj = datetime.strptime(dateString, "%a, %d %b %Y %H:%M:%S %Z")
year = dateObj.year
month = dateObj.month
day = dateObj.day
# gmt gg 
hour = dateObj.hour + 9
minute = dateObj.minute
second = dateObj.second

print(year, month, day)
print(hour, minute, second)


