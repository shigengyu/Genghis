from datetime import datetime
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from article.forms import ArticleForm
from django.http.response import HttpResponseRedirect
from article.models import Article

class ArticleView(TemplateView):
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.order_by('-create_date_time')
        return context

class ArticleCreate(CreateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = '/article'
    
    def form_valid(self, form):
        data = form.save(commit=False)
        current_time = datetime.now()
        data.create_date_time = current_time
        data.update_date_time = current_time
        data.author = 'Univer'
        data.save()
        return super(ArticleCreate, self).form_valid(form)
        
class ArticleUpdate(TemplateView):
    template_name = 'article_edit.html'