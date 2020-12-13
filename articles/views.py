from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'article.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_detail.html', context)