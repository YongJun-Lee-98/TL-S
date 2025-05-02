Django REST Framework는 Django의 
기본 디자인인 MTV(Model - Template -View)를 따르는 것이 아니라
Model - Serializer - View 구조로 나누어 관리됨  

## 1. 이점
> 명확한 관심사의 분리  

- Model
	- 데이터베이스 구조 정의 및 관리
	- 데이터 접근 및 비즈니스 로직 관리
- Serializer
	- 데이터 직렬화/역직렬화 관리
	- 데이터 유효성 검사 및 형태 지정
- View (APIView/ViewSet)
	- 요청 처리와 응답 전달 관리
	- 비즈니스 로직과 권한 관리

DRF의 사용으로 계층의 역할이 더욱 명확해져 유지보수성과 확장성이 크게 향상됩니다.

## Serializer 장점
### 유효성 검사 (Validation)
- 데이터를 받는 즉시 유효성 검사 진행 가능
- 복잡한 유효성 로직을 Serializer에서 간단히 처리 가능

Serializer에서 복잡한 유효성 로직을 처리하는 예시 표현
```python
from django.contrib.auth.models import User
from rest_framework import serializers
import re

class UserRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	password2 = serializers.CharField(write_only=True)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'password2' )
	# 비밀번호 길이, 특수문자 체크 등 복잡한 검증
	def validate_password(self, value):
		if len(value) < 8:
			raise serializers.ValidationError("비밀번호는 8자 이상이어야 합니다.")
		if not re.findall('[!@#$%^&*]', value):
			raise serializers.ValidationError("특수문자를 하나 이상 포함해야 합니다.")
		return value
	# 이메일 중복 검증
	def validate_email(self, value):
		if User.objects.filter(email=value).exists():
			raise serializers.ValidationError("이미 사용중인 이메일입니다.")
		return value
	# 두 비밀번호 일치 여부
	def validate(self, data):
		if data['password'] != data['password2']:
			raise serializers.ValidationError("두 비밀번호가 일치하지 않습니다.")
		return data
	
	def create(self, vlidated_data):
		vlaidated_data.pop('password2')
		user = User.objects.create_user(**validated_data)
		return user
```
### 데이터의 형태를 쉽게 관리
- 원하는 필드를 쉽게 추가하거나 제외 가능
- 모델 필드와는 다른 형태의 데이터 반환 가능(연관 모델 데이터 포함 등)
### 명확한 API 문서화
- API에서 반환되는 데이터 구조를 명확히 정의할 수 있어 자동 문서화가 쉬움
- OpenAPI(Swagger), Redoc 등과 연계하기 용이함 

---
## RESTful API 개발에 최적화된 구조
- DRF는 HTTP Method(GET, POST, PUT, DELETE)에 맞게 데이터를 처리하도록 최적화되어 있음
- 표준화된 REST 구조를 손쉽게 구현할 수 있어 API 유지 관리가 쉬워짐
- 인증, 권한관리, Pagination등을 직관적이고 효율적으로 설정이 가능함 

```python
REST_FRAMEWOR = {
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	],
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.IsAuthenticated', # 기본적으로 인증된 사용자만 허용
	]
}
```

> 관리 예시

```python
# views.py
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

class UserProfileView(APIView):
	permission_classes = [IsAuthenticated] # 인증된 사용자만 접근 가능
	
	def get(self, request):
		return Response({"username": request.user.username})

class AdminOnlyView(APIView):
	permission_classes = [IsAdminUser] # 관리자 접근 가능
	
	def get(self, request):
		retrun Response({"admin_data": "관리자 전용 정보입니다."})
```

> Pagination 설정

```python
REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 10, # 기본 페이지 개수 설정
}
```

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer

class CustomPagination(PageNumberPagination):
	page_size = 5
	page_query_param = 'page'

class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	pagination_class = CustomPagination
```

---
### 유지보수 및 확장성 향상
- Serializer와 View가 명확히 분리되어 있으므로, 요구사항이 변경될 때 코드 수정 범위가 최소화됨
- 기능 추가 및 변경 시 특정 부분만 쉽게 수정할 수 있어 개발 생산성 증가
- 테스트 코드 작성이 쉬워짐 (TEST 코드를 작성하는 부분은 아직 서툴어서 이 부분은 좀 더 메모해두고 작성해볼 수 있도록 해야겠음)
