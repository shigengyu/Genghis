from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from files.models import File
from files.forms import FileForm
from home.models import PathItem

class FileList(TemplateView):
    template_name = 'file_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(FileList, self).get_context_data(**kwargs)
        context['files'] = File.objects.order_by('-upload_date_time').select_related()
        context['path'] = (PathItem('/files', 'Files'),)
        return context

class FileUpload(CreateView):
    template_name = 'file_form.html'
    form_class = FileForm
    success_url = '/files'
    
    def get_context_data(self, **kwargs):
        context = super(FileUpload, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/files', 'Files'), PathItem('/files/upload', 'Upload File'))
        return context
    
    def form_valid(self, form):
        if (not self.request.user.is_authenticated()):
            return HttpResponseRedirect('/home/login')
        
        data = form.save(commit=False)
        data.upload_date_time = datetime.now()
        data.uploaded_by = self.request.user
        data.save()
        return super(FileUpload, self).form_valid(form)