from django.urls import path

from articles.api.views import api_detail_view, api_update_view, api_create_view, api_delete_view, ApiBlogListView

app_name = 'articles'

urlpatterns = [
    path('<slug>/', api_detail_view, name='detail'),
    path('<slug>/update', api_update_view, name='detail'),
    path('<slug>/delete', api_delete_view, name='delete'),
    path('create', api_create_view, name='create'),
    path('list', ApiBlogListView.as_view(), name='list'),
]
