from django.conf.urls import patterns, url
from home.views import HomeView, LoggedInView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^logged-in/', LoggedInView.as_view()),
)