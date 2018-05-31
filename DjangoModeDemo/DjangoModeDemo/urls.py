from django.conf.urls import include, url
from django.contrib import admin
from modeldemo import views

import modeldemo
urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoModeDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('modeldemo.urls')),
    url(r'^index/$',views.index),
    url(r'^index/(\d+?)$',views.datail),

]
