from django.conf.urls import patterns, url
from article.views import ArticleList, ArticleCreate, ArticleUpdate, ArticleDelete
from article.views import ArticleTagList, ArticleTagCreate, ArticleTagUpdate, ArticleTagDelete

urlpatterns = patterns('',
    url(r'^$', ArticleList.as_view()),
    url(r'^create/$', ArticleCreate.as_view()),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdate.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', ArticleDelete.as_view()),
    url(r'^tag/$', ArticleTagList.as_view()),
    url(r'^tag/create/', ArticleTagCreate.as_view()),
    url(r'^tag/update/(?P<pk>\d+)/$', ArticleTagUpdate.as_view()),
    url(r'^tag/delete/(?P<pk>\d+)/$', ArticleTagDelete.as_view()),
)
