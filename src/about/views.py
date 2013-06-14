from django.views.generic.base import TemplateView
from home.models import PathItem

class AboutWebsiteView(TemplateView):
    template_name = "website.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutWebsiteView, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/about/website/', 'About Website'), )
        return context

class AboutProfileView(TemplateView):
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutProfileView, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/about/profile/', 'Profile'), )
        return context