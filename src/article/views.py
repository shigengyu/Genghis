# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from article.forms import ArticleForm

class ArticleView(TemplateView):
    template_name = 'articles.html'

class ArticleCreate(CreateView):
    template_name = 'article_form.html';
    form_class = ArticleForm

class ArticleUpdate(TemplateView):
    template_name = 'article_edit.html'
