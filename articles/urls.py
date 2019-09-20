from django.urls import path
from . import views # 같은 경로의 views.py 가져와서 함수를 사용할 수 있게 함

# /articles/__ 의 경로
app_name= 'articles'
urlpatterns = [
    # 이름을 지정해줘서 경로를 바꾸더라도 찾아갈 수 있도록 함
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'), # detail
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    # /article/3/comments/
    path('<int:article_pk>/comments', views.comments_create, name='comments_create')
]