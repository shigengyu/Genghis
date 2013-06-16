from django.conf.urls import patterns, url
from photos.views import PhotoList, PhotoGallery, PhotoGalleryByTag, PhotoUpload, PhotoUpdate, PhotoDelete
from photos.views import PhotoTagList, PhotoTagCreate, PhotoTagUpdate, PhotoTagDelete

urlpatterns = patterns('',
    url(r'^$', PhotoList.as_view()),
    url(r'^gallery/$', PhotoGallery.as_view()),
    url(r'^gallery/bytag/(?P<slug>[-\w]+)/$', PhotoGalleryByTag.as_view()),
    url(r'^upload/$', PhotoUpload.as_view()),
    url(r'^update/(?P<pk>\d+)/$', PhotoUpdate.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', PhotoDelete.as_view()),
    url(r'^tags/$', PhotoTagList.as_view()),
    url(r'^tags/create/$', PhotoTagCreate.as_view()),
    url(r'^tags/update/(?P<pk>\d+)/$', PhotoTagUpdate.as_view()),
    url(r'^tags/delete/(?P<pk>\d+)/$', PhotoTagDelete.as_view()),
)
