from django.conf.urls import patterns, url
from photos.views import PhotoView

urlpatterns = patterns('',
    url(r'^$', PhotoView.as_view()),
)
