# Create your views here.
from django.views.generic.base import TemplateView, View
from django.http.response import HttpResponseRedirect

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'
    
    def get(self, request):
        if (request.user.is_authenticated()):
            response = HttpResponseRedirect('/')
            return response
        else:
            return super(LoginView, self).get(self, request)


class LoggedInView(TemplateView):
    template_name = 'index.html'


class LogoutView(View):
    def get(self, request):
        response = HttpResponseRedirect('/')
        response.set_cookie('sessionid', None)
        return response
