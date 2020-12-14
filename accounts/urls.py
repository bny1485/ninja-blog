from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_views, name='signup'),
    path('login/', views.login_views, name='login'),
]
