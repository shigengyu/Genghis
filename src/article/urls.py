from django.conf.urls import patterns, url
from article.views import ArticleView, ArticleUpdate, ArticleCreate

urlpatterns = patterns('',
    url(r'^$', ArticleView.as_view()),
    url(r'^create/$', ArticleCreate.as_view()),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdate.as_view()),
)
