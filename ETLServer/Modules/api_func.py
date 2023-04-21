import requests, time
from ETLServer.Modules import httpRes_func as hf
from ETLServer.Modules import convertJson as js
from ETLServer.Modules import yoda_loadJson_block as load


class API_block:

    def load_pipe_league_API(self, idList, api_keys):
        print("load league ID start")

        dataList = []

        for i in idList:
            leagueID = i
            print(leagueID)
            season = 2022
            uri = "https://v3.football.api-sports.io/leagues?id=%s&season=%d" % (leagueID, season)

            headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }

            startTime = time.time()
            resp = requests.request("GET", uri, headers=headers)
            data = resp.json()['response']

            status = resp.headers

            finalTime = hf.resTime(startTime)
            finalUrl = hf.getUrl(uri)
            finalList = hf.getTimeStamp(status)
            finalCrudOpt = hf.getCrudOpt(status)
            finalstatus = hf.httpStatus(resp)
            print(finalstatus)
            finalDict = js.convertToJson(finalTime, finalCrudOpt, finalUrl, finalList[0], finalList[1], finalstatus)

            load.loadMonitoringJson(finalDict)

            data_1 = data[0]
            dataList.append(data_1)
            print(dataList)

        return dataList

    def tmp_pipe_league_API(self, dataList):
        dictList = []

        for i in dataList:
            league_name = i['league']['name']
            api_league_id = i['league']['id']
            league_nation = i['country']['name']
            dataDict = {"league_name": league_name, "api_league_id": api_league_id, "league_nation": league_nation}
            dictList.append(dataDict)

        return dictList


class ApiTeamBlock:

    def loadTeamData(self, idList, api_keys):
        print("load Team ID start")

        dataList = []

        for i in idList:
            leagueId = i
            season = 2022

            uri = "https://v3.football.api-sports.io/teams?league=%s&season=%d" % (leagueId, season)

            headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }

            startTime = time.time()
            resp = requests.request("GET", uri, headers=headers)
            data = resp.json()['response']

            for j in range(len(data)):
                tmpData = data[j]
                dataList.append(tmpData)

            print("load compelete league ID : %s" % leagueId)

            status = resp.headers

            finalTime = hf.resTime(startTime)
            finalUrl = hf.getUrl(uri)
            finalList = hf.getTimeStamp(status)
            finalCrudOpt = hf.getCrudOpt(status)
            finalstatus = hf.httpStatus(resp)
            # print(finalstatus)
            finalDict = js.convertToJson(finalTime, finalCrudOpt, finalUrl, finalList[0], finalList[1], finalstatus)

            load.loadMonitoringJson(finalDict)

        # print(dataList)

        return dataList

    def transformTeamData(self, dataList):
        dictList = []

        for i in dataList:
            teamName = i['team']['name']
            apiTeamId = i['team']['id']
            dataDict = {"teamName": teamName, "apiTeamId": apiTeamId}
            dictList.append(dataDict)

        return dictList


class ApiPlayerBlock:

    def loadPlayerData(self, idList, api_keys):
        print("load Player ID start")

        dataList = []

        for i in range(1, len(idList) + 1):

            if i % 200 == 0:
                time.sleep(60)
            else:

                teamId = idList[i]

                uri = "https://v3.football.api-sports.io/players/squads?team=%d" % teamId

                headers = {
                    'x-rapidapi-host': "v3.football.api-sports.io",
                    'x-rapidapi-key': api_keys
                }

                startTime = time.time()
                resp = requests.request("GET", uri, headers=headers)
                data = resp.json()['response']

                for j in range(len(data)):
                    tmpData = data[j]
                    dataList.append(tmpData)

                print("load compelete team ID : %s" % teamId)

                status = resp.headers

                finalTime = hf.resTime(startTime)
                finalUrl = hf.getUrl(uri)
                finalList = hf.getTimeStamp(status)
                finalCrudOpt = hf.getCrudOpt(status)
                finalstatus = hf.httpStatus(resp)
                # print(finalstatus)
                finalDict = js.convertToJson(finalTime, finalCrudOpt, finalUrl, finalList[0], finalList[1], finalstatus)

                load.loadMonitoringJson(finalDict)

                data_1 = data[0]
                dataList.append(data_1)
        # print(dataList)

        return dataList

    def transformPlayerData(self, dataList):
        dictList = []

        for i in dataList:
            tmpShell = i['players']
            for j in range(len(tmpShell)):
                print(tmpShell[j])
                playerName = tmpShell[j]['name']
                apiPlayerId = tmpShell[j]['id']
                dataDict = {"playerName": playerName, "apiPlayerId": apiPlayerId}
                dictList.append(dataDict)
        return dictList
