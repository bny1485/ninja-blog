from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'articles/article_detail.html', context)

def article_create(request):
    return render(request, 'articles/article_create.html')