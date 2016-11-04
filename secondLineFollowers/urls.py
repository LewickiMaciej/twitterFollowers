from django.conf.urls import url

from . import views

app_name = 'secondLineFollowers'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'pin/$', views.pin, name='pin'),
	url(r'followers/followers/$', views.followers, name='followers'),
	url(r'json/$', views.json, name='json'),
]
