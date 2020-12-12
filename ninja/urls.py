from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    path(r'about/', views.about),
    url(r'', views.home),
]


urlpatterns += staticfiles_urlpatterns()