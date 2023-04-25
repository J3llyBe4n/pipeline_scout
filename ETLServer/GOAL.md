###
여기는 주간 챌린지 / 일간 챌린지 및 기타 소통 창구입니다
###


2023.04.20
==========

## ETL Server 구조도 수정
#### 경과
- Before : API[Module, Main, Data], DB[모듈, Main, Data]
- After : DB_Main, API_Main, Module, Data
#### 고민 및 시도
1. 동일 기능을 가진 스크립트를 폴더로 관리하지 않을 경우 추후 import 과정에서 경로 설정이 어려움
- 구조도를 수정
2. 운영체제마다 가지는 디렉토리의 절대경로가 다름
- 상대 경로로 외부 라이브러리를 import하는 방법 모색

## ubuntu 이미지 기반 Docker 컨테이너 생성
#### 경과
- VIM 설치
- Python 3.8 설치
#### 고민 및 시도
1. apt-get install -y python 명령어로 설치 시 최신 버전 설치, 버전 지정 설치 불가
- apt-get install -y software-properties-common
- Ubuntu / Debian 리눅스 시스템의 소프트웨어 소스 추가 및 관리용 유틸리티와 라이브러리 제공

## api-func의 테스트
#### 경과
- tmp 데이터를 json 파일로 적재 및 폴더 생성
- response 데이터를 pipe_league 테이블에 적재
- 기능마다 팀원 각자 script를 작성해 비교 분석하고 하나를 골라 merge
#### 고민 및 시도
1. 각자의 코드 구현 방식이 달라 merging에 시간이 소요되고 오류 발생
2. 함수명과 변수명의 중복 및 유사성에 의한 오류 발생

## 차회 목표
1. crontab 으로 스케쥴링 api req 전송
2. team table 적재 및 log json 파일 저장 여부 확인
3. [추가] url 별 doc 구상


2023.04.21
==========
<<<<<<< HEAD

## 회의 내용
1. 하나의 script 내에서 request limit을  초과하는 문제
- sleep() / 인당 기능을 담당하여 각자의 key로 request 수 관리
- 추후 구조화 및 needs 파악을 통해 script 구조도 확립 후 request 배치
2. 역할 분담
- 1명 : 기존 script의 refactoring함수 및 변수명 수정, 중복값을 함수 또는 클래스 내로 정리, 주석 정리
> 함수 및 변수명 수정, 중복값을 함수 또는 클래스 내로 정리, 주석 정리
- refactoring 방향 : 코드 실행 속도(성능) 중심 / 구조 rebuilding 지양
- 변수, 함수명 : 2개 이상의 hypen지양
> word_camelWord or word_word
- 2명 : uri 별로 datalake용 script 생성 및 관리 
3. request 정보 적재용 json 파일 갱신 방향성 고려
- {data : []}를 초기 형태로 입력, data의 value값인 list를 읽고 .append() 수향
4. cron user의 기능별 분류 고려

## pipe_team 테이블 적재
#### 고민 및 시도
1. 해외 일부 리그의 특성으로 인해 여러 리그가 team info를 공유하는 문제
> 일부 team info가 중복 입력
- query의 수동 입력으로 중첩 제거 : 수가 적으므로

## 차후 목표
1. uri별 script 작성 및 기존 코드 refactoring
2. branch 작업
3. cron 실행 test


2023.04.22
==========

## cron test
#### 경과
- 이전에 생성한 'crontest' 컨테이너에 mysql-connector-python, requests 모듈 설치
- 간단한 script 파일을 .py 확장자로 생성하고 crontab에 명령문 작성
- script 정상 실행 여부 확인
#### 고려해야 할 사항들
- crontab script 마지막에 blank row가 없으면 바로 위 제어문이 실행되지 않음
- service cron start / service cron end
#### 고민 및 시도
1. python 3.10으로 강제 mapping되어 스크립트가 실행되지 않는 현상
-  /usr/bin/python3.8로 python 버전 지정
2. python 3.8에 모듈이 설치되지 않는 문제 (원인 : 3.8 버전에 distutils가 없음)
- apt-get install python3.8-distutils -y
- python3.8 -m pip install [모듈명]
3. script가 실행되지만 파일 생성 명령어가 실행되지 않는 문제 (원인 : cron이 경로 반환을 못 함)
- script 내부의 모든 디렉토리를 절대 경로로 지정하여 반환(예 : with open("/tester.py", "w") as file)
- realpath [파일/폴더명] 명령어로 절대경로 확인 및 반환
4. cron 실행 자체가 안 되는 현상
- chmod +x /tester.py 의 방식으로 읽고 쓸 파일에 권한 부여
5. syslog 파일이 보이지 않거나 읽을 수 없는 문제
- 임의의 .log 파일을 만들어 syslog에 적재되는 정보를 자동 적재하도록 수동 설정
- 확인중

## 컨테이너 환경에 대한 이해
1. vim [파일명] 으로 파일 수정
2. cat [파일명] 으로 파일 읽기, 내부에 스크립트가 없으면 터미널에 아무것도 뜨지 않음

## 차후 목표
1. 컨테이너의 셋팅 및 환경 정보의 자체 규격화 및 배포 (장기 목표)
2. uri별 script 작성 및 기존 코드 refactoring
3. branch 작업


23.04.22
=======
=======
hi woorek
>>>>>>> da45bcb4677238df081ea5bb296ee0694ad96afe
