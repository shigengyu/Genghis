from django.conf.urls import patterns, url
from about.views import AboutWebsiteView, AboutProfileView

urlpatterns = patterns('',
    url(r'^website/', AboutWebsiteView.as_view()),
    url(r'^profile/', AboutProfileView.as_view()),
)