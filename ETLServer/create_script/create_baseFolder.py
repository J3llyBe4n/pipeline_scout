#이놈은 그냥 우리 프로젝트 전체 기간중 단 한번 도는 친구입니다.
#datas 파일트리 뼈대를 만들어 주는 스크립트입니다.
#fixtures,leagues,players,predictions,standings,teams 디렉토리를 만듭니다.

import os

directory = os.path.join(os.path.dirname(__file__), "../datas/DataLake")

# fixtures
def create_fixturesBaseFolder():
	if not os.path.exists("%s/fixtures" %directory):
		os.mkdir("%s/fixtures" %directory)
		print("folder created")
	else:
		print("already exists!")

# leagues
def create_leaguesBaseFolder():
	if not os.path.exists("%s/leagues" %directory):
		os.mkdir("%s/leagues" %directory)
		print("folder created")
	else:
		print("already exists!")

# players
def create_playersBaseFolder():
	if not os.path.exists("%s/players" %directory):
		os.mkdir("%s/players" %directory)
		print("folder created")
	else:
		print("already exists!")

# predictions
def create_predictionsBaseFolder():
	if not os.path.exists("%s/predictions" %directory):
		os.mkdir("%s/predictions" %directory)
		print("folder created")
	else:
		print("already exists!")

# standings
def create_standingsBaseFolder():
	if not os.path.exists("%s/standings" %directory):
		os.mkdir("%s/standings" %directory)
		print("folder created")
	else:
		print("already exists!")

# teams
def create_teamsBaseFolder():
	if not os.path.exists("%s/teams" %directory):
		os.mkdir("%s/teams" %directory)
		print("folder created")
	else:
		print("already exists!")

create_fixturesBaseFolder()
create_leaguesBaseFolder()
create_playersBaseFolder()
create_predictionsBaseFolder()
create_standingsBaseFolder()
create_teamsBaseFolder()