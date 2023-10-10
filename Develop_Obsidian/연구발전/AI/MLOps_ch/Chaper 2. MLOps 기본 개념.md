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

dt = np.dtype([("corp_start", "S10"), ("corp_end", "S10"), ("distance", int)])
data_set = np.array(values, dtype=dt)

def all_corps():
	corps = {}
	corp_set = set(data_set["corp_end"])
	for corp in corp_set:
		corps[corp] = ""
	return corps

def randomize_corp_start(corps):
	return random.choice(corps)

def get_shortest_route(routes):
	route = sorted(routes, key=lambda dist: dist[2]).pop(0)
	return route

# verbose 0=출력하지 않음, 1=자세히, 2=함축적 정보
def greedy_path(verbose=False):
	start_corp = randomize_corp_start(list(all_corps().keys()))
	print(f"시작회사: {start_corp}")
	
	itinerary = []
	corps_visited = {}
	count = 1
	while True:
		possible_routes = []
		if verbose:
			print('-----')
			print(f"회사 {start_corp} 에서 갈 수 있는 회사들")
		for path in data_set:
			if start_corp in path["corp_start"]:
				#한 번 방문했던 회사는 다시 방문이 불가능
				if path["corp_end"] in corps_visited:
					continue
				else:
					if verbose:
						print(f"{path}, end=", "")
					possible_routes.append(path)
		if not possible_routes:
			if verbose:
				print('더 이상 갈 수 있는 회사가 없습니다. 여행을 종료합니다.')
				print('-----')
			break
		# 다음으로 방문할 수 있는 회사들 중에서 가장 짧은 거리의 회사를 선택합니다.
		route = get_shortest_route(possible_routes)
		if verbose:
			print(f"\n다음 여정: {route} ({count} 번째 동선 입니다.)")
		count += 1
		itinerary.append(route)
		# 방문한 회사를 기록합니다.
		corps_visited[route[0]] = count
		
		if verbose:
			print(f"방문한 회사들: {corps_visited}")
			print(f"현재까지의 여정: {itinerary}")
		start_corp = route[1]
	
	return itinerary

def get_total_distance(complete_itinerary):
	distance = sum(z for x, y , z in complete_itinerary)
	return distance

def lowest_simulation(num):
	routes = {}
	for _ in range(num):
		itinerary = greedy_path()
		distance = get_total_distance(itinerary)
		print(f"총 거리: {distance}")
		routes[distance] = itinerary
	shortest_distance = min(routes.keys())
	route = routes[shortest_distance]
	return shortest_distance, route

def main():
	if len(sys.argv) == 2:
		iterations = int(sys.argv[1])
		print(f"{iterations}회 시뮬레이션을 실행합니다.")
		distance, route = lowest_simulation(iterations)
		print(f"최단거리: {distance}")
		print(f"최적경로: {route}")
	else:
		itinerary = greedy_path(verbose=True)
		print(f"동선: {itinerary}")
		print(f"총 거리: {get_total_distance(itinerary)}")
if __name__ == "__main__":
	main()

```

탐욕 알고리즘을 통해 시뮬레이션을 반복하였을 때 반복 횟수가 적었을 수도 있다.

탐욕 알고리즘 기반의 최적화를 포함하여 다양한 최적화 알고리즘은 수많은 지역 최소점에 빠질 수 있음
아무리 많이 반복하더라도 세상에서 가장 좋은 경로를 발견하지 못할 수도 있다.
즉, 이 말을 전역 최소점에 도달하지 못했을지도 모른다. 라고 할 수 있음

머신러닝에서 자주 사용되는 경사 하강법도 최적화 알고리즘의 일종이다.
머신러닝 모델들은 경사 하강 알고리즘을 이용해 손실을 최소화 하는 방향으로 학습됨

> 딥러닝에서 얻으면 좋은 직관
> 경사 하강 알고리즘의 시각적 이해를 돕는 도구로 텐서플로 플레이그라운드가 있음
> 텐서플로 플레이그라운드에서는 학습률 변화에 따라 모델의 학습 결과가 어떻게 달라지는지를 시각화 해볼 수 있음
> 학습률이 너무 높을 때 - 미세한 수렴이 일어나지 않아 손실이 더 이상 감소하지 않고 0.984에 머물러 있음
> 학습률이 너무 낮을 때 - 수렴이 완료되기까지 오랜 시간이 걸리거나 지역 최소점으로 수렴할 수 있다는 사실을 알수 있음

### 머신러닝의 핵심 개념
머신러닝은 컴퓨터가 명시적인 소스 코드 없이도 데이터로부터 규칙을 학습하도록 만드는 것이라고 볼 수 있음

머신러닝은 
(지도학습(supervised training)), 
(비지도 학습(unsupervised training)), 
(강화 학습(reinforcement))로 나뉨

지도학습은
레이블(label)(혹은 '라벨'이라고도 불림)
이 제공되는 경우 사용이 가능
과거 데이터를 기반으로 학습

모든 머신러닝 모델은 스케일링된 숫자 형식의 데이터로 학습한다는 사실을 유념함

비지도 학습은 레이블을 '발견 discover'하는 데 사용되기도 한다.
머신러닝 모델은 다양한 기준에 따라 여러 군집을 생성하고, 군집은 레이블이 없는 데이터의 분류 기준으로 삼을 수 있음
적절히 군집화된 결과물을 '발견'이하고 분류 기준을 선택하는 것은 온전히 도메인 전무낙의 몫임

이러한 알고리즘을 '군집화'라고 부르며 군집 중 하나를 '최고best'의 선수라는 레이블을 붙임

득점, 리바운드, 블로킹, 어시스트 네 가지 기준으로 NBA 선수들을 분류
군집화 알고리즘을 통해 르브론 제임스와 케빈 듀란트가 동일한 군집으로 배치된 이유는 머신러닝 모델이 보기에 둘은 서로 유사한 강점을 가지고 있기 때문일 것

강화학습은 '에이전트'가 지시 받은 작업을 수행하기 위해 반복적으로 주어진 환경에서 도전과 실패를 반복함
AWS DeepRacer는 자동차가 에이전트가 트랙 환경을 주행하며 학습하기 위한 목적으로 만들어진 플랫폼임

자동차는 트랙의 일정 구간들을 이동하고 플랫폼은 자동차가 트랙의 어느 구간에 있는지를 기록
보상(Reward) 함수는 자동차가 트랙의 특정 구간을 통과할 때마다 앞서 저장한 기록들을 바탕으로 에이전트에게 주는 보상을 달리하여 적절한 액션을 유도
보상함수의 전략이 다르다면 완전히 다른 결과가 나올 수 있기 때문에 이러한 유형의 모델을 훈련할 때는 무작위성이 큰 역할을 함

다음 분기에 판매될 제품의 판매량을 예측해야하는 상황 - 과거 데이터를 바탕으로 추이를 학습하여 미래의 상황을 추론하는 지도 학습 방식을 사용해야 함

## 데이터 과학 해보기
데이터 과학은 구글 코랩 같은 '노트북' 형태의 파이썬 실행환경에서 이루어짐
필자가 제안하고 싶은 구조
데이터 가져오기, 탐색적 데이터 분석(EDA), 모델링, 결론으로 구성
정형화된 구조를 자추면 머신러닝 프로제그에 대한 맥락을 온전히 이해하지 못하고 있더라도 그 사람에게 도움이 될 만한 내용이 포함된 섹션으로 빠르게 이동해 내용을 참고할 수 있게 됨

프로덕션 서비스에 사용되는 모델의 경우 README 파일처럼 기능할 수 있는 노트북 파일을 동봉하면 추후 소스 코드와 모델을 이해하는데 도움이 된다.
데이터 가져오기(Ingest)에 해당하는 부분은
데이터를 웹에서 불러와 판다스 라이브러리 등이 제공하는 데이터 컨테이너에 저장하는 작업을 수행

### 데이터 가져오기를 수행하는 영역
```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
df.head()
```

### EDA 영역
데이터를 탐색하며 분석하는 일에 사용되는 영역
데이터의 생김새, 모양, 분포도 등을 시각화하는 영역
Plotly를 사용하면 데이터를 시각적으로 이쁘게 표현 가능
```python
import plotly.io as pio
pio.renderers.default = 'colab'
import plotly.express as px
fig = px.scatter(top_states_march_current_df, x=top_states_march_current_df.index, y="cases", size="edaths", color="state", facet_col="state")
fig.show()
```

### 모델링 영역
말 그대로 모델을 만드는 작업에 사용
자동차 연비를 추론하기 위해 딥러닝 모델을 만드는 영역이 이에 해당함
모델링 - 학습을 통해 생성된 머신러닝 모델은 클라우드와 Flask API를 이용해 배포할 수 있음

### 결론 영역
비즈니스 리더의 의사결정에 도움을 줄 수 있도록 요약된 핵심 인사이트를 전달하는 목적으로 사용됨

마지막으로 깃허브 등 소스 코드 저장소에 프로젝트를 업로드
MLOps 포트폴리오 하나를 추가하는 것임
이 작업은 머신러닝 프로젝트를 성공시키는 것 만큼 중요함
운영팀 입장에서는 모델이 개발된 배경과 관련된 초기 아이디어 이해할 수 있으므로, 프로덕션 서비스에서 모델 존속 여부를 결정하는 데 크게 도움을 받을 수 있음

## 간단한 파이프라인 밑바닥부터 
애저 앱 서비스에 플라스크 머신러닝 애플리케이션을 배포하는 작업을 진행
깃허브 이벤트는 애저 파이프라인 빌드 프로세스가 빌드 작업을 시작하도록 트리거하고, 빌드가 끝나면 서버리스 플랫폼에 변경된 사항을 배포, 동일한 역할을 하는 서비스라도 애저, AWS, GCP에서 각각 이름이 조금 다를 수는 있지만 대응되는 서비스끼리의 역할은 결국 비슷함
![[IMG_0252.jpeg]]

클라우드에 올리기 전에 로컬에서 테스트 해 볼 수 있는 작업

1. 가상환경을 생성하고 source 명령으로 활성화하기
```python
python3 -m venv ~/.flask-ml-azure
source ~/.flask-ml-azure
```
2. make install 명령을 실행
3. python app.py 명령을 실행
4. 새로운 터미널을 열고 작업 경로로 이동해서 ./make_prediction.sh 명령을 실행

로컬에서 입력한 명령들이 문제없이 동작하면 이제 애저 클라우드를 실행

1. 애저 클라우드 셸을 실행
2. 애저 파이프라인이 활성화된 깃허브 저장소를 만든다.
3. 프로젝트 디렉토리를 깃허브 저장소에 푸시한다.
4. 애저 클라우드 셸에서 애저 파이프라인이 활성화된 깃허브 저장소를 클론한다.
5. 가상환경을 생성하고 source 명령어로 가상환경을 활성화
6. make install 명령어로 필요한 것들을 설치함
7. (az webapp up -n (your-appservice))
8. URL(https://(your-appservice).azurewebsites.net/)에 접속하여 배포된 애플리케이션이 잘 작동하는지 확인한다.
9. 머신러닝 모델에 추론 작업 요청이 가능한지 확인
10. 애저 DevOps 프로젝트를 생성하고 애저에 연결. 자세한 내용은 애저 공식문서를 참고
11. 애저 리소스 매니저에 연결
12. az webapp up 명령어를 사용했을 때 자동으로 생성된 리소스 그룹에 연결
13. 깃허브와 연동된 파이썬 리눅스 웹 애플리케이션 파이프라인을 생성
14. app.py를 수정한 커밋을 깃허브 저장소에 푸시하고 애저 파이프라인을 이용한 지속적 배포가 정상적으로 작동하는지 확인해보기.
15. YAML 파일에 코드 구문 오류를 방지해주는 린트 스텝을 추가해보고, 린트의 정상 작동을 확인해본다.

머신러닝의 프로덕션 환경까지 끌어오는 기본적인 지식들이 정리되어 있음
MLOps는 목표 달성을 위한 행위의 일종
이 분야가 너무 다양한 분야의 기술과 지식을 요구하기 때문에 복잡도가 크게 상승한다는 점

다양한 기술들이 복잡하게 얽힌 내용을 다룰 때는 항상 작은 것부터 시작하는게 좋다.
간단하고 작은 솔루션이 잘 작동하도록 만들고 난 이후에 조금씩 복잡성을 더하며 확장해나가야 함

