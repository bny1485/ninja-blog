from django.shortcuts import render
from .models import Article

# Create your views here.
def article(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'article.html', {'articles': articles})
