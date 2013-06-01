# Create your views here.
from django.views.generic.base import TemplateView

class PhotoView(TemplateView):
    template_name = 'photos.html'
    