from django.conf.urls import patterns, url
from files.views import FileList, FileUpload, FileDelete

urlpatterns = patterns('',
    url(r'^$', FileList.as_view()),
    url(r'^upload/$', FileUpload.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', FileDelete.as_view()),
)
