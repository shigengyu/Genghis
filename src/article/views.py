# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from article.models import Article

class ArticleView(TemplateView):
    template_name = 'articles.html';

class ArticleCreate(CreateView):
    model = Article
    
class ArticleUpdate(UpdateView):
    model = Article
    fields = ['subject', 'content']

class ArticleDelete(DeleteView):
    model = Article
    success_url = '/article'