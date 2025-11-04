from django.urls import path, include, re_path
from django.utils.functional import new_method_proxy

from login import views

urlpatterns = [
    re_path('^index/$', views.index, name='index'),
    re_path('^login/$', views.login, name='login'),
    re_path('^register/$', views.register, name='register'),
    re_path('^logout/$', views.logout, name='logout'),
]