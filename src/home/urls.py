from django.conf.urls import patterns, url
from home.views import HomeView, LoggedInView, LoginView, LogoutView,\
    WikiRedirectView, MySqlRedirectView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^logged-in/', LoggedInView.as_view()),
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^wiki/', WikiRedirectView.as_view()),
    url(r'^mysql/', MySqlRedirectView.as_view()),
)