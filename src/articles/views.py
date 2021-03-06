from datetime import datetime
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect, HttpResponse, \
    HttpResponseNotFound, HttpResponseForbidden
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from articles.models import Article, ArticleTag, ArticleComment
from articles.forms import ArticleForm, ArticleTagForm, ArticleCommentForm
from home.models import PathItem
from home.authentication import require_login, require_admin, is_admin
import wordpress

ARTICLE_PATH_ITEM = PathItem('/articles', 'Article')

class ArticleList(TemplateView):
    template_name = 'article_list.html'
  
    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        
        '''
        articles = Article.objects
        if not self.request.user.is_authenticated() or not is_admin(self.request.user):
            articles = articles.filter(is_draft=False)
        articles = articles.order_by('-create_date_time').select_related()
        '''
        
        '''
            Read articles from wordpress database and create article objects
        '''
        
        context['articles'] = wordpress.fetch_articles()
        context['path'] = (ARTICLE_PATH_ITEM,)
        context['tags'] = ArticleTag.objects
        return context


class ArticleListByTag(TemplateView):
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListByTag, self).get_context_data(**kwargs)
        articles = Article.objects.filter(tags__name=self.kwargs['slug']).select_related()
        context['articles'] = articles
        context['path'] = (ARTICLE_PATH_ITEM,)
        context['tags'] = ArticleTag.objects
        return context


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        article = self.object
        context['article'] = article
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/detail/' + str(self.object.pk), 'Article Detail'))
        context['comment_action'] = 'create'
        context['comment_form'] = ArticleCommentForm({'article': self.object})
        return context


class ArticleCreate(CreateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = '/articles'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(ArticleCreate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleCreate, self).get_context_data(**kwargs)
        context['action'] = 'create'
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/create', 'Create Article'))
        return context

    @require_admin
    def form_valid(self, form):
        data = form.save(commit=False)
        current_time = datetime.utcnow()
        data.create_date_time = current_time
        data.update_date_time = current_time
        data.author = self.request.user
        data.save()
        return super(ArticleCreate, self).form_valid(form)
        

class ArticleUpdate(UpdateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    success_url = '/articles'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(ArticleUpdate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleUpdate, self).get_context_data(**kwargs)
        context['action'] = 'update'
        context['id'] = self.object.pk
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/update/' + str(self.object.pk), 'Update Article'))
        return context
    
    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset
    
    @require_admin
    def form_valid(self, form):
        data = self.object
        if self.object.author != self.request.user:
            return HttpResponseForbidden()
        
        data.update_date_time = datetime.utcnow()
        return super(ArticleUpdate, self).form_valid(form)

    def get_success_url(self):
        return '/articles/detail/' + str(self.object.id)
        

class ArticleDelete(DeleteView):
    template_name = 'article_confirm_delete.html'
    form_class = ArticleForm
    success_url = '/articles'
    
    @require_admin
    def get(self, request, *args, **kwargs):        
        return super(ArticleDelete, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDelete, self).get_context_data(**kwargs)
        context['id'] = self.object.pk
        context['article'] = self.object
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/delete/' + str(self.object.pk), 'Confirm Delete Article'))
        return context
    
    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset

    @require_admin
    def delete(self, request, *args, **kwargs):
        return super(ArticleDelete, self).delete(request)


class ArticleTagList(TemplateView):
    template_name = 'article_tag_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTagList, self).get_context_data(**kwargs)
        context['article_tags'] = ArticleTag.objects.order_by('display_name')
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/tag', 'Tags'))
        return context


class ArticleTagCreate(CreateView):
    template_name = 'article_tag_form.html'
    form_class = ArticleTagForm
    success_url = '/articles/tag'

    @require_admin
    def get(self, request, *args, **kwargs):
        return super(ArticleTagCreate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ArticleTagCreate, self).get_context_data(**kwargs)
        context['action'] = 'create'
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/tag', 'Tags'), PathItem('/articles/tag/create', 'Create Tag'))
        return context

    @require_admin
    def form_valid(self, form):
        data = form.save(commit=False)
        data.save()
        return super(ArticleTagCreate, self).form_valid(form)


class ArticleTagUpdate(UpdateView):
    template_name = 'article_tag_form.html'
    form_class = ArticleTagForm
    success_url = '/articles/tag'

    @require_admin
    def get(self, request, *args, **kwargs):
        return super(ArticleTagUpdate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTagUpdate, self).get_context_data(**kwargs)
        context['action'] = 'update'
        context['id'] = self.object.pk
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/tag', 'Tags'), PathItem('/articles/tag/update/' + str(self.object.pk), 'Update Tag'))
        return context
    
    def get_queryset(self):
        queryset = ArticleTag.objects.all()
        return queryset

    @require_admin
    def form_valid(self, form):
        return super(ArticleTagUpdate, self).form_valid(form)


class ArticleTagDelete(DeleteView):
    template_name = 'article_tag_confirm_delete.html'
    form_class = ArticleTagForm
    success_url = '/articles/tag'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(ArticleTagDelete, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTagDelete, self).get_context_data(**kwargs)
        context['tag'] = self.object
        context['path'] = (ARTICLE_PATH_ITEM, PathItem('/articles/tag', 'Tags'), PathItem('/articles/tag/delete/' + str(self.object.pk), 'Confirm Delete Article Tag'))
        return context
    
    def get_queryset(self):
        queryset = ArticleTag.objects.all()
        return queryset
    
    @require_admin
    def delete(self, request, *args, **kwargs):
        return super(ArticleTagDelete, self).delete(request)

class ArticlesRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        return '/wp'

def get_article_comment(request, *args, **kwargs):
    
    if request.is_ajax() and request.method == 'GET':
        comment_id = kwargs.get('pk')
        comment = ArticleComment.objects.get(id=comment_id)
        data = {
                'id': comment_id,
                'content': comment.content
                }
        return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    else:
        return HttpResponseNotFound()

@csrf_exempt
def create_article_comment(request, *args, **kwargs):
    
    if request.is_ajax() and request.method == 'POST':
        if (not request.user.is_authenticated()):
            return_url = request.get_full_path()
            return HttpResponseRedirect('/home/login?next=' + return_url)
        
        comment = ArticleComment()
        comment.article_id = request.POST['article_id']
        comment.content = request.POST['content']
        current_time = datetime.utcnow()
        comment.create_date_time = current_time
        comment.update_date_time = current_time
        comment.author = request.user
        comment.save(force_insert=True)
        data = {'success': True}
        return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    else:
        return HttpResponseNotAllowed()

@csrf_exempt
def update_article_comment(request, *args, **kwargs):
    
    if request.is_ajax() and request.method == 'POST':
        if (not request.user.is_authenticated()):
            return_url = request.get_full_path()
            return HttpResponseRedirect('/home/login?next=' + return_url)
        
        comment_id = kwargs.get('pk')
        comment = ArticleComment.objects.get(id=comment_id)
        
        if (request.user == comment.author):
            comment.content = request.POST['content']
            comment.save()
            data = {'success': True}
        else:
            data = {'success': False, 'message': 'You are not the author of the comment'}
        return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    else:
        return HttpResponseNotAllowed()

@csrf_exempt
def delete_article_comment(request, *args, **kwargs):
    
    if request.is_ajax() and request.method == 'POST':
        if (not request.user.is_authenticated()):
            data = {'success': False, 'message': 'Please login to delete comment'}
        
        comment_id = kwargs.get('pk')
        comment = ArticleComment.objects.get(id=comment_id)
        
        if (request.user == comment.author or is_admin(request.user)):
            comment.delete()
            data = {'success': True}
        else:
            data = {'success': False, 'message': 'You are not the author of the comment'}
        
        return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    else:
        return HttpResponseNotAllowed()