from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

app_name = "articles"

urlpatterns = [
    path('', views.article_list, name='list_article'),
    path('create/', views.article_create, name='create_article'),
    path('<slug>/', views.article_detail, name='datail_article'),
]
