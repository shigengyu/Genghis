from django.conf.urls import patterns, url
from home.views import HomeView, FacebookLoginView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^facebook-login/', FacebookLoginView.as_view()),
)