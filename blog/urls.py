from django.urls import path, re_path
from django.contrib import admin
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index),
    path('appeal/', views.appeal_create),
    path('search/', views.search),
    path('list/', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('index/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('crawler/', views.crawler),
    re_path('detail/(\d+)/$', views.detail)
]

urlpatterns += [
    path('', RedirectView.as_view(url='/index/')),
]