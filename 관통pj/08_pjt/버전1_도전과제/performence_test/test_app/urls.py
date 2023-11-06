from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data),
    path('nan_data/', views.nan_data),
    path('algorithm/', views.algorithm),
]

