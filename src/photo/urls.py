from django.conf.urls import patterns, url
from photo.views import PhotoView

urlpatterns = patterns('',
    url(r'^$', PhotoView.as_view()),
)
