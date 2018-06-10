from django.conf.urls import include, url
from django.contrib import admin
from liuyan_01 import urls
from liuyan_01 import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'liuyan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('liuyan_01.urls',namespace='liuyan_01')),
]
