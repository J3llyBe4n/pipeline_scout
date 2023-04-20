from httpRes_func import *
def convertToJson(respStatusList):
    tmptmpDict = {}
    tmptmpDict['responseTime'] = respStatusList[0]
    tmptmpDict['crudOption'] = respStatusList[1]
    tmptmpDict['Date'] = respStatusList[2]
    tmptmpDict['Time'] = respStatusList[3]
    tmptmpDict['httpStatus'] = respStatusList[4]
    # tmptmpList = [tmptmpDict['responseTime'], tmptmpDict['crudOption'], tmptmpDict['Date'],tmptmpDict['Time'],tmptmpDict['httpStatus']]
    return tmptmpDict

li1 = ["https://v3.football.api-sports.io/leagues?id=139",
    "https://v3.football.api-sports.io/leagues?id=140",
    "https://v3.football.api-sports.io/leagues?id=141",
    "https://v3.football.api-sports.io/leagues?id=142",
    "https://v3.football.api-sports.io/leagues?id=143" ]

for i in range(len(li1)):
    startTime = time.time()
    baseStatus = re.get(url = li1[i], headers = headers)
    resTime(startTime)

    status = baseStatus.headers

    tmpUrl = getUrl()
    tmpCrudOpt = getCrudOpt()
    tmpgetDate = getTimeStamp()[0]
    tmpgetTime = getTimeStamp()[1]
    tmphttpStatus = httpStatus()


    tmpList = [tmpUrl, tmpCrudOpt, tmpgetDate, tmpgetTime, tmphttpStatus]
    tmptmptmpList = convertToJson(tmpList)

    '''제이슨으로 파일디렉토리 내리기'''

    print(tmptmptmpList)
