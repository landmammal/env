from django.conf.urls import url
from . import views

app_name = "users"
urlpatterns = [
    url(r'^home/(?P<user_id>[0-9]+)/$', views.home, name='home'),
    url(r'^index/$', views.UserListView.as_view(), name='index'),
    url(r'^add/$', views.add, name='add')
]
