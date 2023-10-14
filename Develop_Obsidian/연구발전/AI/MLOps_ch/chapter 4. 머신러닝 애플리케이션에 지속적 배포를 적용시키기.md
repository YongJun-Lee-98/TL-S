## 머신러닝 모델 패키징
'모델을 패키징 한다'에서
패키징
DEB 'Debian Package'나 RPM 'Redhat Package Manager'과 같은 패키지 파일을 만든다는 것은 아님
머신러닝 모델 패키징은 모델을 컨테이너 환경에 통합함으로써 컨테이너 기반 프로세스의 장점인 공유, 분산, 배포를 모델에도 쉽게 적용할 수 있도록 만드는 것을 의미함

```txt:requirements.txt
simpletransformers == 0.4.0

transformers == 2.1.0

flask == 2.1.0

torch == 1.8.0

onnxruntime == 1.7.0
```

```Dockerfile
FROM python:3.8

COPY ./requirements.txt /ws/requirements.txt

WORKDIR /ws

RUN pip install -r requirements.txt

COPY ./webapp/app.py /ws

ENTRYPOINT ["python3"]

  

CMD ["app.py"]
```

```python:app.py
from flask import Flask, request, jsonify

import torch

import numpy as np

from transformers import RobertaTokenizer

import onnxruntime

  

app = Flask(__name__)

tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

session = onnxruntime.InferenceSession("roberta-sequence-classification-9.onnx")

@app.route("/predict", methods=["POST"])
def predict():
	input_ids = torch.tensor(
		tokenizer.encode(request.json[0], add_special_tokens=True)).unsqueeze(0)
	if input_ids.requires_grad:
		x = input_ids.detach().cpu().numpy()
	else:
		x = input_ids.cpu().numpy()
	input = {session.get_inputs()[0].name: x}
	out = session.run(None, inputs)
	result = np.argmax(out)
	return jsonify(["positive": bool(result)])

if __name__=="__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
```

이 부분은 m1맥에서는 대부분 작동을 안하는 것 같음

## 머신러닝 모델의 지속적 배포를 위한 코드형 인프라
도커 허브와 같은 공개 저장소에 있는 이미지를 다운로드 받아 사용하는 사람들을 주위에서 흔히 찾아볼 수 있다.
로컬 환경에서 빌드하여 레지스트리에 업로드한 이후 종종 다운로드 받아 사용하던 이미지에 설치되어 있는 패키지 하나를 업데이트해야하는 상황에서
이미지를 처음 만들었을 때 사용했던 도커파일과 소스 코드를 찾아내기위해 뒤져보았지만 실패함
이런 문제가 나타나는 이유는 로컬 컴퓨터에서 컨테이너 이미지를 빌드한 뒤, 빌드된 이미지만 공개 저장소에 푸시했기 때문. 레지스트리에서 호스팅되는 컨테이너 이미지의 장점은 정말 많지만, 한편으론 한번 빌드되어 업로드 된 이후 작은 변경 사항도 반영하기 여럽다는 특징이 단점이 될 수 있음

애플리케이션 소스 코드는 물론 환경에 대한 정보가 명세된 파일을 보관하고 잇는 원격 공개 저장소로부터 정보를 읽어서 컨테이너 이미지를 자동으로 빌드하도록 만들어야 한다.

자동으로 빌드된 컨테이너 이미지가 컨테이너 레지스트리에 푸시되는 일까지도 자동으로 수행되도록 해야한다.

우리는 비효율적인 수작업에 쉽게 익숙해지는 본능을 경계하고 자동화의 기회를 끊임없이 엿보아야 한다.

도커 허브에 컨테이너 이미지를 업로드해두고 반복적으로 사용하던 중 앞서 필자가 겪었던 문제에 맞닥뜨렸다고 가정해보자. 해당 컨테이너 이미지를 호스팅하는 도커 허브 저장소에는 이미지를 다시 빌드하는 일에 도움이 되는 그 어떤 문서도 존재하지 않는다. 또한, 우리가 애플리케이션에 사용하려고 하는 새로운 버전의 모델 파일은 용량이 너무 커서 애저 클라우드의 모델 레지스트리에 보관되어 있다.
이렇게 복잡한 상황이 다시는 나타나지 않도록 모든 것을 자동화하는 방법에 대해 알아보자

애저 모델 레지스트리는 애저 클라우드의 머신러닝 플랫폼에 탑재된 다양한 기능 중 하나다.
제시했던 문제 시나리오에 부합하도록 방금 전 실습에서 사용했던 RoBERTa-SequenceClassification 모델을 애저 머신러닝 스튜디오의 모델 레지스트리에 등록하는 것

프로젝트 루트의
.github/workflows/main.yml
파일 내용
워크플로에는 여러 작업이 포함될 수 있다.
빌드'build'라는 작업만이 워크플로에 포함될 것
클라우드 머신러닝 플랫폼에서 모델을 가져오는 일부터
컨테이너 레지스트리에 빌드된 이미지를 등록하는 일까지 모두 다 '빌드' 작업에서 처리된다.
```yml
name: 머신러닝 모델이 패키징된 도커 컨테이너 이미지를 빌드하고 도커 허브 레지스트리에 푸시한다.

on:

# 메인 브랜치에 푸시되거나 풀 리퀘스트가 발생했을 때 워크플로가 실행됨
	push:
		branches: [ main ]

# 깃허브의 ‘액션’ 탭을 통해 워크플로를 직접 실행할 수 있도록 허용함

workflow_dispatch:

  

jobs:

build:

runs-on: ubuntu-latest

  

steps:

  

- name: 체크아웃

uses: actions/checkout@v2

  

- name: 애저 인증

uses: azure/login@v1

with:

creds: ${{ secrets.AZURE_CREDENTIALS }}

  

- name: 애저 확장 설치 및 사용자 입력 대기모드 방지 설정

run: |

az --version

az config set extension.use_dynamic_install=yes_without_prompt

az extension add -n ml

  

- name: 모델 복원

run: |

az ml model download \

--resource-group Practical-MLOps-Chapter4 \

--workspace-name Practical-MLOps-Chapter4 \

--name RoBERTa-SequenceClassification \

--version 1 \

--download-path . && \

mv RoBERTa-SequenceClassification/* ./webapp/ && \

rm -r RoBERTa-SequenceClassification

  

- name: 도커 허브 로그인

uses: docker/login-action@v1

with:

username: ${{ secrets.DOCKER_HUB_USERNAME }}

password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

  

- name: 깃허브 컨테이너 레지스트리 로그인

uses: docker/login-action@v1

with:

registry: ghcr.io

username: ${{ github.repository_owner }}

password: ${{ secrets.GH_CONTAINER_REGISTRY }}

  

- id: GH_REPOSITORY_OWNER

uses: ASzc/change-string-case-action@v5

with:

string: ${{ github.repository_owner }}

- name: 컨테이너 빌드 후 도커 허브와 깃허브 레지스트리로 동시에 푸시

uses: docker/build-push-action@v2

with:

context: ./

file: ./Dockerfile

push: true

tags: |

${{ secrets.DOCKER_HUB_USERNAME }}/flask-docker-onnx-azure_x86:v1

ghcr.io/${{ steps.GH_REPOSITORY_OWNER.outputs.lowercase }}/flask-docker-onnx-azure_x86:v1
```

위 yaml 파일에서 보 듯 '빌드'라는 하나의 작업은 명확히 구분되는 여러 단계로 구성되어 있음
이렇게 구분되어 있으면 커다란 작업에 문제가 발생했을 때 정확히 어떤 부분을 실행하다가 문제가 생겼는지 명확히 파악이 가능한 장점이 있음

#### '빌드'작업의 단계들
- 저장소를 체크아웃하면서 시작
- 깃허브 액션을 실행하는 서버 컴퓨터의 로컬환경에서는 존재하지 않는 상태
- 애저 깃허브 액션을 이용해 인증을 수행
- 인증이 성공적으로 완료되면 보델 레지스트리에 등록된 모델의 이름과 해당 모델이 포함돼 있는 애저 머신러닝 스튜디오의 워크스페이스 이름 및 리소스 그룹의 이름을 이용해 앞서 업로드 했던 ONNX 모델을 다운받음
- 깃허브 액션이 여기까지 성공적이라면 서버 컴퓨터 프로젝트 디렉토리의 webapp 폴더에 RoBERTa-Sequence 모델이 위치해 있는 상태일 것임
- 이들을 모두 패키징한 컨테이너 이미지를 빌드하는 단계가 실행될 것

이 YAML 파일의 빌드 작업을 구성하는 단계 중 애저 인증 단계에서는 AZURE_CREDENTIALS라는 이름의 변수를 사용한다.
변수를 둘러싼 독특한 문법은 깃허브 저장소의 시크릿에 저장된 값을 불러오기 위해 필요함

애저 인증을 위해 시크릿에 저장되어 있어야 하는 값은 애저 SP 정보이다.
SP가 낯선 독자들은 애저 클라우드 MLOps를 다룬 8장에서 인증관련 내용을 봐라
다양한 리소스에 접근할 수 있도록 SP를 발급받고 워크플로에서 해당 값을 읽어갈 수 있도록 깃허브에 등록
깃허브 저장소에 들어가 [Settings]버튼을 누르고 'Secret'탭을 열면 [New repository secret]버튼을 확인할 수 있다

시크릿 이름을 YAML에서 사용되는 변수명 AZURE_CREDENTIALS과 동일한 값으로 설정하고 발급받은 SP를 복사해서 붙여넣음  