from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^set/(?P<key>[\w]+)/$', views.set, name='set'),
    url(r'^get/(?P<key>[\w]+)/$', views.get, name='get'),
]
