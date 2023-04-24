import requests, time
from ETLServer.Modules.load_toLocalJson import * 

class ApiStandings:

	def load_standingJson(self, idList, api_keys):
		print("run func load_standingJson")

		for i in idList:

			season = 2022
			leagueId = i
			print("call api req -> params : %d" %leagueId)

			base_Url = "https://v3.football.api-sports.io/standings?league=%d&season=%d" %(leagueId, season)

			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }
			
			#start_time = time.time()
			resp = requests.request("GET",base_Url, headers=headers)
			data_raw = resp.json()['response']

			#data_json = data_raw.json
			

			load_standingJson(data_raw, leagueId)

			


