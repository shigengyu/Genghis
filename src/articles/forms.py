from django.forms.models import ModelForm
from articles.models import Article, ArticleTag, ArticleComment
from django.forms.widgets import TextInput, Textarea, SelectMultiple, HiddenInput

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

class ArticleCommentForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ArticleCommentForm, self).__init__(*args, **kwargs)
        article = kwargs.get('article')
        self.fields['article'].initial = article
    
    class Meta:
        model = ArticleComment
        fields = ('article', 'content',)
        widgets = {
            'article': HiddenInput(),
            'content': Textarea(attrs={'class':'span12', 'rows': '5'}),
        }
