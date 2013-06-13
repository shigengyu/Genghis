from django.conf.urls import patterns, url
from photos.views import PhotoList, PhotoUpload, PhotoUpdate, PhotoDelete

urlpatterns = patterns('',
    url(r'^$', PhotoList.as_view()),
    url(r'^upload/$', PhotoUpload.as_view()),
    url(r'^update/(?P<pk>\d+)/$', PhotoUpdate.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', PhotoDelete.as_view()),
)
