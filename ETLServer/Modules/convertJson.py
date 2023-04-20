from httpRes_func import *

def convertToJson(resTime, crudOpt, date, time, http_Status):

    tmpDict = {}
    tmpDict['responseTime'] = resTime
    tmpDict['crudOption'] = crudOpt
    tmpDict['Date'] = date
    tmpDict['Time'] = time
  	tmpDict['httpStatus'] = http_Status

    return tmpDict