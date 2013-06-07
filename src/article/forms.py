from django.forms.models import ModelForm
from article.models import Article, ArticleTag
from django.forms.widgets import TextInput, Textarea, SelectMultiple

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('subject', 'content', 'tags', 'attachments')
        widgets = {
            'subject': TextInput(attrs={'class':'span11'}),
            'content': Textarea(attrs={'class':'span11', 'rows': '10'}),
            'tags': SelectMultiple(attrs={'class':'span3'}),
            'attachments': SelectMultiple(attrs={'class':'span11'}),
        }
    

class ArticleTagForm(ModelForm):
    class Meta:
        model = ArticleTag
        fields = ('name', 'display_name')
        widgets = {
            'name': TextInput(attrs={'class':'span5'}),
            'display_name': TextInput(attrs={'class':'span5'}),
        }
