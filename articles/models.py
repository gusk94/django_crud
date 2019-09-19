from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # auto_now_add 는 추가할 때의 시간, auto_now는 지금 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # python manage.py makemigrations : 스키마를 어떻게 만들 것인지 장고에게 알려줌(모델 정의 알려줌)
    # python manage.py migrate : 실제 스키마를 만듦, 데이터베이스 테이블을 만든다.