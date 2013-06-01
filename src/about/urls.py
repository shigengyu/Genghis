from django.conf.urls import patterns, url
from about.views import AboutView

urlpatterns = patterns('',
    url(r'^$', AboutView.as_view()),
    url(r'^profile/', AboutView.as_view()),
)