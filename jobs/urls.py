from django.urls import path
from . import views # 같은 경로의 views.py 가져와서 함수를 사용할 수 있게 함

app_name= 'jobs'
urlpatterns = [
    path('', views.new, name='new'),
]
