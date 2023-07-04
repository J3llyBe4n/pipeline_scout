from fastapi import APIRouter, Request
#from lib.api_modules import make_json
from utils.football_lib import *

router = APIRouter()

@router.get("/team-static/")
async def return_url_path(request: Request, test: str):
    url = str(request.url).split("?url=")[-1]
    make_json(url, "230101_test.json", "/Users/jesse/Desktop/test/")
    return {"file load done": test}
