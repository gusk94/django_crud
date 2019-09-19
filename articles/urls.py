from django.urls import path
from . import views # 같은 경로의 views.py 가져와서 함수를 사용할 수 있게 함

# /articles/__ 의 경로
urlpatterns = [
    path('', views.index),
    path('<int:article_pk>/', views.detail),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:article_pk>/delete/', views.delete),
]