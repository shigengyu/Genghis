from django.conf.urls import patterns, url
from article.views import ArticleView, ArticleUpdate, ArticleCreate

urlpatterns = patterns('',
    url(r'^$', ArticleView.as_view(), name = 'article_list'),
    url(r'^create/$', ArticleCreate.as_view(), name = 'article_create'),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdate.as_view(), name = 'article_update'),
)
