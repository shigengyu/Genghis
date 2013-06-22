from django.conf.urls import patterns, url
from articles.views import ArticleList, ArticleListByTag, ArticleDetail, \
    ArticleCreate, ArticleUpdate, ArticleDelete
from articles.views import ArticleTagList, ArticleTagCreate, ArticleTagUpdate, ArticleTagDelete, \
    get_article_comment, create_article_comment, update_article_comment, delete_article_comment



urlpatterns = patterns('',
    url(r'^$', ArticleList.as_view()),
    url(r'^bytag/(?P<slug>[-\w]+)/$', ArticleListByTag.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', ArticleDetail.as_view()),
    url(r'^create/$', ArticleCreate.as_view()),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdate.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', ArticleDelete.as_view()),
    url(r'^tag/$', ArticleTagList.as_view()),
    url(r'^tag/create/', ArticleTagCreate.as_view()),
    url(r'^tag/update/(?P<pk>\d+)/$', ArticleTagUpdate.as_view()),
    url(r'^tag/delete/(?P<pk>\d+)/$', ArticleTagDelete.as_view()),
    url(r'^comments/create/', create_article_comment),
    url(r'^comments/detail/(?P<pk>\d+)/$', get_article_comment),
    url(r'^comments/update/(?P<pk>\d+)/$', update_article_comment),
    url(r'^comments/delete/(?P<pk>\d+)/$', delete_article_comment),
)
