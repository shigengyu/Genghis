from django.views.generic.base import TemplateView, View
from django.http.response import HttpResponseRedirect
from home.models import PathItem
from home.authentication import is_admin

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['is_admin'] = is_admin(self.request.user)
        return context

class LoginView(TemplateView):
    template_name = 'login.html'
    
    def get(self, request):
        if (request.user.is_authenticated()):
            response = HttpResponseRedirect(next)
            return response
        else:
            return super(LoginView, self).get(self, request)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        context['path'] = (PathItem('/home/login', 'Login'),)
        return context

class LoggedInView(TemplateView):
    template_name = 'index.html'


class LogoutView(View):
    def get(self, request):
        response = HttpResponseRedirect('/')
        response.set_cookie('sessionid', None)
        return response
