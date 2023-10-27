from django.urls import path
from . import views


urlpatterns = [
    # 1. 날씨 API 테스트
    path('', views.index),
    # 2. 서울의 5일 치 예보 데이터 확인
    path('save-data/', views.save_data),
    # 3. 예보 데이터 중 원하는 데이터만 DB 저장
    path('list-data/', views.list_data),
    # 4. 저장된 데이터 전체 조회
    path('hot-weathers/', views.hot_weathers),
    # 5. 특정 조건 데이터 확인 : 섭씨 30도 이상 시간대 조회
]
