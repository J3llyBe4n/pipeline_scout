import os
from google.cloud import storage
import datetime
import json

nowDate = datetime.datetime.utcnow().date().strftime('%y%m%d')

json_path = 'C:/Users/user/PycharmProjects/soccer_pipe_line/pipeline_scout/ETLServer/humming-bird-383304-263eaa656cba.json'
# 환경변수 설정
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path
# GCS 클라이언트 초기화
client = storage.Client()

# IAMScouter 프로젝트에서 사용할 버킷 이름 입력
bucket_name = 'i_am_scouter'
bucket = client.get_bucket(bucket_name)

# 로컬 디렉토리 경로
local_directory = 'C:/Users/user/PycharmProjects/soccer_pipe_line/pipeline_scout/ETLServer/datas/'
log_local_directory = os.path.join(os.path.dirname(__file__), 'datas', 'Logs')

# 로컬 디렉토리의 모든 파일을 반복
for dirpath, dirs, files in os.walk(local_directory):
    for file_name in files:
        # 로컬 파일 경로
        local_file_path = os.path.join(dirpath, file_name)
        
        # GCS 객체 경로 생성
        gcs_object_name = local_file_path.replace(local_directory, '')
        gcs_object_name = gcs_object_name.replace(os.path.sep, '/')
        
        # Blob 객체 생성 및 업로드
        blob = bucket.blob(gcs_object_name)
        with open(local_file_path, 'rb') as file:
            load_blob = blob.upload_from_file(file)
            load_blob
            print(f"{local_file_path} uploaded to gs://{bucket_name}/{gcs_object_name}")
        
        # 업로드 시간
        upload_time = datetime.datetime.utcnow()
        
        # Blob upload한 Logs 떨구기
        with open("%s/%s_blob_logs.json" %(log_local_directory, nowDate), "r") as json_file:
            data = json.load(json_file)

        data['id'].append(file_name)
        data['time'].append(upload_time)
        data['http_status'].append(load_blob.status_code)
        data['from'].append("local_path:"+local_file_path)
        data['to'].append("gcs_path:"+gcs_object_name)

        with open("%s/%s_blob_logs.json" %(log_local_directory, nowDate), "w") as json_file:
            json.dump(data, json_file, indent=4)        
            print('blob logs recorded')