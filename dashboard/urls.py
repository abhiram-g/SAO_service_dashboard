from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.services, name='services'),
    url(r'^(?P<service_chosen>[a-zA-Z0-9_]+)/$', views.subservices, name='subservices'),
    url(r'^(?P<service_chosen>[a-zA-Z0-9_]+)/(?P<subservice_chosen>[a-zA-Z0-9_]+)/$', views.service_function, name='service_function'),
]
