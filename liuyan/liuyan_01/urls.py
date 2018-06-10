from django.conf.urls import include, url
from django.contrib import admin
from liuyan_01 import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'liuyan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/$', 'liuyan_01.views.index', name='index'),
    url(r'^login/$', 'liuyan_01.views.login', name='login'),
    url(r'^record/$', 'liuyan_01.views.record', name='record'),
    url(r'^edit/$', 'liuyan_01.views.edit', name='edit'),
    url(r'^edit01/$', 'liuyan_01.views.edit01', name='edit01'),
    url(r'^login01/$', 'liuyan_01.views.login01', name='login01'),
    url(r'^record01/$', 'liuyan_01.views.record01', name='record01'),
]
