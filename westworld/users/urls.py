from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/(?P<user_id>[0-9]+)/$', views.home, name='home')
]
