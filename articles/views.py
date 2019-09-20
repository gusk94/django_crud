from django.shortcuts import render, redirect, get_object_or_404
from .models import Article # Article 모델을 사용하기 위해 가져옴

# articles 의 메인 페이지, article list 를 보여 줌
def index(request):
    # SELECT * FROM articles
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


# Variable Routing 으로 사용자가 보기를 원하는 페이지 pk 를 받아서 Detail 페이지를 보여준다
def detail(request, article_pk):
    # SELECT * FROM articles WHERE pk=3
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


# 입력 페이지 제공
# GET /articles/create/
# def new(request):
#     return render(request, 'articles/new.html')


# 데이터를 전달 받아서 article 생성
# POST /articles/create/ -> 작성
def create(request):
    # 아니라면 (POST) 사용자 데이터 받아서 article 생성
    if request.method == 'POST':
        # /articles/new/ 의 new.html 의 form 에서 전달받은 데이터
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        # <a href="/articles/">
        return redirect('articles:detail', article.pk) # redirect 를 불러와 index 페이지로 다시 이동하도록 만든다.
    
    # 만약 GET 요청으로 들어오면 html 페이지 rendering
    else:
        return render(request, 'articles/create.html')


# 사용자로부터 받은 article_pk 값에 해당하는 article 을 삭제
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)


# /articles/pk/update/
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # POST : 실제 Update 로직이 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)

    # GET : Update 를 하기 위한 Form 을 제공하는 페이지
    else:
        context = {'article':article}
        return render(request, 'articles/update.html', context)
