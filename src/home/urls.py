from django.conf.urls import patterns, url
from home.views import HomeView, LoggedInView, LoginView, LogoutView, IconsView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^logged-in/', LoggedInView.as_view()),
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^icons/', IconsView.as_view()),
)