from django.conf.urls import include, url
from django.contrib import admin

import modeldemo
urlpatterns = [
    url(r'index/', 'modeldemo.views.home'),
]