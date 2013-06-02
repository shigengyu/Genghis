from django.forms.models import ModelForm
from article.models import Article
from django.forms.widgets import TextInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('subject', 'content' )
        widgets = {
            'subject': TextInput(attrs={'class':'span11'}),
            'content': Textarea(attrs={'class':'span11', 'rows': '10'}),
        }