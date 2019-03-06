"""为应用程序users定义URL模式"""
from django.urls import path,re_path
from django.contrib.auth import login
from .import views

urlpatterns = [
    #登录页面
    re_path('^login/$',login,{'template_name':'users/login.html'},name='login'),
]

app_name = 'users'