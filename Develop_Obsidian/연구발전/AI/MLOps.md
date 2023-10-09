본 내용은 [MLOps 실전 가이드](https://m.hanbit.co.kr/store/books/book_view.html?p_code=B9385341956)를 학습하면서 남기는 내용입니다.

### 머신러닝 엔지니어링의 도구들
클라우드 네이티브 머신러닝 플랫폼
- AWS 세이지메이커, 애저 머신러닝 스튜디오, GCP AI플랫폼
컨테이너형 워크플로
- 컨테이너, 쿠버네티스, 프라이빗/퍼블릭 컨테이너 레지스트리
서버리스 기술
- AWS 람다, AWS 아테나, 구글 클라우드 함수, 애저 함수
머신러닝에 특화된 하드웨어
- GPU, 구글 텐서 처리 장치(TPU), 애플 A14
빅데이터 플랫폼과 데이터 처리 도구
AWS S3, GCS, 데이터브릯, 하둡/스파크, 스노우 플레이크, 아마존 EMR, 구글 빅쿼리

머신러닝 모델이 실제 서비스를 통해 문제를 해결하는 단계로 자연스럽게 이동하지 못한다는 것은 업계에서 산업 표준으로 MLOps의 필요성을 요구하게 된 계기가 되엇음

MLOps는 DevOps 방법론을 사용하여 머신러닝을 자동화하는 프로세스라고 생각하면 된다.

## DevOps & MLOps
DevOps의 목적 = 고품질 소프트웨어를 빠르게 출시하는 것을 조직의 목표로 삼는 곳에서 사용되는 일련의 기술 및 관리 전반을 일컫는다.

### 지속적 통합
> Continuous Integration(CI, 지속적 통합)은
> 소프트웨어 프로젝트를 지속적으로 테스트
> 테스트 결과를 바탕으로 소프트웨어 품질을 향상시키는 프로세스
> 테스트 자동화 라고도 불림 - 오픈소스
> Saas 빌드 서버 (ex: 깃허브 액션, 젠킨스, 깃랩, 서클CI)
> 클라우드 네이티브 빌드 시스템 (ex: AWS 코드 빌드)

### 지속적 배포
> 다양한 Continuous Deployment(CD) 방법을 통해
> 사람의 개입 없이 새로운 환경에 코드를 전달할 수 있음
> CD는 코드형 인프라를 사용하여 코드를 자동으로 배포하는 프로세스

### 마이크로서비스
> 의존성이 거의(혹은 아예) 없고 독립적인 기능을 가진 소프트웨어 서비스
> 예로 머신러닝 추론 엔드포인트(endpoint)는 마이크로 서비스로 구성하기 매우 적합함
> 대표적으로 플라스크(Flask)는 파이썬 기반 마이크로서비스 구현을 돕는 프레임워크 중 하나임
> AWS 람다 - 클라우드에서 제공되는 다양한 서비스형 함수를 대표
> 마이크로 서비스는 컨테이너 환경에서 즉시 실행 가능하도록 구성이 가능함
> 서비스형 컨테이너(CaaS)를 사용해서 도커파일 + 플라스크 애플리케이션을
> AWS 파게이트, 구글 클라우드런, 애저 앱 서비스 등 서비스에 손쉽게 배포가 가능함

### 코드형 인프라
> IaC(Infrastructure as Code, 코드형 인프라)는 
> 인프라를 소스 코드의 형태로 보관하고 배포하는 프로세스를 의미함
> 인프라에 변경 사항이 있다면 코드를 변경하고 반영하면 된다.
> 인프라를 구축하기 위해 추가적인 수작업이 필요하지 않도록 돕는다.
> 많이 사용되는 기술 : AWS 클라우드 포메이션, AWS SAM 등의 클라우드 전용 IaC
> 풀루미, 테라폼과 같은 멀티 클라우드 서비스도 고려해 볼 수 있다.

### 모니터링
> 조직의 현재 소프트웨어 시스템의 성능과 신뢰성에 대해 판단하고 적잘한 의사결정을 내릴 수 있도록 돕는 프로세스 및 기법
> New Relic, DataDog, Stackdriver와 같은 애플리케이션 성능 모니터링 도구들이나 간단한 로깅 라이브러리를 이용할 수 있음
> 프로덕션 환경에 배포된 애플리케이션이나 데이터 과학 소프트웨어 시스템이 어떻게 작동하고 있는지와 관련된 데이터를 수집하여 카이젠 철학이 적용
> 데이터 중심으로 움직이는 조직은 매일 또는 매주 문제들을 조금씩 개선하기 위해 시스템과 측정항목을 모니터링 한다.

### 효과적인 기술 소통
> 기술적으로 단순하고, 강력하며, 여러 번 재사용 가능한 수단과 방법을 적절히 이용하는 것을 의미함
> 프로젝트 초기에 프로토타이핑을 위해 AutoML을 채택하는 것이 효과적인 기술 소통의 좋은 예시임
> 시스템의 고도화 도중 AutoML의 모델은 폐기될 수 있으나 다루기 어려운 문제에 리소스가 낭비되는 것을 방지하는 좋은 도구가 됨

### 효과적인 기술 프로젝트 관리
> 인력과 도구를 적절히 사용하여 프로젝트를 관리하는 것
> 티켓 시스템이나 스프레드시트와 같은 도구를 활용할 수 있음
> 기술 프로젝트를 훌륭하게 관리하기 위해 해결해야 하는 문제를
> 작은 단위로 세분화하여 점진적으로 발전하도록 구성해야 함
> 머신러닝 작업에서 나타나는 안티패턴(실제로 많이 사용하는 문제 해결 패턴이지만 비효율적이거나 비생산적인 결과를 낳는 패턴을 의미)
> 문제를 '완벽하게' 해결하는 딱 하나의 머신러닝 모델을 만들기 위해 팀 전체가 매달리는 형태 보다는 매일 또는 매주 작은 단위로 분해된 문제를 부여 받고 점진적으로 해결해나가는 방식을 채택하는 것이 모델 구축의 성공 가능성을 높인다.

## DevOps 구현
파이썬 프로젝트의 경우는 다른 언어로 구성된 프로젝트들에 비해 지속적 통합이 수월한 편에 속함
깃 허브 저장소 - (메이크파일, requirements.txt, hello.py, test_hello.py)
테스트 자동화의 첫 번째 단계는 'scaffold'를 구성하는 것
### 메이크 파일
> 유닉스 기반 운영체제와 함께 제공되는 
> 메이크(make) 시스템을 통해 파일에 작성된 명령을 실행함.
> 메이크파일을 잘 활용하면 앞으로 살펴볼 지속적 통합과 관련된 단계들을 한데 묶어 단순화하는 도구로 사용할 수 있다.

### MAKEFILE 파일과 관련있는 다른 파일 종류들

| 신장                                                             | 파일 종류 개발자      | 파일 카테고리 | 파일 종류 기술                         |
| ---------------------------------------------------------------- | --------------------- | ------------- | -------------------------------------- |
| [.MAK](https://www.fileviewpro.com/ko/file-extension-mak/)       | Sublime HQ Pty Ltd    | 개발자 파일   | Makefile                               |
| [.WLF](https://www.fileviewpro.com/ko/file-extension-wlf/)       | Microsoft Corporation | 데이터 파일   | Microsoft Windows 98/Me Dr. Watson Log |
| [.ONETOC](https://www.fileviewpro.com/ko/file-extension-onetoc/) | Microsoft Corporation | 설정 파일     | Microsoft OneNote Table Of Contents    |
| [.CPR](https://www.fileviewpro.com/ko/file-extension-cpr/)       | Steinberg             | 오디오 파일   | Cubase Project                         |
| [.FOLDER](https://www.fileviewpro.com/ko/file-extension-folder/) | Microsoft Corporation | 시스템 파일   | Microsoft Windows Explorer Folder File |
| [.CPL](https://www.fileviewpro.com/ko/file-extension-cpl/)       | Microsoft Corporation | 시스템 파일   | Windows Control Panel Item             |
| [.~CU](https://www.fileviewpro.com/ko/file-extension-~cu/)       | Unknown Developer     | 시스템 파일   | Windows Cursor File                    |
| [.VCG](https://www.fileviewpro.com/ko/file-extension-vcg/)       | Microsoft Corporation | 텍스트 파일   | SharePoint WorkSpace vCard Contact     |
| [.GAU](https://www.fileviewpro.com/ko/file-extension-gau/)       | Microsoft Corporation | 기타 파일     | Flight Simulator Gauge File            |
| [.WK1](https://www.fileviewpro.com/ko/file-extension-wk1/)       | IBM                   | 데이터 파일   | Lotus Worksheet                        |

### Make install
make install 명령어로 소프트웨어를 설치
### Make lint
make lint 명령어로 구문 오류를 확인
### Make test
make test 명령어로 테스트를 실행 (.mak)
```mak
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R, C hello.py
test:
	python -m pytest -vv --cov=hello test_hello.py
```

### requirements.txt (python에서의)
pip에서 사용하는 규약임
pip freeze를 통하여 생성이 가능함 (직접 만들 수도 있음)
```bash
pip freeze > requirements.txt
```
Make 파일로 실행이 가능하지만 개별적으로 실행할 경우
```bash
pip install -r requirements.txt
```
명령어를 통해 설치도 가능함

### 소스 코드와 테스트
#### hello.py
```py
def add(x, y):
	"""This is an add function"""
	return x + y
print(add(1, 1))
```
위의 코드는 소스코드로 외부 파일(hello.py)로 작성되어 있는 형태이다.
아래는 위의 코드와 동일한 위치에 있으며
함수를 사용하기 위해서 불러오는 형태
#### test_hello.py
```py
from hello import add

def test_add():
	assert 2 == add(1, 1)
```

#### 파이썬 가상환경 만드는 방법
```bash
python3 -m venv ~/.your-repo-name
```
.your-repo-name은 다른 이름으로 변경을 하여도 되는 가상환경의 이름이다.

#### 파이썬 가상환경 실행시키기
```bash
source ~/.your-repo-name/bin/activate
```
가상환경 만들기에서 .your-repo-name을 변경했다면 source에서도 변경해서 실행시켜야 한다.

## DataOps와 데이터 엔지리어링
DataOps를 수행하기 위해 다양한 상용 도구가 많이 출시되기 시작했음
아파치 에어플로 - 데이터 처리 워크플로 예약, 관리, 모니터링 도구
AWS(데이터 파이프라인, 글루) - 글루: 데이터 소스의 스키마를 감지 -> 데이터 소스의 메타데이터 저장하고, 서버리스 ETL을 수행할 수 있는 제품
AWS (아테나, 퀵사이트) - 데이터를 쿼리하고 시각화하는 기능을 제공

데이터의 크기, 변경 빈도, 품질 및 정제 수준 등을 고려해 알맞은 데이터 저장소와 제품을 선택하는 것도 중요함
많은 회사들이 중앙 집중식 저장소인 데이터레이크를 데이터 엔지리어링과 관련된 모든 활동의 허브로 사용함
데이터 레이크는 높은 내구성과 가용성뿐 아니라 높은 빈도 I/O(입출력) 작업에서 무한에 가까운 확장성을 제공함

### 데이터레이크
아마존 S3와 같은 클라우드 기반 객체 스토리지 시스템의 동의어처럼 사용됨

데이터 엔지니어 직군의 사람들은 아래와 같은 다양한 상황에 대응하는 시스템을 설계하고 구축함
- 주기적인 데이터 수집, 스케줄링된 작업 실행
- 스트리밍 데이터 처리
- 서버리스와 이벤트 기반 데이터 처리
- 빅데이터 관련 작업
- 머신러닝 엔지니어링 작업을 위한 데이터 및 모델 버전 관리

## 플랫폼 자동화
데이터의 흐름을 자동화한 이후에는
머신러닝 솔루션 구축을 위해 조직이 높은 추상화 수준의 플랫폼을 잘 다루고 있는지 점검해 볼 필요가 있다. 

| 조직이 사용하는 플랫폼                         | 조직에 적합한 플랫폼   |
| ---------------------------------------------- | ---------------------- |
| 아마존 S3 등의 클라우드 플랫폼의 데이터 레이크 | 아마존 세이지 메이커   |
| 구글 클라우드 플랫폼 기반의 작업               | 구글 AI 플랫폼         |
| 애저 기반의 작업                               | 애저 머신러닝 스튜디오 |
| 쿠버네티스                                     | 쿠브플로               |

### MLOps의 피드백 루프
#### 재사용 가능한 머신러닝 파이프라인을 이용한 모델 생성 및 재학습
모델을 한번 만들었다고 끝나는 것이 아님, 
데이터가 변하거나 고객의 특성이 변할 수 있고 
심지어 모델을 만드는 사람이 변할 수도 있음. 
따라서 버전화되고 재사용 가능한 머신러닝 파이프라인을 갖춰야 한다.

#### 머신러닝 모델의 지속적 배포
인프라를 포함한 모든 단계가 자동화되면 코드형 인프라를 사용해 모델을 프로덕션에 사용되는 새로운 환경까지 언제든 배포할 수 있게 된다.

#### MLOps 파이프라인에 대한 추적 로그
머신러닝 모델 뿐 아니라 파이프라인 전반에 걸친 다양한 사건들을 추적하는 일은 필수적임
일반적인 프로그램들도 로깅이 중요한 것처럼
머신러닝 엔지니어링에서도 추적 로깅 시스템을 갖추는 것이 매우 중요함
추적 로깅은 문제에 접근하는 방식과 문제를 해결하는 방식에 대한 피드백 루프의 일부 기능이 가능함

#### 미래에 대비하기 윈한 모델 드리프트 모니터링
프로덕션 환경의 머신러닝 시스템에는 끊임없이 새로운 데이터가 주어지낟.
새롭게 주어지는 데이터의 분포가 기존에 학습된 모델에게 불리하게 작용할 수 있음
최종적으로 학습시킨 이후의 다양한 변화를 모니터링하여 모델의 정확도로 인한 제품의 중대한 문제가 발생하기 전에 대응이 가능

#### 배포타깃
플랫폼에 맞게 모델을 만든후 타깃에 배포가 가능함
보통의 경우는 HTTP 엔드포인트에 모델을 배포하는 것이 가장 일반적이지만

엣지 머신러닝의 새로운 패러다임은 "머신러닝 작업에 특화된 전문 프로세서"를 사용함
구글 - TPU, 애플 - A14가 이에 해당함
구글 AutoML 비전과 같은 고수준의 제품들을 포함하고 있는 구글 클라우드 플랫폼은 텐서플로 라이트, 텐서플로.js, 코랄과 같이 다양한 디바이스에 텐서플로 모델을 배포할 수 있도록 제공함

## MLOps 기본 개념
### [[쉘 스크립트]]
#### AWS 클라우드 셸 
\AWS 고유 명령어에 대한 자동완성 기능이 내장된 배시 셸 (자주 사용하는 경우 ~/.bashrc를 수정하여 편리하게 사용하면 됨)

#### vim 편집기
클라우드 셸이 기본으로 제공하는 편집기
CLI의 거의 기본임 [vim FAQ](https://vimhelp.org/vim_faq.txt.html)참조
클라우드 환경에서 자유롭게 사용할 수 있는 AWS 람다와 같은 도구들과 긴밀하게 통합되어있고
복잡한 과정 없이 곧바로 원하는 동작을 수행할 수 있다.

#### 비시 셸과 명령어
각 셸마다의 편의 기능
지셸 : oh-my-zsh
vim : awesome vim

### 파일 목록
ls 명령어에서 -1 플래그는 추가 정보를 포함한 목록을 보여줌
```bash
ls -l
```

### 실행 명령
셸의 실행파일이나 위치를 알아내는 명령어 which
아래 코드는 ls의 명령어가 어디에 저장되어 있는지 알려주는 명령어이다.
```bash
which ls
```

### 파일 탐색
pwd 명령어 : 현재 작업 중인 디렉토리의 전체 경로를 출력
```bash
pwd
```

### 셸의 입출력
하나의 명령을 다른 명령으로 파이핑 하는 것을 입력이나 출력의 결과에 정교한 작업을 추가할 목적으로 셸에서 자주 사용하는 테크닉이다.
비슷한 연산으로는 리다이렉션이 있다.

'hello world this is MLOps' 라는 문장을 echo 명령어를 통해 작성하고
이를 out.txt라는 파일에 작성한다.
cat 명령어를 통해 출력되는 파일 내용은 파이프를 통해 wc 명령어의 입력에 연결됨
wc명령어의 -w옵션은 입력된 문장에서 단어 수를 세고 / -c 옵션은 문자의 수를 세어 출력하게 된다.
```bash
echo "hello world this is MLOps" > out.txt
cat out.txt | wc -c
cat out.txt | wc -w
```

shuf 명령어의 출력을 새로운 파일에 작성하는 스크립트
shuf 명령어는 지정된 행까지 모든 행을 무작위로 섞은 뒤 출력
[openfoodfacts](https://www.kaggle.com/datasets/openfoodfacts/world-food-facts/data)
```bash
time shuf -n 100000 en.openfoodfacts.org.products.tsv > 10k.sample.en.openfoodfacts.org.products.tsv
```
첫 100,000개의 행을 사용하여 무작위로 행을 재배치하고 그 출력값을 새로운 파일에 저장

셸을 사용하면 데이터 사이언스 라이브러리로 처리하기 너무 큰 파일도 간단한 명령어들을 조합하여 작업시간을 줄일 수 있다.

## 클라우드 컴퓨팅 기반과 구성요소
클라우드 컴퓨팅을 시작할 때
['Multi Cloud Onboarding With Cloud Computing' 강의](https://www.youtube.com/watch?v=zznvjk0zsVg)의
멀티 클라우드 개발 환경을 구성하길 권함
[[강연 내용 한글 정리]]

## 파이썬 벼락치기
os 라이브러리의 listdir 함수는 경로에 있는 모든 파일및 디렉토리의 이름을 반환한다.
```python
import os
os.listdir(".")
```
파이썬 파일 작성 뿐 아니라
IPython이나 주피터 REPL도 적극적으로 사용하기 추천한다.
```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/noahgift/regression-concepts/master/height-weight-25k.csv")
```

## 수학 관련 내용
### 기술 통계학과 정규분포
세상의 많은 것들은 정규 분포를 따름

파이썬에서 pandas를 사용해서 데이터를 나열하고 시각화 해보기

데이터 나열
```python
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/noahgift/regression-concepts/master/height-weight-25k.csv")
df
```

데이터 시각화
```python
import seaborn as sns
import numpy as np

sns.lmplot(x="Height-Inches", y="Weight-Pounds", data=df)
```

데이터를 다방면에서 더욱 잘 이해하고 노력하는 과정을 탐색적 데이터 분석(EDA)라고 함

Pandas의 DataFrame 클래스의 describe()메소드를 사용하면 기술 통계들을 쉽게 얻을 수 있다.
```python
df.describe()
```
![[결과 이미지 폴더/Pasted image 20231007120510.png]]

키와 몸무게를 한눈에 시각화하는 결합 커널 밀도 그래프 (kernel density plot)
일반적으로 이러한 형태의 그래프는 정규분포를 시각화하기에 적합하다.
```python
sns.jointplot(x="Height-Inches", y="Weight-Pounds", data=df, kind="kde")
```
![[결과 이미지 폴더/Pasted image 20231007120815.png]]

### 최적화
머신러닝의 본질은 최적화이다.
최적화는 문제에 대한 최선의 또는 충분히 좋은 해결책을 찾는 행위이다.
경사하강법(gradient descent)은 딥러닝에서 핵심적으로 사용되는 최적화 알고리즘.

#### 탐욕 알고리즘
최적화의 이해를 돕기위해 설명된 부분으로
[탐욕 알고리즘(greedy algorithm)](https://github.com/ProtossDragoon/greedy-change) 깃헙을 참고하여 다운받고 
테스트를 통하여 동작을 살펴보는 것

```python
import change

import unittest

  

class TestChange(unittest.TestCase):

def test_get_c500(self):

	alg = change.Algorithm(5000, coin_types={10, 50, 100, 500})
	c500, c100, c50, c10 = alg.calculate()
	self.assertEqual(c500, 10)
	self.assertEqual(c100, 0)
	self.assertEqual(c50, 0)
	self.assertEqual(c10, 0)

def test_get_c500(self):
	alg = change.Algorithm(200, coin_types={10, 50, 100, 500})
	
	c500, c100, c50, c10 = alg.calculate()
	
	self.assertEqual(c500, 0)
	
	self.assertEqual(c100, 2)
	
	self.assertEqual(c50, 0)
	
	self.assertEqual(c10, 0)

def test_get_c500(self):
	alg = change.Algorithm(50, coin_types={10, 50, 100, 500})
	
	c500, c100, c50, c10 = alg.calculate()
	
	self.assertEqual(c500, 0)
	
	self.assertEqual(c100, 0)
	
	self.assertEqual(c50, 1)
	
	self.assertEqual(c10, 0)
	
def test_get_c500(self):
	
	alg = change.Algorithm(40, coin_types={10, 50, 100, 500})
	
	c500, c100, c50, c10 = alg.calculate()
	
	self.assertEqual(c500, 0)
	
	self.assertEqual(c100, 0)
	
	self.assertEqual(c50, 0)
	
	self.assertEqual(c10, 4)
	
def test_get_c500(self):

	alg = change.Algorithm(4290, coin_types={10, 50, 100, 500})
	
	c500, c100, c50, c10 = alg.calculate()
	
	self.assertEqual(c500, 8)
	
	self.assertEqual(c100, 2)
	
	self.assertEqual(c50, 1)
	
	self.assertEqual(c10, 4)
	
if __name__ == "__main__":
	unittest.main()
```
결과가 최선의 개수임을 보장하지는 못함
책에서의 예시로
120원을 결제 한다면
일반적인 경우 큰 단위 동전을 채우고 작은 단위로 넘어가게 됨

일반적인 경우
100 * 1 + 10 * 2 = 120
동전 개수 = 3개

하지만, 60원 짜리 동전이 있다고 한다면
60 * 2 = 120
동전 개수 = 2개
동전 개수 2개가 더 적은 양의 개수로 취급이 가능하지만
탐욕 알고리즘은 이러한 경우 모든 상황을 고려한 최적의 해를 찾지 못할 가능성이 존재함

책에서
최적화 탐욕 알고리즘 큰 틀에서 이해하는데 더 유용한 예시
외판원 문제 (Traveling Salesperson Problem)를 통해 방문해야 하는 회사들의 목록과 그 위치가 주어졌을 때 외판원들은 경로 거리를 어떻게 계산해서 최단거리를 찾을 수 있을까?

[routes.py](https://github.com/ProtossDragoon/greedy-tsp/blob/master/routes.py)는 저자님의 깃헙에서 다운로드
스크립트는 시뮬레이션을 여러 번 반복해서 시뮬레이션 할 수 있도록 구성되어 있음
시뮬레이션을 시작할 때마다 경로 탐색 시작점도 무작위로 선택됨
시뮬레이션을 두번 이상 실행하는 경우 모든 반복에서 찾은 경로의 길이 중 가장 짧은 길이의 경로만 저장되고 나머지는 버려짐
프로그램 사용자는 시간이 허락하는 만큼 시뮬레이션을 반복 실행하면 됨

```python
import sys
import random
import numpy as np
from routes import values

dt = np.dtype([("corp_start", "S10"), ("corp_end", "S10", ("distance", int))])

```