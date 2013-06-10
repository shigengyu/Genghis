from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from article.models import Article, ArticleTag
from article.forms import ArticleForm, ArticleTagForm
from home.models import PathItem
from home.authentication import RequireLogin, RequireAdmin

ARTICLE_PATH_ITEM = PathItem('/article', 'Article')

class ArticleList(TemplateView):
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.order_by('-create_date_time').select_related()
        context['path'] = (ARTICLE_PATH_ITEM,)
        return context


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['article'] = self.object
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/detail/' + str(self.object.pk), 'Article Detail'))
        return context


class ArticleCreate(CreateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = '/article'
    
    @RequireAdmin
    def get(self, request, *args, **kwargs):
        return super(ArticleCreate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleCreate, self).get_context_data(**kwargs)
        context['action'] = 'create'
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/create', 'Create Article'))
        return context

    @RequireAdmin
    def form_valid(self, form):
        if (not self.request.user.is_authenticated()):
            return HttpResponseRedirect('/home/login')
        
        data = form.save(commit=False)
        current_time = datetime.now()
        data.create_date_time = current_time
        data.update_date_time = current_time
        data.author = self.request.user
        data.save()
        return super(ArticleCreate, self).form_valid(form)
        

class ArticleUpdate(UpdateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = '/article'
    
    @RequireAdmin
    def get(self, request, *args, **kwargs):
        return super(ArticleUpdate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleUpdate, self).get_context_data(**kwargs)
        context['action'] = 'update'
        context['id'] = self.object.pk
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/update/' + str(self.object.pk), 'Update Article'))
        return context
    
    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset
    
    @RequireAdmin
    def form_valid(self, form):
        data = self.object
        data.update_date_time = datetime.now()
        return super(ArticleUpdate, self).form_valid(form)


class ArticleDelete(DeleteView):
    template_name = 'article_confirm_delete.html'
    form_class = ArticleForm
    success_url = '/article'
    
    @RequireAdmin
    def get(self, request, *args, **kwargs):
        return super(ArticleDelete, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDelete, self).get_context_data(**kwargs)
        context['id'] = self.object.pk
        context['article'] = self.object
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/delete/' + str(self.object.pk), 'Confirm Delete Article'))
        return context
    
    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset

    @RequireAdmin
    def delete(self, request, *args, **kwargs):
        return super(ArticleDelete, self).delete(request)


class ArticleTagList(TemplateView):
    template_name = 'article_tag_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTagList, self).get_context_data(**kwargs)
        context['article_tags'] = ArticleTag.objects.order_by('display_name')
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/tag', 'Tags'))
        return context


class ArticleTagCreate(CreateView):
    template_name = 'article_tag_form.html'
    form_class = ArticleTagForm
    success_url = '/article/tag'

    @RequireAdmin
    def get(self, request, *args, **kwargs):
        return super(ArticleTagCreate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ArticleTagCreate, self).get_context_data(**kwargs)
        context['action'] = 'create'
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/tag', 'Tags'), PathItem('/article/tag/create', 'Create Tag'))
        return context

    @RequireAdmin
    def form_valid(self, form):
        data = form.save(commit=False)
        data.save()
        return super(ArticleTagCreate, self).form_valid(form)


class ArticleTagUpdate(UpdateView):
    template_name = 'article_tag_form.html'
    form_class = ArticleTagForm
    success_url = '/article/tag'

    @RequireAdmin
    def get(self, request, *args, **kwargs):
        return super(ArticleTagUpdate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTagUpdate, self).get_context_data(**kwargs)
        context['action'] = 'update'
        context['id'] = self.object.pk
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/tag', 'Tags'), PathItem('/article/tag/update/' + str(self.object.pk), 'Update Tag'))
        return context
    
    def get_queryset(self):
        queryset = ArticleTag.objects.all()
        return queryset

    @RequireAdmin
    def form_valid(self, form):
        return super(ArticleTagUpdate, self).form_valid(form)


class ArticleTagDelete(DeleteView):
    template_name = 'article_tag_confirm_delete.html'
    form_class = ArticleTagForm
    success_url = '/article/tag'
    
    @RequireAdmin
    def get(self, request, *args, **kwargs):
        return super(ArticleTagDelete, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTagDelete, self).get_context_data(**kwargs)
        context['tag'] = self.object
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/article/tag', 'Tags'), PathItem('/article/tag/delete/' + str(self.object.pk), 'Confirm Delete Article Tag'))
        return context
    
    def get_queryset(self):
        queryset = ArticleTag.objects.all()
        return queryset
    
    @RequireAdmin
    def delete(self, request, *args, **kwargs):
        return super(ArticleTagDelete, self).delete(request)
