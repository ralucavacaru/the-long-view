from django.conf.urls import include, url
from django.contrib import admin

from timeline import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^timeline', views.timeline, name='timeline'),
	url(r'^definitions', views.definitions, name='definitions'),
	url(r'^history', views.history, name='history'),
	url(r'^references', views.references, name='references'),
    url(r'^admin/', include(admin.site.urls)),
]
