from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from photos.models import Photo, PhotoTag
from photos.forms import PhotoUploadForm, PhotoUpdateForm, PhotoTagForm
from home.models import PathItem
from home.authentication import require_admin

class PhotoList(TemplateView):
    template_name = 'photo_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(PhotoList, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.order_by('date').select_related()
        context['path'] = (PathItem('/photos', 'Photos'),)
        return context


class PhotoGallery(TemplateView):
    template_name = 'photo_gallery.html'
    
    def get_context_data(self, **kwargs):
        context = super(PhotoGallery, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(display_in_gallery=True).order_by('date').select_related()
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/gallery', 'Gallery'))
        return context


class PhotoUpload(CreateView):
    template_name = 'photo_upload.html'
    form_class = PhotoUploadForm
    success_url = '/photos'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(PhotoUpload, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PhotoUpload, self).get_context_data(**kwargs)
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/upload', 'Upload Photo'))
        return context

    @require_admin
    def form_valid(self, form):
        data = form.save(commit=False)
        data.upload_date_time = datetime.now()
        data.uploaded_by = self.request.user
        data.save()
        return super(PhotoUpload, self).form_valid(form)


class PhotoUpdate(UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoUpdateForm
    success_url = '/photos'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(PhotoUpdate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PhotoUpdate, self).get_context_data(**kwargs)
        context['id'] = self.object.pk
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/update/' + str(self.object.pk), 'Update Photo'))
        return context
    
    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset
    
    @require_admin
    def form_valid(self, form):        
        return super(PhotoUpdate, self).form_valid(form)


class PhotoDelete(DeleteView):
    template_name = 'photo_confirm_delete.html'
    success_url = '/photos'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(PhotoDelete, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PhotoDelete, self).get_context_data(**kwargs)
        context['id'] = self.object.pk
        context['photo'] = self.object
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/delete/' + str(self.object.pk), 'Confirm Delete Photo'))
        return context
    
    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset

    @require_admin
    def delete(self, request, *args, **kwargs):
        return super(PhotoDelete, self).delete(request)


class PhotoTagList(TemplateView):
    template_name = 'photo_tag_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(PhotoTagList, self).get_context_data(**kwargs)
        context['photo_tags'] = PhotoTag.objects.order_by('display_name')
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/tag', 'Tags'))
        return context


class PhotoTagCreate(CreateView):
    template_name = 'photo_tag_form.html'
    form_class = PhotoTagForm
    success_url = '/photos/tags'

    @require_admin
    def get(self, request, *args, **kwargs):
        return super(PhotoTagCreate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PhotoTagCreate, self).get_context_data(**kwargs)
        context['action'] = 'create'
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/tag', 'Tags'), PathItem('/photos/tag/create', 'Create Tag'))
        return context

    @require_admin
    def form_valid(self, form):
        data = form.save(commit=False)
        data.save()
        return super(PhotoTagCreate, self).form_valid(form)


class PhotoTagUpdate(UpdateView):
    template_name = 'photo_tag_form.html'
    form_class = PhotoTagForm
    success_url = '/photos/tags'

    @require_admin
    def get(self, request, *args, **kwargs):
        return super(PhotoTagUpdate, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PhotoTagUpdate, self).get_context_data(**kwargs)
        context['action'] = 'update'
        context['id'] = self.object.pk
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/tag', 'Tags'), PathItem('/photos/tag/update/' + str(self.object.pk), 'Update Tag'))
        return context
    
    def get_queryset(self):
        queryset = PhotoTag.objects.all()
        return queryset

    @require_admin
    def form_valid(self, form):
        return super(PhotoTagUpdate, self).form_valid(form)


class PhotoTagDelete(DeleteView):
    template_name = 'photo_tag_confirm_delete.html'
    form_class = PhotoTagForm
    success_url = '/photos/tags'
    
    @require_admin
    def get(self, request, *args, **kwargs):
        return super(PhotoTagDelete, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PhotoTagDelete, self).get_context_data(**kwargs)
        context['tag'] = self.object
        context['path'] = (PathItem('/photos', 'Photos'), PathItem('/photos/tag', 'Tags'), PathItem('/photos/tag/delete/' + str(self.object.pk), 'Confirm Delete Photo Tag'))
        return context
    
    def get_queryset(self):
        queryset = PhotoTag.objects.all()
        return queryset
    
    @require_admin
    def delete(self, request, *args, **kwargs):
        return super(PhotoTagDelete, self).delete(request)
