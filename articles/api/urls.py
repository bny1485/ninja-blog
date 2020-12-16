from django.urls import path

from articles.api.views import api_view

app_name = 'articles'

urlpatterns = [
    path('<slug>/', api_view, name='detail'),
]