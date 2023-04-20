import requests as re
import time

# uri = 'https://v3.football.api-sports.io/teams?id=42&league=39&season=2022'

uri = 'https://v3.football.api-sports.io/status'
headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': 'a86d420d0d8840c8e722e16cf9742f7b'
        }
startTime = time.time()
resp = re.get(url=uri, headers=headers)
# responseTime = round((time.time() - startTime),4)
responseTime = (time.time() - startTime)
responseStatus = resp.status_code
responseHeaders = resp.headers


print(responseTime)
print(responseStatus)
print(responseHeaders)
