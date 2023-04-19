import requests

class API_block:

	def load_pipe_league_API(self, idList, api_keys):
		print("load start")
		cnt = 0
		dataList = []
		
		for i in idList:
			leagueID = i
			print(leagueID)
			season = 2022
			uri = "https://v3.football.api-sports.io/leagues?id=%s&season=%d" %(leagueID, season)
			print(uri)
			headers = {
				'x-rapidapi-host': "v3.football.api-sports.io",
	        	'x-rapidapi-key': api_keys
	        }

			data = requests.request("GET", uri, headers=headers).json()['response']
			data_1 = data[0]
			cnt += 1
			dataList.append(data_1)
			print(dataList)
			print(cnt)
		return cnt, dataList


	def tmp_pipe_league_API(self, dataList):
		dictList = []

		for i in dataList:
			league_name = i['league']['name']
			api_league_id = i['league']['id']
			league_nation = i['country']['name']
			dataDict = {"league_name" : league_name, "api_league_id" : api_league_id, "league_nation" : league_nation}
			dictList.append(dataDict)

		return dictList