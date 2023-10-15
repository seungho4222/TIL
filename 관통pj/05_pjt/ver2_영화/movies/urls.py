from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/create', views.comments_create, name='comments_create'),
    path('<int:movie_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]
