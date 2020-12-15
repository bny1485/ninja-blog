from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'articles/article_detail.html', context)


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to data base
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list_article")
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
