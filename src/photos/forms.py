from django.forms.models import ModelForm
from photos.models import Photo
from django.forms.widgets import TextInput, Textarea, FileInput, DateInput
from genghis import settings

class PhotoUploadForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'description', 'source', 'date', 'attachment', 'display_in_gallery')
        widgets = {
            'name': TextInput(attrs={'class':'span11'}),
            'description': Textarea(attrs={'class':'span11', 'rows': '10'}),
            'source': TextInput(attrs={'class':'span11'}),
            'date': DateInput(attrs={'class':'span11'}),
            'attachment': FileInput(attrs={'class':'span11'})
        }

class PhotoUpdateForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'description', 'source', 'date', 'display_in_gallery')
        widgets = {
            'name': TextInput(attrs={'class':'span11'}),
            'description': Textarea(attrs={'class':'span11', 'rows': '10'}),
            'source': TextInput(attrs={'class':'span11'}),
            'date': DateInput(attrs={'class':'span11'}),
        }