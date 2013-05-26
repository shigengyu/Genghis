# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from article.models import Article

class ArticleView(TemplateView):
    template_name = 'articles.html';

class ArticleCreate(CreateView):
    model = Article
    fields = ['subject', 'content']
    
class ArticleUpdate(CreateView):
    model = Article
    fields = ['subject', 'content']

class ArticleDelete(CreateView):
    model = Article
    success_url = '/article'