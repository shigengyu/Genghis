from django.forms.models import ModelForm
from files.models import File
from django.forms.widgets import TextInput, Textarea, FileInput

class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = ('name', 'description', 'attachment')
        widgets = {
            'name': TextInput(attrs={'class':'span11'}),
            'description': Textarea(attrs={'class':'span11', 'rows': '10'}),
            'attachment': FileInput(attrs={'class':'span11'})
        }

class FileUpdateForm(ModelForm):
    class Meta:
        model = File
        fields = ('name', 'description')
        widgets = {
            'name': TextInput(attrs={'class':'span11'}),
            'description': Textarea(attrs={'class':'span11', 'rows': '10'}),
        }