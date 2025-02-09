
```bash
python -m django --version
```
프로젝트 생성 시 사용 중인 이름은 피해야 함
django 라는 이름은 Django 그 자체와 충돌이 일어남
test는 Python 패키지 이름 중 하나

코드가 서비스 되어야 하는 위치
PHP는 /var/www 웹 서버의 최상단 문서에 넣는게 익숙하겠지만
Django는 /home/mycode 와 같은 DocumentRoot 의 바깥에 두는 것을 권장함

## startproject에서 생성되는 것들
mysite/
	manage.py
	mysite/
		__ init __ .py
		settings.py
		urls.py
		asgi.py
		wsgi.py

manage.py : 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
DJANGO_SETTINGS_MODULE 프로젝트 settings.py 파일을 가르키도록 환경 변수를 지정
.NET을 통해 Django를 설치한 경우 스크립트 django-admin는 시스템 경로에 있어야함
pip 경로에 없는 경우 가상 환경이 활성화 되었는지 확인

manage.py 일반적으로 
단일 Django 프로젝트를 작업 시 django-admin
