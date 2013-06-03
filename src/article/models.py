from django.db import models
from django.db.models.base import Model
from django.db.models import permalink
from django.forms.forms import Form

class ArticleTag(Model):
    name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name


class Article(Model):
    subject = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=50)
    create_date_time = models.DateTimeField()
    update_date_time = models.DateTimeField()
    tags = models.ManyToManyField(ArticleTag)
    
    def __unicode__(self):
        return self.subject

class ArticleForm(Form):
    class Meta:
        model = Article

class ArticleComment(Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article)
    subject = models.CharField(max_length=256)
    content = models.TextField()
    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.subject
