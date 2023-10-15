# :cat: 장고 프로젝트 준비

#### 1. 프로젝트 생성 전
1. 가상환경(venv) 생성
    - python -m venv venv
2. 가상환경 활성화
    - source venv/Scripts/activate
        - 비활성화: deactivate
        - 패키지 목록 확인: pip list
3. 장고 설치
    - pip install Django
4. 의존성 파일 생성
    - pip freeze > requirements.txt
        - .gitignore 생성 (첫 add 전!!)

#### 2. 프로젝트와 앱
1. Django 프로젝트 생성
    - django-admin startproject firstpjt .
        - 서버 실행: python manage.py runserver
2. 앱 생성 후 등록
    - python manage.py startapp articles
    - 프로젝트 파일 - settings.py - INSTALLED_APPS 리스트에 앱 추가

#### 3. 요청과 응답
- URLs -> View -> Template
    - urls: 웹주소로 요청이 왔을 때 views 모듈에서 선택한 함수 호출
    - views: 함수 생성 -> 모든 view함수의 첫번째 인자는 request !! -> templates 내 호출할 홈페이지 지정
    - templates: 앱 폴더 -> templates 폴더 -> articles 폴더 -> 템플릿 파일 생성

---

#### ※ model
- class 모델명(models.Model):
    - 필드 작성: 변수명 = models.***Field(options)
    - 출력 메서드: \__str__
- python manage.py makemigrations
- python manage.py migrate
- [참고] (https://docs.djangoproject.com/en/4.2/ref/models/fields/)

#### ※ admin
- python manage.py createsuperuser
    - 아이디, 메일(option), 비번 생성
- admin 사이트에 model 필드 등록 -> admin.py
    - admin.site.register(model명, ArticleAdmin)
- admin 사이트에서 각 필드 보여주기 (예시)
    ```py
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ['pk', 'title', 'content', 'created_at', 'updated_at']
    ```

#### ※ sql 데이터
- python manage.py shell_plus
- 모델명.objects.querysetApi()
- [참고] (https://docs.djangoproject.com/en/4.2/ref/models/querysets/)
- ✔ 파이썬처럼 사용가능

---

#### 1. Static files
- 기본경로: apps/static/apps/ 경로에 이미지 파일 배치
```py
{% load static %}
<img src="{% static 'apps/img-1.png' %}" alt="img">
```

- 추가경로 설정
```py
# settings.py

# 기본 경로 및 추가경로에 위치한 정적파일을 참조하기 위한 url
STATIC_URL = 'static/'
# 임의의 추가 경로 설정
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

-> html
<img src="{% static 'img-2.png' %}" alt="img">
```

#### 2. Media files
- 사전 준비
```py
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'
```

- url 지정
```py
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 이미지 업로드
```py
-> 모델 필드 추가
# apps/models.py

class App(models.Model):
    image = models.ImageField(blank=True, upload_to='images/' or '%Y%m%d/'),

-> 라이브러리 설치 및 모델 등록
pip install pillow

python manage.py makemigrations
python manage.py migrate

pip freeze > requirements.txt

-> html 이미지 폼
# apps/create.html

<form action="{% url '' %}" method="POST" enctype="multipart/form-data">

-> view 함수 수정
# apps/views.py

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
```

- 업로드 이미지 제공
```py
# apps/detail.html

<img src="{{ article.image.url }}" alt="img">
```