'''
[Code Explanation]
- 1차 가공된 API request 요청 정보를 딕셔너리의 형태로 병합

[Need to Know]
- 
'''

# convertToJson > convert_toJson
# resTime, crudOpt, http_Status > response_time, crud_option, http_status
def convert_toJson(response_time, crud_option, uri_info, time_stamp, http_status):

    tmp_dict = {}
    tmp_dict['response_time'] = response_time
    tmp_dict['crud_option'] = crud_option
    tmp_dict['url'] = uri_info[0]
    tmp_dict['parameter'] = uri_info[1]
    tmp_dict['date'] = time_stamp[0]
    tmp_dict['time'] = time_stamp[1]
    tmp_dict['http_status'] = http_status

    return tmp_dict

def convert_lineUpsJson(tmp_data, fixture_id):
    fixture_id = fixture_id
    home_teamData = tmp_data[0]
    away_teamData = tmp_data[1]

    tmp_dict ={'fixture': fixture_id, 'home' : home_teamData, 'away': away_teamData}

    return tmp_dict

def convert_eventsJson(tmp_data, fixture_id):
    fixture_id = fixture_id
    tmp_dict = {'fixture': fixture_id, 'events' : tmp_data}

    return tmp_dict

def convert_coachsJson(tmp_data):
    tmp_dict ={}
    for i in range(len(tmp_data)):
        for original_key, value in tmp_data.items():
            new_key = original_key.replace('id','coach_id')
            tmp_dict[new_key] = value
    return tmp_dict

def convert_playerJson(team_id, tmp_data):
    tmp_dict = {}
    tmp_playerData =[]
    for i in range(len(tmp_data)):
        for j in range(len(tmp_data[i])):
            tmp_playerData.append(tmp_data[i][j])

    tmp_dict ={'id': team_id, 'data' : tmp_playerData}

    return tmp_dict


def convert_predictionsJson(tmp_data, fixture_id):
    print(tmp_data)
    fixture_id = fixture_id
    tmp_dict = {'fixture':fixture_id, 'predictions':tmp_data['predictions'], 'league':tmp_data['league'], 'teams':tmp_data['teams'], 'comparison':tmp_data['comparison'],'h2h':tmp_data['h2h']}

    return tmp_dict