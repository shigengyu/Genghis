from django.views.generic.base import TemplateView
from home.models import PathItem

class AboutView(TemplateView):
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/about/profile/', 'Profile'), )
        return context