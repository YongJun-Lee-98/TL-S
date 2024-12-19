
## Django의 기본 MTV(Model-Template-View) 디자인 패턴
모델-템플릿-뷰는 디자인 패턴의 일종
역할에 따라 코드를 분리하는 가이드로서 사용

### Model
Model은 Django와 데이터베이스를 연결시켜주는 코드
데이터의 형태를 나타냄 일반적으로 각각의 모델은 데이터베이스 테이블과 매핑됨

모델은 다음 속성들을 가짐
- 파이썬의 클래스를 사용하며, 모든 Model 클래스는 django.db.models.Model 클래스를 상속 받는다.
파일명의 기본값 = models.py
class DajngoModel
```
class DjangoModel(models.Model):
    name = models.CharField("이름")
```

### Template
Template은 웹 브라우저로 돌려줄 코드이며, 사용자에게 제공될 결과물의 형태를 나타냄
HTML을 사용해서 나타내고 Django에서는 templates 디렉터리 내에 HTML 파일을 사용함
templates/smaple.html
```
<!DOCTYPE html>
<html lang="ko">
    <body>
        <h1>DjangoTemplate</h1>
    </body>
</html>
```

### View
View는 사용자의 요청을 받아 처리하는 웹 사이트 로직을 가지는 코드
파이썬의 함수(Function)을 활용한다.
기본값은 views.py
```
def django_view(request):
    return HttpResponse("Django View")
```
def로 main 함수를 정의하였고 return으로 돌려줄 문자열을 정의한다.
문자열을 직접 리턴하는 것이 아니라 HttpResponse 객체를 리턴해 주어야 한다.
Django가 돌려준 값을 브라우저가 읽을 수 있도록 적절하게 처리해 주는 것임

### URLconf 구현
URLconf를 작성하기  
views.py는 직접 만들어야 했지만 url.py는 django-admin start project \[] \[] 를 사용했을 때 같이 만들어진다.
urlpatterns에 
`path("주소", 함수)`   
를 추가하여 형식 url 주소를 관리한다.  

## Template 사용하기
Template은 Django가 브라우저에 보낼 문서의 형태를 미리 만들어 놓은 것

브라우저에 돌려보낼 문서의 형태를 미리 만들어 놓는 것
브라우저에 돌려줄 내용을 View 함수에 기록할 수도 있지만, 웹 브라우저에 보내는 문서 형식인 HTML은 많은 내용을 가지고 있음

이 내용을 전부 View 함수 내부에서 다루면 코드를 읽기 힘들어진다.
따라서 Django에서는 요청을 처리하는 함수인 View와 처리해서 보내줄 내용을 미리 담아놓은 Template을 분리해서 사용한다.

# Django에 데이터 저장하기
## Model 구성하기

### Model과 데이터베이스의 관계
URLconf를 메뉴판, View를 해당 메뉴를 처리하는 직원으로 비유했음
Model은 메뉴를 만들기 위한 재료들을 저장하는 창고
블로그에 작성해 놓은 글이 없으면 늘 같은 화면 밖에 볼 수 없듯
우리가 만든 main과 view는 늘 같은 답변밖에 주지 못함
계속해서 업데이트되는 햄버거 목록과 같은 것을 보여주고 싶다면 정보를 저장할 수 있는 엑셀 시트가 필요함
저장할 데이터의 형태는 Model의 구성을 정할 수 있음

### 정보를 저장할 app 추가
Djangoㅇ서는 큰 프로젝트를 application이라는 단위로 나눔
큰 단위를 시작할 때
`python manage.py startapp [이름]`
이후 이 이름을 settings.py의 INSTALLED_APPS리스트에 추가함

-# database는 추후에  
mysql / mariadb / sqlite3 / postgresql 과 연결하는 방법을 찾아서  
app으로 추가

# Django로 데이터 보여주기
## 전체 목록 가져오기
### Django 코드를 포함한 파이썬 인터프리터 실행
Interpreter는 소스코드를 바로 실행하는 프로그램 또는 환경을 말한다.  
Django 프로젝트의 코드를 포함한 인터프리터를 사용하려면 manage.py를 사용해야 한다.  
manage.py shell로 실행된 인터프리터에서는 Django 프로젝트의 코드를 바로 사용할 수 있다.

## models
models를 class로 정의하고  
'python manage.py makemigrations [app 이름]'   
'python manage.py migrate [app 이름]'

테이블이 'app이름_class명' 으로 생성되는 것을 확인할 수 있음  
class의 내부에 정의된 models 변수들은 열(Column)값으로 생성해 줌  

## Django admin 사용
### The Django admin site

Blog 클래스를 다룰 수 있는 관리자 페이지 만들기
관리자 기능은 각 app의 admin.py에 정의함
```
    # 아래 내용을 사용하면 title명을 admin 페이지에서 표시할 수 있음
    def __str__(self):
        return self.title
```

## 데이터베이스 다루기
### 전체 햄버거 목록 가져오기
```
python manage.py shell
```
명령어를 사용해서 실행된 인터프리터에서 Django 프로젝트의 코드를 바로 사용할 수 있다.  
> ORM
> ORM(Object-relational mapping, 객체 관계 타이핑)은 데이터베이스의 데이터를 연결해주는 기능이다. 
> blog/models의 Page를 import 한 뒤
> Page.objects.all()을 입력하면 QuerySet이라는 객체가 출력되면 해당 객체는 내부 속성으로 Burger들을 가지고 있음을 볼 수 있음

[Django orm Doc](https://docs.djangoproject.com/ko/5.1/topics/db/queries/)

### 특정 조건을 만족하는 한개 정보를 가져오기 (get)

```
Page.objects.get(title='제목')
```
get 함수로 조건에 부합하는 객체 하나를 가져온다.

### 특정 조건을 만족하는 정보 가져오기 (filter)
all은 모든 객체를, get은 조건을 만족하는 객체 하나만을 가져온다.  
조건을 만족하는 여러 객체를 가져올 때는 filter 메서드를 사용한다.  
```
Page.object.filter(title__endswith="제목 조건 구문")
```

해당 결과물의 type은 객체를 담는 리스트 역할을 하는 QuerySet 객체를 반환한다.

## View에서 데이터 다루기
### 데이터를 가져오는 과정
요청 전달 -> URLconf -> View -> def View (<-Model) -> Template -> View(response) -> 응답 전달

### View 함수에서 데이터 가져오기
```python
from blog.models import Post

def post_list(request):
    posts = post.objects.all()
    print("전체 포스트 리스트", posts)
    return render(request, "post_list.html")
```
- 가져온 데이터를 Template로 전달해주기
View 함수는 Model 클래스를 사용해 데이터베이스로부터 원하는 데이터를 가져오고, 그 데이터를 템플릿으로 전달해주는 역할을 한다.
- Template은 View 함수가 전달해준 데이터를 사용해서 동적으로 HTML을 구성한다.

동적으로 HTML을 구성한다는 것은, 사용자의 요청이나 데이터베이스의 데이터에 따라 다른 HTML을 그때그때 만들어서 보여준 다는 의미이다.  
포털 사이트의 뉴스나 인스타그램의 피드를 생각해보면 좋음 같은 웹사이트이며 보여주는 내용의 형태는 같지만 뉴스는 최신 항목이 올라오면 다른 내용이 나오며, 인스타그램의 피드는 로그인한 사용자마다 다른 내용들을 보여준다.

Template로 가져온 데이터를 전달해줄 때는 파이썬의 dictionary 객체를 사용해 전달한다. 관용적으로 Template에 전달하는 사전 객체의 변수명은 context를 사용한다.

## Template에서 데이터 다루기
### Template 문법
HTML의 형태를 가진 Template은 별도의 문법을 가진다.  
여기서 사용할 Template 요소에 대해 알아본다.  

#### 변수
Template에서 변수를 출력하고자 할 때는 \{\{ 와 \}\} 사이에 변수명을 입력한다.  
변수명이 object라면 \{\{ object \}\} 라고 입력한다.  

#### 태그
태그는 \{% 로 시작하고 %\}로 끝난다.

#### for
for 태그는 반복 가능한(Iterable) 객체를 순회하는 데 사용한다.  
objects=[1, 2, 3, 4, 5]와 같은 리스트 객체가 있다고 가정하고, 파이썬과 Template에서의 사용법과 결과는 아래와 같음
```python
for item in objects:
    print(item)
```

```
{% for item in objects %}
    <div>{{ item }}</div>
{% endfor %}
```
[이외의 태그](https://docs.django.ac/templates/tags)들의 설명  

### Template에서 전달된 데이터 출력하기
#### 변수를 그대로 출력
앞에서 dict key로 objects.all() 열과를 QuerySet 값을 가진 사전 객체를 Template으로 전달했음
사전의 키(key)는 Template에서 변수(variable)가 된다.  
pages를 출력해보자

# Django에 데이터 전송하기
## 웹에서 데이터를 전송하는 방법
#### GET과 POST
- GET 방식으로 데이터 전송하기
GET 방식은 우리가 서버에 보낼 데이터가 공개되어도 상관없는 경우에 사용한다.

> 사이트의 구조  
> search.naver.com/search.naver. 네이버에서 검색 결과를 보여주는 서버 주소를 나타냄  
> ? : 여기서부터가 서버의 주소가 아니라 서버에 보낼 데이터를 나타냄을 알리는 구분 기호 서버의 주소 뒤에 ? 가 붙으면 다음의 내용은 서버에 보낼 데이터를 의미함  
> query=파이썬 : 데이터는 key=value 형태로 서버에 구분되어 보내면. 이 구문을 사용해 query라는 키에 파이썬이라는 값을 담아서 서버에 전달한다.  

## GET 방식을 사용한 포스트 검색
Django admin을 사용해서 데이터를 추가하고 보여주는 페이지를 만들었음  
등록한 버거가 많아진다면 우리가 원하는 정보를 찾기 어려움  
네이버에서 특정 단어를 검색하듯이 GET 방식을 사용해서 버거를 검색하는 기능을 만들기  

### URLconf - View - Template 연결
Django를 사용해 새로운 페이지를 만든다면  
URLconf와 View, Template을 서로 연결  
검색을 위한 view 작성  

### Template에서 데이터 보여주기
objects.filter를 통해 db의 값을 보여주는 것

## form을 사용한 GET 요청
?keyword=<검색할 키워드>를 입력해,  
View에 keyword라는 항목으로 값을 전달하고 목록을 검색하였음  
HTML의 form을 사용해서 좀 더 편하게 검색 동작을 수행하도록 코드를 개선하기

> object.none()은 아무 객체도 포함하지 않은 빈 QuerySet을 리턴한다.

### Template에 검색창 만들기
#### Input과 button 추가
검색어가 없을 때의 버그를 수정했고 이제 검색하는 HTML 페이지에 검색창과 버튼을 추가해보기  
HTML에서 사용자 입력을 받는 요소는 \<input>, \<button> 태그를 사용함  

# 글과 댓글 모델 구현

## 1:N 연결의 이해
학교와 학생, 음반과 노래와 같이 하나의 부모 요소에 여러 자식 요소가 연결된 연결을 1:N(일대 다 또는 다대일) 관계라 부른다. 블로그 댓글은 1개든 10개든 수와 상관 없이 반드시 하나의 포스트와 연결되므로, 글과 댓글은 1:N으로 연결된다고 한다.  

- 하나의 테이블에서 댓글 3개를 나타내는 경우  

|제목|내용|
|--|--|
|Django의 역사| 정말 유용한 내용이에요|
|Django의 역사(중복)| 감사합니다.|
|Django의 역사(중복)| 다음 글은 언제인가요? |

테이블의 구성에서 Django의 역사 라는제목 데이터가 댓글 개수만큼 중복되어 저장된다. 글 제목을 수정하려면 반드시 3개의 데이터를 동시에 수정해야 한다.  
1:N 테이블은 비효율적인 구조를 막기 위해 각각의 테이블에 나누어 저장하여 데이터의 중복을 막음  

- 글(Post) 테이블  

| ID | 제목 |
|--|--|
| 1 | Django의 역사 |
| 2 | Django 튜토리얼 |
| 3 | Django로 만드는 블로그 |

- 댓글(Comment) 테이블

| ID | 제목 |
|--|--|
| 1 | 정말 유용한 내용이에요 |
| 2 | 감사합니다. |
| 3 | 블로그 내용 좋아요 |

- 글(Post)와 연결된 댓글(Comment) 테이블

| ID | PostID | 제목 |
|--|--|--|
| 1 | 1 |정말 유용한 내용이에요 |
| 2 | 1 |감사합니다. |
| 3 | 3 |블로그 내용 좋아요 |  


위의 세 가지의 테이블을 구성하면 처음 두개의 댓글(ID 1, 2)는 글 1번 과 연결되고 3번째 댓글은 3번글과 연결된다.

이렇게 각 테이블을 구성하고, 1:N에서 N부분의 테이블에 자신이 어떤 부모 요소에 연결되어 있는지 나타내는 것을 1:N관계로 테이블을 구성했다고 말한다.  
Django는 이러한 Relational Database(RDB)를 사용한다.  

### Post admin 구성
```python
from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
```

models.py의 Comment에 Post와 연결된 ForeignKey 필드는 작성해둔 Post를 선택할 수 있는 Select box의 형태로 나타난다.  
하나의 Post에만 2개의 Comment를 추가해보기  

# 글과 댓글 보여주기  
## 글(Post) 목록 보여주기
1. View 함수의 이름은 post_list를 사용한다.
2. URL은 /posts/를 사용한다.
3. 템플릿은 post_list.html을 사용한다.
4. View, URL, 템플릿의 연결을 확인한다.
5. View에서 ORM을 사용해 모든 글 목록을 가져와 템플릿에 전달한다.
6. 템플릿은 View에서 전달받은 내용을 표시한다.

### View 작성
```python
# views.py
from django.shortcuts import render

def post_list(request):
    return render(request, "post_list.html")
```

### URLconf 작성
```python
from blog.views import post_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("posts/", post_list),
]
```

### 템플릿 작성
```html
<!doctype html>
<html lang="ko">
    <body>
        <h1>Post List</h1>
    </body>
</html>
```

### View에서 ORM을 사용해 모든 글 목록을 가져와 템플릿에 전달
```python
from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts = Post.objects.all()
    # 템플릿에 전달할 dict
    context = {
        "posts": posts,
    }
    # 3번째 인수로 템플릿에 데이터를 전달
    return render(request, "posts.html", context)
```
### templates은 View에서 전달 받은 내용을 표시
``` html
<html>
    <body>
        <h1>Post List</h1>
        <!-- 글 목록을 ul(Unordered List)요소에 표시 -->
        <ul>
            <!-- for-in 태그로 순회하며 각각의 글은 li(List Item) 요소로 표시 -->
        {% for post in posts %}
             <li>
                <!-- 각각의 글의 제목과 내용을 나누어 표시 -->
                 <h2>{{ post.title }}</h2>
                 <p>{{ post.cotent }}</p>
            </li>
        {% endfor %}
        </ul>
    </body>
</html>
```

## 댓글(Comment) 목록 보여주기
### Django ORM을 사용해 1:N 객체 접근하기
댓글을 보여주는 것은 글을 보여주는 것과는 조금 다름  
댓글 목록을 보여주기 전에, Django ORM을 사용해서 1:N 관계인 객체를 어떻게 가져올 수 있는지 알아보기  
```python
class Comment(models.Model): # N방향의 모델 (Comment)
    post = models.ForeignKey(Post) # 1방향의 모델 (Post)
```
Comment 모델은 post 속성으로 자신과 연결된 Post에 직접 액세스할 수 있음. 인터프리터에서 기능을 실습해보기  

Comment는 자신의 post 속성으로 연결된 Post 객체에 접근할 수 있다.  
이를 정방향 관계라 함. 반대로 1:N에서 1방면의 객체에서 N방면의 객체로 접근하는 것을 겨방향 관계라 한다.  
역방향 접근을 위한 속성은 \{N방향 모델명의 소문자화\}_set이라는 이름으로 Django ORM이 자동으로 생성해준다.  
즉, Post 객체가 자신에게 연결된 Comment들을 가져오기 위해서는 {Comment모델의 소문자화}_set인 comment_set이라는 이름으로 접근한다.  
```bash
>>> from blog.models import Post, Comment
>>> post = Post.objects.first()
>>> post.comment_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x10688d100>
```
comment_set은 RelatedManager 객체로, N방향으ㅢ 객체로 접근할 수 있도록 도와주는 역할을 한다. Comment의 입장에서 연결된 Post는 1개뿐이기 때문에 곧바로 접근이 가능하지만 Post입장에서 Comment와 연결된 Comment들이 여럿이므로 Manager 객체를 통해 가져온다.  

Post.objects.all()을 호출한 때와 유사하게 여러 Comment를 동시에 돌려주고자 QerySet 객체가 리턴되는 것을 볼 수 있었음  
for문으로 순회하며 연결된 Comment의 내용도 확인해보기  

### 템플릿에서 댓글 객체 표시하기
```html
<ul>
    {% for post in posts %}
</ul>
```
---
# 유저가 업로드하는 정적 파일
## 정적파일의 분류
Django에서 정적파일은 두 가지로 나뉜다.
- 소스코드에 포함되는 정적파일
- 유저가 업로드하는 정적파일

정적파일은 이미지/동영상/CSS 파일과 같은 변하지 않는 데이터를 뜻한다. 이전에 정적파일ㅇ르 넣어놓기로 했던 디렉터리(static)을 두는 곳을 말하며 여기에 있는 파일들은 만드는 프로젝트의 일부분으로 취급됨

반면 유저가 업로드하는 정적파일은 프로젝트에 포함되지 않음
이 분류의 정적파일은 블로그라는 전체 프로젝트와는 별개로, 블로그를 사용하는 사용자들이 업로드하는 그렝 포함된 이미지와 같은 데이터를 의미한다. 
소스코드에 포함되는 정적파일은 settings.py STATICFILES_DIR에 저장될 경로를 지정하고 
템플릿에서 {\% static \%} 태그를 사용해서 불러오는 방식을 사용한다. 
소스코드에 포함되는 파일의 경로만 지정하면 되므로 비교적 설정이 간단하다. 

# 유저가 업로드하는 정적 파일
## 정적 파일 분류
Django에서는 정적 파일은 두 가지로 나뉜다.
- 소스코드에 포함되는 정적 파일
- 유저가 업로드하는 정적 파일

정적 파일은 이미지/동영상/CSS 파일과 같은 변하지 않는 데이터를 뜻함  
이전에 정적 파일을 넣어놓기로 했던 디렉터리 static는 소스코드에 포함되는 정적파일을 두는 곳을 말하며 여기에 있는 파일들은 만드는 프로젝트의 일부분으로 취급된다.  

반면에 유저가 업로드하는 정적파일은 프로젝트에 포함되지 않는다. 이 분류의 정적파일은 블로그라는 전체 프로젝트와는 별개로, 블로그를 사용하는 사용자들이 업로드하는 글에 포함된 이미지와 같은 데이터를 의미함

소스코드에 포함되는 정적파일은 settings.py의 STATICFILES_DIRS에 저장될 경로를 지정하고, 템플릿에서 {% static %} 태그를 사용해서 불러오는 방식을 사용한다.  
소스코드에 포함되는 파일의 경로만 지정하면 되므로 비교적 설정이 간단하다. 한편 유저가 업로드하는 정적파일은 조금 더 설정이 복잡하다.

Django에서는 이 둘을 조금 다른 이름으로 부른다.  
소스코드에 포함되는 정적파일은 의미 그대로 Staticfile, 유저가 업로드하는 정적파일은 User-uploaded static file이라 부른다.  

## 유저가 업로드하는 정적파일 설정
settings.py에서 소스코드에 포함되는 정적파일의 설정은 대부분 STATIC_으로 시작하고, 유저가 업로드하는 정적파일과 관련된 설정은 대부분 MEDIA_로 시작한다.

- MEDIA_URL
  유저가 업로드한 파일에 접근할 수 있도록 브라우저에 제공하는 경로 접두어(Prefix)를 나타낸다. 기본 설정이 되어 있어 이전에는 생략했지만, 소스코드에 포함되는 정적파일은 STATIC_URL이라는 설정값을 사용하며 기본값은 \/static\/ 이다. 한편, 유저가 업로드한 파일의 경로 접두어는 \/media\/를 사용한다.  
- MEDIA_ROOT
  실제로 유저가 업로드한 파일이 저장될 경로를 나타낸다.
  유저가 업로드한 정적 파일은 프로젝트 디렉터리 하위의 media 디렉터리를 사용한다.  
  settings.py의 BASE_DIR은 프로젝트 디렉터리를 나타내며,
  한 단계 하위 디렉터리는 BASE_DIR / "디렉터리 명" 으로 지정한다.
```python
# MEDIA_ 관련 설정 추가 
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
```
## 정적파일을 저장하는 필드 추가
각각의 글에 썸네일 이미지를 저장할 필드를 추가한다.  
이미지를 저장할 때는 Django에 내장되어 있는 ImageField를 사용한다.  

```python
class Post(models.Model):
	title = models.CharField("포스트 제목", max_length=100)
	content = models.TextField("포스트 내용")
	thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)
```

## MEDIA_URL과 업로드 파일 연결
```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog.views import post_list
from config.views import index

urlpatterns = [
	path("admin/", admin.site.urls),
	path("", index),
	path("posts/", post_list),
]

urlpatterns += static(
	# URL의 접두어가 MEDIA_URL일 때는 정적파일을 돌려준다.
	prefix=settings.MEDIA_URL,
	# 돌려줄 디렉터리는 MEDIA_ROOT를 기준으로 한다.
	document_root= settings.MEDIA_ROOT,
)
```
import 시 모듈의 이름에 주의하기
settings는 django.conf에서 가져오며, static은 django.conf.urls.static에서 가져온다.

static 함수에 전달하는 prefix와 document_root 인수는 각각 어떤 URL 접두어가 올 경우와 어디에서 파일을 찾아 돌려줄 것인가를 뜻한다.
MEDIA_URL로 시작하는 URL 요청이 오면, MEDIA_ROOT에서 파일을 찾아 돌려주기 위해 위와 같이 설정한다.  
개발서버 재시작후 Django admin에서 이미지를 클릭해보기  

> Note MEDIA_ROOT와 MEDIA_URL
> 위 코드를 사용해 MEDIA_URL 경로와 MEDIA_ROOT의 파일을 연결시키면, 외부에서 정적파일의 URL을 요청했을 때 해당 요청을 Django가 처리하여 파일을 돌려주게 된다. 이 설정이 미리되어있지 않은 이유는 효율성 때문이다. 외부에서의 요청에 대해 정적파일을 돌려주는 작업은 Nginx나 Apache와 같은 웹 서버가 담당하는 것이 더 효율적임 정적파일 처리를 웹 서버 대신 Django가 담당하는 것은 개발 단계의 편의성을 위해서만 사용해야 한다.

## 템플릿에 업로드된 파일 보여주기
admin.py의 내용중
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]
```


### ImageField의 속성들
Post의 thumbnail 속성은 ImageField이다.
Django는 ImageField에 업로드한 이미지를 사용할 수 있는 기능을 제공한다.
이를 먼저 알아보기
> python manage.py shell
> 
> from blog.models import Post
> post = Post.objects.first()
> 
> # thumbnial 속성에 접근하면 ImageField의 파일 정보를 확인할 수 있다.
> post.thumbnail
> 
> # ImageField의 "name"속성은 MEDIA_ROOT 디렉터리를 기준으로 저장된 이미지의 경로를 나타낸다.
> post.thumbnail.name
> 
> # ImageFiled의 "path" 속성은 시스템 전체를 기준으로 이미지의 전체 경로를 나타낸다.
> post.thumbnail.path
> 
> # ImageField의 "size" 속성은 저장된 파일의 bytes 수를 나타낸다.
> post.thumbnail.size
> 
> # ImageField의 "url" 속성은 MEDIA_URL을 기준으로 이미지의 접근 URL을 생성한다.
> post.thumbnail.url

# 글 상세 페이지
## 상세 페이지 기본 구조
글의 전체 목록에는 모든 내용을 표시할 수 없다. 각각의 글이 가진 모든 내용을 표시할 상세 화면을 구성해보자.
새 기능을 추가할 때는 늘 빈 View, URL, Template을 만들고 연결을 확인한다.  
- View: blog/views.py의 post_detail
- URL: ID가 1번인 글을 \/post/1/, 2번인 글은 \/post/2\/ 를 사용
- Template: templates/post_detail.html을 사용

View와 Template은 지금까지 만들어왔던 예제와 크게 다르지 않다. 하지만 전체 글 목록을 볼 수 있는 \/post/ URL(View는 post_list)과는 달리, 글의 상세 페이지는 자신(Post)의 ID 값에 따라 서로 다른 동적인 URL을 가져야한다.  

> Model의 id필드
> 
> Model 클래스로 생성된 테이블에는 id 필드가 자동으로 생성되며, 해당 테이블에 새로운 데이터(row)가 추가될 때마다 기존에 존재하던 가장 큰 id값보다 1증가된 값이 할당된다. Django의 Model에서 id필드는 이 기능을 지원하는 AutoField로 되어 있음

```python
urlpatterns = [
	...
	path("posts/<int:post_id>/", post_detail),
]
```
url.py의 패턴에 주소를 등록하고
이 안에서 함수의 내부에 매개변수를 넣을 수 있음  

## ID에 해당하는 글을 보여주기
urls.py <\int:post_id> 영역을 사용해 URL을 통해 동적으로 값을 전달할 수 있게 되어있다.  
이제 URL로 전달받은 ID에 해당하는 Post를 실제로 보여주도록 하자.  

### 전달받은 인수를 Template에 보여주기
지금은 어떤 숫자를 입력하든, 내용의 변화없이 Post Detail이라는 제목이 보이는 페이지가 나타난다.  
URL을 통해 인수를 받았다는 사실을 사용자가 보는 화면에 출력해보자.  
View 함수에서 Template에 dict를 사용해서 값을 전달한다.  

스타일은 잘 적요되지만 본문 내용의 줄바꿈이 적용되지 않음
이 글은 admin에서 보낸 글에서는 줄바꿈이 적용되었음을 보여주지만
HTML에서는 줄바꿈 내용이 적용되지 않는다. 
Django의 기능 사용하여 줄바꿈을 적용은 |linebreaksbr을 추가하기

> |linebreaksbr 필터
> linebreaksbr은 Django Template에서 필터의 한 종류이다. 필터는 좌측의 변수 문자열의 줄바꿈을 HTML의 \<br> 태그로 치환해 준다.
> \<br>은 HTML의 줄바꿈 태그이다.  


## 댓글 기능
### 댓글 목록 표시
제목 썸네일 본문을 모두 출력했음
이제 하단에 댓글 목록을 보여주어야함
댓글 목록은 이미 구현해보았으니 구현된 코드만 살펴보기

## 사용자의 입력을 받는 Template
### HTML 형태 구현
HTML 에서 사용자의 입력을 받는 요소는 다음과 같음
- 입력에 대한 제목: \<label>
- 한 줄 짜리 텍스트 입력: \<input type="text">
- 여러 줄의 텍스트 입력: \<textarea>
- 버튼: \<button>

> post_add.html
```html
<body>
	<div>
		<h1>Post Add</h1>
	<form method="GET">
		<div>
			<label>제목</label>
			<input type="text">
		</div>
		<div>
			<label>내용</label>
			<textarea></textarea>
		<div>
		<button>작성</button>
		</form>
	</div>
<body>
		
```

```html
...

<body>
	<div>
		<h1>Post Add</h1>
	<form method="GET">
		<div>
			<label>제목</label>
			<input name="title" type="text">
		</div>
		<div>
			<label>내용</label>
			<textarea name="content"></textarea>
		<div>
		<button type="submit">작성</button>
		</form>
	</div>
<body>

...
```
메서드가 POST가 아닐때
HTTP의 요청 메서드는 GET, POST뿐 아니라 HEAD, PUT, PATCH, OPTIONS, DELETE 등 여러 종류가 있지만 HTML의 gorm태그에서는 GET과 POST 방식만 사용이 가능하다. 따라서 HTML form으로 전달받은 request의 method가 POST일 때와 POST가 아닐 때로 구분하면, POST가 아닐때는 GET 방식임을 나타낸다.  

### POST데이터를 사용한 DB row 생성
#### objects.create 메서드
요청이 POST 메서드일 때 전달된 데이터를 가져오는데 성공했으니
가져온 데이터를 사용해 DB에 새 row를 생성해보자
ORM을 사용해서 DB에 데이터를 생성할 때 create메서드를 사용한다.
create 메서드의 리턴값은 생성된 객체이며, 이를 변수에서 바로 할당해 사용이 가능함
```python
created_instance = ModelClass.objects.create(필드명=필드값)
```



## 댓글 작성
### Comment 객체
Comment객체의 구성
```python
post = models.ForeignKey(Post, on_delete=models.CASCADE)
```
Comment를 생성하려면 연결될 Post를 지정해주어야함  
인터프리터에서 아래와 같이 Post 변수에 할당 후 진행해보기  

```python
if request.method == "POST":
	# textarea의 "name" 속성값 ("comment")을 가져온다.
	comment_content = request.POST["comment"]
	
```

## 글 작성시 이미지 업로드
파일을 전송해야할 경우 form에는 enctype="multipart/form-data" 속성을 추가해야한다.  
enctype 속성은 데이터를 서버로 전송할 때 어떤 인코딩 유형을 사용할 것인지를 나타낸다.  

# CustomUser
users 앱 생성 및 등록
python manage.py startup users
/models.py
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
     pass
```
AbstractUser는 Django가 CustomUser 모델을 만들기 위해 제공하는 기본 유저 형태를 가진 모델 클래스이다.  
이 클래스는 Django의 기본 User 모델이 가진 필드를 똑같이 가지고 있으며, AbstractUser를 상속받으면 자동적으로 다음 필드들이 모델에 추가된다.  
- username(ID)
- passwoard
- first_name(이름)
- last_name(성)
- email
- is_staff(관리자 여부)
- is_active(활성화 여부)
- date_joined(가입 일시)
- last_login(마지막 로그인 일시)

관리자 페이지나 로그인 페이지에서 사용하는 아이디/비밀번호 중, 아이디에 해당하는 필드는 username 필드이다. (id 필드는 모델 클래스에서 자동 생성되며, 테이블의 기본키를 나타내는 데 쓰인다.)
실제로 사용하지 않는 정보들도 있을 수 있지만 Django의 동작은 User 모델이 최소한 이 필드들을 가지고 있을 것으로 예측하고 만들어져 있는 경우가 많다.  

> CustomerUser를 위한 모델
> Django에서 CustomUser를 지원하는 모델로 AbstractUser와 이보다 적은 정보를 가지고 있는 AbstractBaseUser, 두 가지 정보를 제공한다.
> password
> last_login
> AbstractBaseUser 모델을 사용해 CustomUser를 구현하면, 이외에 사용자를 나타내기 위한 필드들은 개발자가 별도로 구성해야 한다. AbstractBaseUser를 사용해 사용자 모델의 기본 필드들을 커스터마이징하는 것은 어느정도 Django의 사용에 익숙해진 후에 하길 바람


CustomUser 모델에 추가한 필드를 관리자 페이지에 표시하도록 함  
fields키의 캆 튜플이 하나의 요소를 가지는 경우에는 마지막에 반드시 쉼표가 붙어야한다.  
```python
# 단일 요소를 가지는 튜플 예시
{
	"fields": ("profile_image",)
}
```

## 로그인/피드 페이지 기본 구조
인스타그램에 접속했을 때, 로그인 중이라면 바로 피드 페이지가 나타나지만 로그인되지 않았거나 처음 접속한 경우에는 로그인 페이지로 이동한다.  

> 두 조건에 맞도록 View에서 동작을 제어한다.

1. 이미 사용자가 브라우저에서 로그인을 했다면
   -> 피드(새 글 목록) 페이지를 보여줌
2. 사용자가 로그인을 한 적이 없다면 (또는 로그아웃을 했다면)
   -> 로그인 페이지를 보여줌

