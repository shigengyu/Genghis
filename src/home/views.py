# Create your views here.
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class LoggedInView(TemplateView):
    template_name = 'index.html'