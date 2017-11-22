from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.dashboard),
    url(r'^pokes/(?P<id>\d+)/$', views.poke),
]
