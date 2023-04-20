from httpRes_func import *

li1 = [ "https://v3.football.api-sports.io/leagues?id=139",
		"https://v3.football.api-sports.io/leagues?id=140",
		"https://v3.football.api-sports.io/leagues?id=141",
		"https://v3.football.api-sports.io/leagues?id=142",
		"https://v3.football.api-sports.io/leagues?id=143" ]

json_list = []
for i in li1:
    json_dict = {}
    responseTime = resTime(startTime)
    json_dict['responseTime'] = responseTime
    endPointUrl = getUrl()
    json_dict['endPointUrl'] = endPointUrl
    crudOption = getCrudOpt()
    json_dict['crudOption'] = crudOption
    nowDate = getTimeStamp()[0]
    json_dict['nowDate'] = nowDate
    nowTime = getTimeStamp()[1]
    json_dict['nowTime'] = nowTime
    http_Status = httpStatus()
    json_dict['httpStatus'] = http_Status
    json_list.append(json_dict)
    print(json_dict)

print(json_list)
