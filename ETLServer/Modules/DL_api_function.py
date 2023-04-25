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

import Modules.load_toLocalJson as loadL
import Modules.convert_toJson as conv		# js > conv
import Modules.load_json as load
import Modules.http_response as http 		# hf > http


#from ETLServer.Modules import load_toLocalJson as loadL
#from ETLServer.Modules.load_toLocalJson import * 
#from ETLServer.Modules import convert_toJson as conv		# js > conv
#from ETLServer.Modules import load_json as load
#from ETLServer.Modules import http_response as http 		# hf > http

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
			data = response.json()['response']
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
			data = response.json()['response']
			status = response.headers

			uri_info = http.get_uriInfos(uri)
			time_stamp = http.get_timeStamp(status)
			crud_option = http.get_crudOption(status)
			http_status = http.get_httpStatus(response)

			tmp_dict = conv.convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status)
			load.load_json(tmp_dict)

			loadL.load_fixtureJson(data, league_id)
