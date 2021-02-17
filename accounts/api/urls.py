from django.urls import path
from accounts.api.views import registration_view, updata_account_view, account_properties_view

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'


urlpatterns = [
    path('registr', registration_view, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('properties', account_properties_view, name='properties'),
    path('properties/update', updata_account_view, name='update'),
]
