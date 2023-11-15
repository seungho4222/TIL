## :whale: Front
```md
# base
npm create vue@latest  ->  (router, pinia 선택)
cd pjt  ->  (경로 이동)
npm install
npm run dev


# Local Storage
npm i pinia-plugin-persistedstate

> main.js
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)

> stores/counter.js
export const useCounterStore = defineStore('counter', () => {...
}, { persist: true })


# DRF 서버 AJAX 요청
npm install axios


# 부트스트랩
npm install --save bootstrap
npm i bootstrap-icons

> main.js
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.min.css'
```


## :dog: Back
#### Base
```md
> 가상 환경 생성 및 활성화
python -m venv venv
source venv/Scripts/activate

> 패키지 설치
pip install -r requirements.txt
(pip install django djangorestframework)

> Migration 진행
python manage.py makemigrations
python manage.py migrate

> Fixtures 데이터 로드(있을 경우)
python manage.py loaddata filename.json
```

#### CORS Policy
```py
# 설치
pip install django-cors-headers

# settings.py
INSTALLED_APPS = [
  'corsheaders',
]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]
```

#### DRF Authentication
```py
# 설치
pip install dj-rest-auth
pip install 'dj-rest-auth[with_social]'

# settings.py
INSTALLED_APPS = [
  'rest_framework'
  'rest_framework.authtoken',
  'dj_rest_auth',
  'django.contrib.sites',
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'dj_rest_auth.registration',
]

SITE_ID = 1

REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}


# pjt/urls.py
urlpatterns = [
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]


# apps/view.py
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
  pass


# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

## :bear: TIP
```md
# 환경변수 사용
1. front 폴더에서 .env.local 파일 생성
2. VITE_API_KEY='key' 작성
3. const API_KEY = import.meta.env.VITE_API_KEY
```