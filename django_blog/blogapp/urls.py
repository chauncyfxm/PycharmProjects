"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.index, name='index'),
    # 列表
    url(r'^search$', views.SearchView.as_view(), name='search'),
    url(r'^list$', views.blog_list, name='blog_list'),
    url(r'^category/(?P<cid>[0-9]+)/$', views.blog_list, name='category'),
    url(r'^blog/(?P<bid>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^comment/(?P<bid>[0-9]+)/$', views.CommentView.as_view(), name='comment'),
]
