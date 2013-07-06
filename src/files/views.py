from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from files.models import File
from files.forms import FileUploadForm, FileUpdateForm
from home.models import PathItem
from home.authentication import require_admin

class FileList(TemplateView):
    template_name = 'file_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(FileList, self).get_context_data(**kwargs)
        context['files'] = File.objects.order_by('id').select_related()
        context['path'] = (PathItem('/files', 'Files'),)
        return context

class FileUpload(CreateView):
    template_name = 'file_upload.html'
    form_class = FileUploadForm
    success_url = '/files'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(FileUpload, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(FileUpload, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/files', 'Files'), PathItem('/files/upload', 'Upload File'))
        return context

    @require_admin
    def form_valid(self, form):
        data = form.save(commit=False)
        data.upload_date_time = datetime.utcnow()
        data.uploaded_by = self.request.user
        data.save()
        return super(FileUpload, self).form_valid(form)

class FileUpdate(UpdateView):
    template_name = 'file_update.html'
    form_class = FileUpdateForm
    success_url = '/files'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(FileUpdate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(FileUpdate, self).get_context_data(**kwargs)
        context['id'] = self.object.pk
        context['path'] = (PathItem('/files', 'Files'), PathItem('/files/update/' + str(self.object.pk), 'Update File'))
        return context
    
    def get_queryset(self):
        queryset = File.objects.all()
        return queryset
    
    @require_admin
    def form_valid(self, form):        
        return super(FileUpdate, self).form_valid(form)

class FileDelete(DeleteView):
    template_name = 'file_confirm_delete.html'
    success_url = '/files'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(FileDelete, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(FileDelete, self).get_context_data(**kwargs)
        context['id'] = self.object.pk
        context['file'] = self.object
        context['path'] = (PathItem('/files', 'Files'), PathItem('/files/delete/' + str(self.object.pk), 'Confirm Delete File'))
        return context
    
    def get_queryset(self):
        queryset = File.objects.all()
        return queryset

    @require_admin
    def delete(self, request, *args, **kwargs):
        return super(FileDelete, self).delete(request)