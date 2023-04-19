import requests

api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

def load_pipe_league_API(idList, api_keys):
    cnt = 0
    dataList = []
    
    for i in idList:
        leagueID = i
        season = 2022
        uri = "https://v3.football.api-sports.io/leagues?id=%s&season=%d" %(leagueID, season)
        headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': api_keys
        }
        data = requests.request("GET", uri, headers = headers).json()['response'][0]
        cnt += 1
        dataList.append(data)

    return cnt, dataList


def tmp_pipe_league_API(dataList):
    dictList = []

    for i in dataList:
        league_name = i['league']['name']
        api_league_id = i['league']['id']
        league_nation = i['country']['name']
        dataDict = {"league_name" : league_name, "api_league_id" : api_league_id, "league_nation" : league_nation}
        dictList.append(dataDict)

    return dictList
        

