# Create your views here.
from django.views.generic.base import TemplateView

class ArticleView(TemplateView):
    
    template_name = "articles.html";