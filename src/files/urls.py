from django.conf.urls import patterns, url
from files.views import FileList, FileUpload

urlpatterns = patterns('',
    url(r'^$', FileList.as_view()),
    url(r'^upload/$', FileUpload.as_view()),
)
