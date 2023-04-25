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
    print(directory)

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
    