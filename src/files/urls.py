from django.conf.urls import patterns, url
from files.views import FileList, FileUpload, FileUpdate, FileDelete

urlpatterns = patterns('',
    url(r'^$', FileList.as_view()),
    url(r'^upload/$', FileUpload.as_view()),
    url(r'^update/(?P<pk>\d+)/$', FileUpdate.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', FileDelete.as_view()),
)
