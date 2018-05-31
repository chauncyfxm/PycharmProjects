from django.conf.urls import include, url
from . import views



urlpatterns = [
    # index
    url(r'^$', views.index,name = 'index'),

    # editpage
    url(r'^editpage/$', views.editpage, name = "editpage"),

    # datail
    url(r'^datail/(\d*)$', views.datail, name = 'datail'),

    # editpagehandle
    url(r'^editpagehandle/$', views.editpagehandle, name = 'editpagehandle'),

    # login
    url(r'login/$', views.login, name='login'),
    url(r'login_handle/$', views.login_handle, name='login_handle'),
    url(r'logout/$', views.logout, name='logout'),

    # record
    url(r'record/$', views.record, name='record'),
    url(r'record_handle/$', views.record_handle, name='record_handle'),


    # ajax
    url(r'ajax/$', views.ajax, name='ajax'),

    # myblog
    url(r'myblog/$', views.myblog, name='myblog')
]