import os
import json

directory = os.path.join(os.path.dirname(__file__), 'DataLakes')

def create_teamsInfoFolder():
    if not os.path.exists("%s/teams/information" %directory):
        os.mkdir("%s/teams/information" %directory)
        print("folder created")
    else:
        print("already exists!")

def create_teamsInfoJson():
    
    season = 2022

    data_dict = {}
    # 팀_2022.json
    with open(f"{directory}/teams/information/team_{season}.json", '+a') as file:
        json.dump(data_dict, file)
