
def convertToJson(resTime, crudOpt, url, date, time, http_Status):

    tmpDict = {}
    tmpDict['responseTime'] = resTime
    tmpDict['crudOption'] = crudOpt
    tmpDict['url'] = url
    tmpDict['Date'] = date
    tmpDict['Time'] = time
    tmpDict['httpStatus'] = http_Status

    return tmpDict