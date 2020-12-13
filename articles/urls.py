from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.article_list),
    path('<slug>/', views.article_detail),
]
