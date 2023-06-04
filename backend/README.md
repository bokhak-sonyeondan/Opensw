## Backend 진행상황


### 주요 명령어
- `python3 mange.py runserver` 서버 실행
- `python3 mange.py makemigrations` model 변경 사항을 체크
- `python3 mange.py migrate` 변경사항 db에 반영

### 사용 패키지
- django
- djangorestframework
- django-cors-headers
- django-all-auth
- django-rest-auth

## chat 실행전 확인
- channels, daphne 다운로드 받기
- 윈도우에 docker desktop 다운받고 우분투와 연결 (모르겠으면 연락)
- docker run -p 6379:6379 redis:7 실행(데이터 베이스, 웹소켓 소통 위한 이미지 생성)
- python3 -m pip install channels_redis 설치
- python3 -m pip install selenium 설치
- 실행 전 docker 컨테이너 실행 여부 확인바람
