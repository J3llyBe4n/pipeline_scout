'''
[Code Explanation]
- 리그의 standing 정보를 json 파일에 적재하는 모듈
- 런던의 utc 협정 시간대 적용
- 파일 저장 형태 :'[날짜]_[리그]id_standing.json'

[Need to Know]
- 24번째 줄의 try/except 구문은 테스트용 파일 생성자이므로 추후 삭제 필요
'''

import json
import os
from datetime import datetime


def load_standingJson(tmp_data, league_id):
    now_date = datetime.utcnow().date().strftime("%Y_%m_%d")
    
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'standings')
    #print(directory)

    # test 하려고 이 부분을 추가(현재 폴더 싸개가 없으므로..?)
    try :
        with open("%s/%s_%d_standing.json" % (directory, now_date, league_id), "r") as json_file:
            data = json.load(json_file)
    except:
        with open("%s/%s_%d_standing.json" % (directory, now_date, league_id), "w") as json_file:
            data = {'data' : []}
            json.dump(data, json_file, indent=4)

    # with open("%s/%s_%d_standing.json" % (directory, now_date, league_id), "r") as json_file:
    #     data = json.load(json_file)
     
    data['data'].append(tmp_data)

    print(tmp_data)

    with open("%s/%s_%d_standing.json" % (directory, now_date, league_id), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("sucksex")

def load_fixtureJson(tmp_data, league_id):
    now_date = datetime.utcnow().date().strftime("%y%m%d")
    
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'fixtures')
    #print(directory)

    with open("%s/%s_%d_fixture.json" % (directory, now_date, league_id), "r") as json_file:
        data = json.load(json_file)
     
    data['data'].append(tmp_data)

    print(tmp_data)

    with open("%s/%s_%d_fixture.json" % (directory, now_date, league_id), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("sucksex")

def load_TstatsJsonData(tmp_data, league_id):
    now_date = datetime.utcnow().date().strftime("%Y_%m_%d")
    
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'teams', 'statistics')
    with open("%s/%s_%d_Tstats.json" % (directory, now_date, league_id), "r") as json_file:
        data = json.load(json_file)
     
    data['data'].append(tmp_data)

    # print(tmp_data)

    with open("%s/%s_%d_Tstats.json" % (directory, now_date, league_id), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print(league_id)
        print("sucksex")

def load_TinfosJson(tmp_data, league_id):
    now_date = datetime.utcnow().date().strftime("%y%m%d")
    
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'teams', 'teams_info')
    #print(directory)

    try :
        with open("%s/%s_%d_Tinfo.json" % (directory, now_date, league_id), "r") as json_file:
            data = json.load(json_file)
    except:
        with open("%s/%s_%d_Tinfo.json" % (directory, now_date, league_id), "w") as json_file:
            data = {'data' : []}
            json.dump(data, json_file, indent=4)

    data['data'].append(tmp_data)

    print(tmp_data)

    with open("%s/%s_%d_Tinfo.json" % (directory, now_date, league_id), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("sucksex")

def load_h2hJson(tmp_data):
    
    date_time = tmp_data[0]['fixture']['date'][:tmp_data[0]['fixture']['date'].index('T')].replace('-','')[2:]
    print(date_time)
    league_id = tmp_data[0]['league']['id']
    print(league_id)
    
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'h2h')

    with open("%s/%s/%s_%s_h2h.json" %(directory,date_time, date_time, league_id), "r") as json_file:
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s/%s_%s_h2h.json" %(directory,date_time, date_time, league_id), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("heheh")
    
def load_eventsJson(tmp_data):
    
    now_date = datetime.now().date().strftime("%y%m%d")
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas/DataLake/fixtures/events')

    with open("%s/%s/%s_events.json" %(directory, now_date, now_date), "r") as json_file:
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s/%s_events.json" %(directory, now_date, now_date), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("heheh")

def load_fixtureStatsJsonData(tmp_data):
    now_date = datetime.utcnow().date().strftime("%Y_%m_%d")

    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'statistics')
    with open("%s/%s/%s_statistics.json" % (directory, now_date, now_date), "r") as json_file:
        data = json.load(json_file)
     
    data['data'].append(tmp_data)

    # print(tmp_data)

    with open("%s/%s/%s_statistics.json" % (directory, now_date, now_date), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print(league_id)
        print("sucksex")