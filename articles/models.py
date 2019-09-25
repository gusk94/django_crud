from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    # 문자열 빈 값 저장 : null X , ''로 저장
    content = models.TextField()
    # blank: 데이터 유효성과 관련되어 있다.
    # null : DB 와 관련되어 있다.
    # '', Null
    image = models.ImageField(blank=True)
    # auto_now_add 는 추가할 때의 시간, auto_now는 지금 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # python manage.py makemigrations : 스키마를 어떻게 만들 것인지 장고에게 알려줌(모델 정의 알려줌)
    # python manage.py migrate : 실제 스키마를 만듦, 데이터베이스 테이블을 만든다.


class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article 이 삭제되면 Comment 도 함께 삭제'
    # related_name == 'Article instance 가 comment 를 역참조 할 수 있는 이름을 정의 / related_name 이 없을 경우 comment_set 이 참조 이름(default))
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content
