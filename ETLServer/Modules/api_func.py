import requests, time
from ETLServer.Modules import httpRes_func as hf
from ETLServer.Modules import convertJson as js
from ETLServer.Modules import yoda_loadJson_block as load

class API_block:

	def load_pipe_league_API(self, idList, api_keys):
		print("load start")

		dataList = []
		
		for i in idList:
			leagueID = i
			print(leagueID)
			season = 2022
			uri = "https://v3.football.api-sports.io/leagues?id=%s&season=%d" %(leagueID, season)

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
			dataDict = {"league_name" : league_name, "api_league_id" : api_league_id, "league_nation" : league_nation}
			dictList.append(dataDict)

		return dictList 