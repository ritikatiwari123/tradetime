from django.urls import path

from . import views
from .views import *

app_name = 'user'
urlpatterns = [
    path('login/', userauth_login.as_view(), name= 'LoginPage'),
    path('auth/', views.login, name= 'auth'),

]
