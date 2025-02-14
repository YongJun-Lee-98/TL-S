## 실행
django-admin command options
manage.py command options
python -m django command options

각 애플리케이션에서 제공하는 사용법 정보와 명령어 목록을 표시
### 2. django-admin help

사용 가능한 모든 명령 목록을 표시하려면 실행
### 3. django-admin help -commands

주어진 명령에 대한 설명과 사용 가능한 옵션 목록을 표시하려면 실행
### 4. django-admin help command

## 앱 이름
"앱 이름" 목록을 사용
"앱 이름"은 모델이 포함된 패키지의 기본이름
INSTALLED_APPS 문자열이 포함된 경우
'mysite.blog' 앱 이름 입니다.

## 버전 확인
django-admin version
현재 Django 버전을 표시 django-admin version
## 디버그 출력 표시
--verbosity 지원되는 경우를 사용하여 django-admin 콘솔에 인쇄되는 알림 및 디버그 정보의 양을 지정

---
## 사용 가능한 명령

### check
```bash
django-admin check [app_label [app_label]]
```
시스템 검사 프레임워크를 사용하여 전체 Django 프로젝트에서 일반적인 문제를 검사
기본적으로 모든 앱이 확인됨. 앱 라벨 목록을 인수로 제공하여 앱의 하위 집합을 확인

사용예시
```bash
django-admin check auth admin myapp
```
#### --tag TAGS, -t TAGS
시스템 검사 프레임워크는 태그로 분류된 다양한 유형의 검사를 수행
이러한 태그를 사용하여 특정 카테고리의 검사만 수행되도록 제한할 수 있음
모델 및 호환성 검사만 수행할 경우 아래를 실행
```bash
django-admin check --tag models --tag compatibility
```
### --database DATABASE
데이터베이스 액세스가 필요한 검사를 실행하도록 데이터베이스를 지정
```bash
djago-admin check --database default --database other
```
--list-tags
사용 가능한 모든 태그를 나열
--deploy
배포 설정에만 관련된 몇 가지 추가 검사를 활성화

--fail-level {CRITICAL, ERROR, WARNING, INFO, DEBUG}
명령이 0이 아닌 상태로 종료되도록 하는 메세지 레벨을 지정

## compilemessages
### django-admin compilemessages
내장된 GetText 지원과 함께 사용할 파일로 생성된 파일ㅇ르 컴파일함
--locale LOCALE, -l LOCALE
처리할 로케일을 지정함
제공하지 않으면 모든 로케일을 지정

--exclued EXCLUDE, -x EXCLUDE
처리에서 제외할 로케일을 지정
제공하지 않으면 로케일이 제외되지 않음

--use-fuzzy, -f
컴파일된 파일에 퍼지 번역을 포함

--ignore PATTERN, -i  PATTERN

## createcachetable
django-admin createcachetable
