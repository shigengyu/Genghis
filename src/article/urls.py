from django.conf.urls import patterns, url
from article.views import ArticleView

urlpatterns = patterns('',
    url(r'^$', ArticleView.as_view()),
)
