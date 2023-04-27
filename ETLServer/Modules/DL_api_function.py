'''
[Code Explanation]
- API request의 요청 정보를 1차 가공하여 log 폴더에 json 파일로 저장
- 5개의 변수 중 2개가 리스트의 형태로 반환 > 7개 항목의 데이터 반환

[Need to Know]
- Visual Code가 현재 디렉토리 이외를 인식하지 못해 임의로 sys 모듈을 사용
- 현재까지 기록된 log 정보의 항목이 6개이므로 23-04-24의 일부 항목 수가 다름
'''

import requests, time
import sys
sys.path.append('../')

# import Modules.load_toLocalJson as loadL
# import Modules.convert_toJson as conv		# js > conv
# import Modules.load_json as load
# import Modules.http_response as http 		# hf > http


from ETLServer.Modules import load_toLocalJson as loadL
from ETLServer.Modules.load_toLocalJson import *
from ETLServer.Modules import convert_toJson as conv		# js > conv
from ETLServer.Modules import load_json as load
from ETLServer.Modules import http_response as http 		# hf > http

class ApiStandings:

	def load_standingJson(self, idList, api_keys):
		print("run func load_standingJson")

		for i in idList:

			season = 2022
			league_id = i
			print("call api req -> params : %d" %league_id)

			uri = "https://v3.football.api-sports.io/standings?league=%d&season=%d" %(league_id, season)
			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}
			
			start_time = time.time()
			response = requests.request("GET",uri, headers=headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response'][0]
			status = response.headers

			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			load.load_json(tmp_dict)

			loadL.load_standingJson(data, league_id)

class ApiFixtures:

	def load_fixtureJson(self, idList, api_keys):

		print("run func load_fixtureJson")
		season = 2022
		
		for i in idList:
			league_id = i
			print("call api req -> params : %d" %league_id)

			uri = "https://v3.football.api-sports.io/fixtures?league=%d&season=%d" %(league_id, season)

			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
			}

			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response'][0]
			status = response.headers

			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			load.load_json(tmp_dict)

			loadL.load_fixtureJson(data, league_id)

class ApiTeamStatistics:

	def Api_TstatsJson(self, idList, api_keys, round_date):
		print("run func load_TeamStatisticsJson")
		print(round_date)

		cnt = 1
		for i in range(len(idList)):
			
			if cnt % 250 == 0:
				time.sleep(60)
				print('wait for 60s')
			else:
				pass

			season = 2022
			leagueId = idList[i][0]
			teamId = idList[i][1]
			print("call api req -> params : %d" % leagueId)

			uri = "https://v3.football.api-sports.io/teams/statistics?league=%d&season=%d&team=%d&date=%s" %(leagueId, season, teamId, round_date)
			headers = {
						'x-rapidapi-host': "v3.football.api-sports.io",
						'x-rapidapi-key': api_keys
						}
			# print(uri)
			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response']

			status = response.headers

			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			load.load_json(tmp_dict)
			
			load_TstatsJsonData(data, leagueId)
			cnt += 1

class ApiTeams:

	# league_id 리스트로 받아오기기
	def load_teamJson(self, idList, api_keys):

		print("run func load_fixtureJson")
		# season = 2022
		
		for i in idList:
			league_id = i
			print("call api req -> params : %d" %league_id)

			uri = "https://v3.football.api-sports.io/teams?league=%d" %(league_id)

			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
			}

			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response'][0]
			status = response.headers

			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			load.load_json(tmp_dict)

			loadL.load_teamJson(data, league_id)

class ApiH2h:

	def load_h2hJson(self,data_list, api_keys):
		print("run func load_h2hJson")

		for i in range(len(data_list)):
			home = data_list[i]['home_id']
			away =data_list[i]['away_id']
			date_day = data_list[i]['date']
			print(date_day)

			params = "%d-%d" %(home, away) 
			print("call api req -> params : %s" %params)

			uri = "https://v3.football.api-sports.io/fixtures/headtohead?h2h=%s&date=%s&timezone=%s" %(params, date_day, 'europe/london')
			
			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys

			}

			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response'][0]
			status = response.headers



			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			#load.load_json(tmp_dict)

			loadL.load_h2hJson(data)

class ApiEvents:
	def load_eventsJson(self,data_list, api_keys):
		print("run func eventsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			print("call api req -> params : %s" %fixture_id)

			uri = 'https://v3.football.api-sports.io/fixtures/events?fixture=%d' %fixture_id

			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys

			}

			start_time = time.time()
			response = requests.request("GET", uri, headers= headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response'][0]
			status = response.headers



			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)

			load.load_json(tmp_dict)

			final_dict = loadL.convert_eventsJson(data,fixture_id)
			loadL.load_eventsJson(final_dict)

class ApiFixtureTStats:

	def load_fixtureTStatsJson(self, data_list, api_keys):
		print("run func load_fixtureTStatsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			print(fixture_id)

			uri = "https://v3.football.api-sports.io/fixtures/statistics?fixture=%d" %fixture_id
			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys

			}

			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response']
			status = response.headers



			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			#load.load_json(tmp_dict)

			final_dict = conv.convert_lineUpsJson(data, fixture_id)
			loadL.load_lineUpsJson(final_dict)

class ApiFixturePStats:

	def load_fixturePStatsJson(self, data_list, api_keys):
		print("run func load_fixturePStatsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			print(fixture_id)

			uri = "https://v3.football.api-sports.io/fixtures/players?fixture=%d" %fixture_id
			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys

			}

			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response']
			status = response.headers



			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			#load.load_json(tmp_dict)

			final_dict = conv.convert_lineUpsJson(data, fixture_id)
			loadL.load_lineUpsJson(final_dict)

class ApiFixtureLineups:

	def load_lineUpsJson(self, data_list, api_keys):
		print("run func lineupsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			print("call api req -> params : %s" %fixture_id)

			uri = 'https://v3.football.api-sports.io/fixtures/lineups?fixture=%d' %fixture_id

			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys

			}

			start_time = time.time()
			response = requests.request("GET", uri, headers= headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response']
			status = response.headers



			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)

			load.load_json(tmp_dict)
			final_dict = conv.convert_lineUpsJson(data, fixture_id)
			loadL.load_lineUpsJson(final_dict)


class ApiLeagues:

	# league_id 리스트로 받아오기기
	def load_leagueJson(self, data_list, api_keys):

		print("run func load_fixtureJson")
		season = 2022
		
		print("call api req -> params : %d" %season)
		for i in data_list:
			league_id = i
			uri = "https://v3.football.api-sports.io/leagues?season=%d&id=%d" %(season, league_id)

			headers = {
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}

			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response'][0]
			status = response.headers

			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			load.load_json(tmp_dict)

			loadL.load_leagueJson(data, i)

def load_psquadJson(self, data_list, api_keys):
		print("run func load_fixtureJson")
		season = 2022
		
		# print("call api req -> params : %d" %team_id)
		for i in data_list:
			team_id = i
			uri = "https://v3.football.api-sports.io/players/squads?team=%d" %(team_id)

			headers = {
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}

			start_time = time.time()
			response = requests.request("GET", uri, headers = headers)
			response_time = http.get_responseTime(start_time)
			data = response.json()['response']
			status = response.headers

			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			load.load_json(tmp_dict)

			loadL.load_psquadJson(data, i) 