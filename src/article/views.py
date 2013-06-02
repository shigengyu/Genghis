from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from article.models import Article, ArticleTag
from article.forms import ArticleForm, ArticleTagForm
from home.models import PathItem


class ArticleList(TemplateView):
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.order_by('-create_date_time')
        context['path'] = (PathItem('/article', 'Article'),)
        return context

class ArticleCreate(CreateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = '/article'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleCreate, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/article', 'Article'), PathItem('/article/create', 'Create Article'))
        return context
    
    def form_valid(self, form):
        data = form.save(commit=False)
        current_time = datetime.now()
        data.create_date_time = current_time
        data.update_date_time = current_time
        data.author = request.user.get_full_name()
        data.save()
        return super(ArticleCreate, self).form_valid(form)
        
class ArticleUpdate(UpdateView):
    template_name = 'article_form.html'


class ArticleTagList(TemplateView):
    template_name = 'article_tag_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTagList, self).get_context_data(**kwargs)
        context['article_tags'] = ArticleTag.objects.order_by('display_name')
        context['path'] = (PathItem('/article', 'Article'), PathItem('/article/tag', 'Tags'))
        return context

class ArticleTagCreate(CreateView):
    template_name = 'article_tag_form.html'
    form_class = ArticleTagForm
    success_url = '/article/tag'

    def get_context_data(self, **kwargs):
        context = super(ArticleTagCreate, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/article', 'Article'), PathItem('/article/tag', 'Tags'), PathItem('/article/tag/create', 'Create Tag'))
        return context

    def form_valid(self, form):
        data = form.save(commit=False)
        data.save()
        return super(ArticleTagCreate, self).form_valid(form)
