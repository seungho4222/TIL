from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('login/', views.login, name='login'),
    path('hello/<name>/', views.hello, name='hello'),
    path('age/<int:age>/', views.age, name='age')
]
