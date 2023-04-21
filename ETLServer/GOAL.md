###
여기는 주간 챌린지 / 일간 챌린지 및 기타 소통 창구입니다
###

2023.04.20
==========

### ETL Server 구조도 수정
Before : API[Module, Main, Data], DB[모듈, Main, Data]
After : DB_Main, API_Main, Module, Data
#### 고민 및 시도
- 동일 기능을 가진 스크립트를 폴더로 관리하지 않을 경우 추후 import 과정에서 경로 설정이 어려움
> 구조도를 수정
- 운영체제마다 가지는 디렉토리의 절대경로가 다름
> 상대 경로로 외부 라이브러리를 import하는 방법 모색

### ubuntu 이미지 기반 Docker 컨테이너 생성
- VIM 설치
- Python 3.8 설치
#### 고민 및 시도
- apt-get install -y python 명령어로 설치 시 최신 버전 설치, 버전 지정 설치 불가
> apt-get install -y software-properties-common
: Ubuntu / Debian 리눅스 시스템의 소프트웨어 소스 추가 및 관리용 유틸리티와 라이브러리 제공

### api-func의 테스트
#### 경과
- tmp 데이터를 json 파일로 적재 및 폴더 생성
- response 데이터를 pipe_league 테이블에 적재
- 기능마다 팀원 각자 script를 작성해 비교 분석하고 하나를 골라 merge
#### 고민 및 시도
- 각자의 코드 구현 방식이 달라 merging에 시간이 소요되고 오류 발생
- 함수명과 변수명의 중복 및 유사성에 의한 오류 발생

### 익일 목표
1. crontab 으로 스케쥴링 api req 전송(crontab 사용 연습)
2. team table 적재 및 log json 파일 저장 여부 확인
+). url 별 doc 구상


2023.04.21
==========