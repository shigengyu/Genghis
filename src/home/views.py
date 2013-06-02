# Create your views here.
from django.views.generic.base import TemplateView, View
from django.http.response import HttpResponseRedirect

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class LoggedInView(TemplateView):
    template_name = 'index.html'

class LogoutView(View):
    def get(self, request):
        response = HttpResponseRedirect('/')
        response.set_cookie('sessionid', None)
        return response
