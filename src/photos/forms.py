from django.forms.models import ModelForm
from photos.models import Photo
from django.forms.widgets import TextInput, Textarea, FileInput, DateInput

class PhotoUploadForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'description', 'source', 'date', 'attachment')
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
        fields = ('name', 'description', 'source', 'date')
        widgets = {
            'name': TextInput(attrs={'class':'span11'}),
            'description': Textarea(attrs={'class':'span11', 'rows': '10'}),
            'source': TextInput(attrs={'class':'span11'}),
            'date': DateInput(attrs={'class':'span11'}),
        }