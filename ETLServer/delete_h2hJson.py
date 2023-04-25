#폴더 내 json 파일을 차차 읽고 key가 data인 value 가 빈칸이면 해댱 json을 삭제시키는 거

import json, os
from datetime import datetime


now_date = datetime.utcnow().date().strftime("%y%m%d")
print(now_date)

directory = os.path.join(os.path.dirname(__file__), 'datas/DataLake/fixtures/h2h', now_date)

file_list = os.listdir(directory)

#print(file_list)

for file_name in file_list:
	file_path = os.path.join(directory, file_name)

	try:
		with open(file_path, "r") as r:
			file_data = json.load(r)
			print(file_data)


			if "data" in file_data and not file_data["data"]:
				os.remove(file_path)
				print(f"file deleted {file_path}")

			else:
				print(f"file valid : {file_path}")


	except json.decoder.JSONDecodeError as e:
		print("error")
		print(f"error :{e}")
		
