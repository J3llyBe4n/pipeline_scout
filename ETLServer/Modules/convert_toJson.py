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