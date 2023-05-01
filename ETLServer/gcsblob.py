import os
from google.cloud import storage

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
            blob.upload_from_file(file)
            print(f"{local_file_path} uploaded to gs://{bucket_name}/{gcs_object_name}")